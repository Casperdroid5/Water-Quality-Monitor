import pigpio
from PyQt5.QtCore import QObject, QThread, QMutex, QSettings, pyqtSignal, pyqtSlot
from wait import wait_ms
from time import time


class FocusStepper(QThread):
    postMessage = pyqtSignal(str)

    pio = None  # Reference to PigPIO object
    mutex = QMutex()

    def __init__(self, pio, my_settings: QSettings):
        super().__init__()
        if not isinstance(pio, pigpio.pi):
            raise TypeError("Constructor attribute is not a pigpio.pi instance!")
        self.pio = pio

        self.not_en_pin = my_settings.value('focus_control/motor_not_en_pin', None, int)
        self.step_pin = my_settings.value('focus_control/motor_step_pin', None, int)
        self.dir_pin = my_settings.value('focus_control/motor_dir_pin', None, int)
        self.pwm_frequency = my_settings.value('focus_control/motor_pwm_frequency', None, int)

        self.pio.set_mode(self.not_en_pin, pigpio.OUTPUT)
        self.pio.set_mode(self.step_pin, pigpio.OUTPUT)
        self.pio.set_mode(self.dir_pin, pigpio.OUTPUT)

        self.pio.set_PWM_frequency(self.step_pin, self.pwm_frequency)
        self.pio.set_PWM_dutycycle(self.step_pin, 0)  # switch off PWM
        self.pio.write(self.not_en_pin, 1)  # disable driver
        self.position = None
        self.prev_time_stamp = None

    @pyqtSlot()
    def go_home(self):
        try:
            if self.pio is not None:
                self.pio.set_PWM_frequency(self.step_pin, 1000)  # increase speed
                self.move(50)
                wait_ms(500)  # go up a little
                self.move(-50)
                wait_ms(2500)  # go down a lot
                self.stop()
                self.pio.set_PWM_frequency(self.step_pin, self.pwm_frequency)  # reset speed
                self.position = 0
        except Exception as err:
            self.postMessage.emit(f"{self.__class__.__name__}: error; type: {type(err)}, args: {err.args}")

    @pyqtSlot(int)
    def set_position(self, val):
        """ Set stepper position from home by enabling the PWM for a certain period that roughly
            agrees with the nr of steps. This approach is probably good enough, although not accurate to the step
            :param val: nr of steps from home position
        """
        try:
            if self.prev_time_stamp is not None and (time() - self.prev_time_stamp) < 0.5:
                # skip this signal, they come too fast
                return
            if self.pio is not None:
                if self.mutex.tryLock(100):
                    if self.position is None:
                        self.go_home()
                    # value = int((val - self.position))
                    # self.pio.write(self.not_en_pin, 0)
                    # self.pio.write(self.dir_pin, value >= 0)
                    # for i in range(0, abs(value)):
                    #     # bit bang to position
                    #     self.pio.write(self.step_pin, 1)
                    #     wait_ms(5)
                    #     self.pio.write(self.step_pin, 0)
                    #     wait_ms(5)
                    # self.pio.write(self.not_en_pin, 1)

                    frequency = 1000
                    value = int((val - self.position) * 1000 / frequency)
                    self.pio.set_PWM_frequency(self.step_pin, frequency)  # set well-defined PWM frequency
                    sign = 1 if value > 0 else -1
                    self.move(50 * sign)  # set direction by sign
                    wait_ms(abs(value))
                    self.stop()
                    self.position = val
                    self.prev_time_stamp = time()
                    self.pio.set_PWM_frequency(self.step_pin, self.pwm_frequency)  # reset speed
                    print(self.position, value, sign)
                    self.mutex.unlock()
        except Exception as err:
            self.postMessage.emit(f"{self.__class__.__name__}: error; type: {type(err)}, args: {err.args}")

    @pyqtSlot(int)
    def move(self, val):
        """ Set PWM dutycycle.
            :param val: PWM dutycycle, int between -100 and 100, polarity defines direction
        """
        value = int(round(255 * abs(val) / 100))
        try:
            if self.pio is not None:
                self.pio.write(self.not_en_pin, val == 0)
                self.pio.write(self.dir_pin, val >= 0)
                self.pio.set_PWM_dutycycle(self.step_pin, value)
        except Exception as err:
            self.postMessage.emit(f"{self.__class__.__name__}: error; type: {type(err)}, args: {err.args}")

    @pyqtSlot()
    def stop(self):
        try:
            self.move(0)
        except Exception as err:
            self.postMessage.emit(f"{self.__class__.__name__}: error; type: {type(err)}, args: {err.args}")
