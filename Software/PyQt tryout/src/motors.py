import time
import pigpio

_MAX: int = 100_0000
#_MIN: int = 350_000
_OFF: int = 0
#_FREQUENCY = 100_000

class MOTORS():
    def __init__(self, pi, MOTORnum: int, DIR, STEP, EN, PHASE, SLEEP) -> None:
        self._pigpio = pi
        self._gpio_MOTORnum: int = MOTORnum 
        self._gpio_DIR: int = DIR
        #self._gpio_STEP: int = STEP
        self._gpio_EN: int = EN
        #self._gpio_PHASE: int = PHASE
        self._gpio_SLEEP: int = SLEEP
        self.state = ''

    def set_motor_power(self, enabled: bool): 
        if enabled == True:
            self._pigpio.hardware_PWM(self.MOTORnum, _MAX, _MAX)
        else: 
            self._pigpio.hardware_PWM(self.MOTORnum, _OFF, _OFF)

    def set_motor_dir(self, DIR: bool):
        if DIR == 1:
            self._pigpio.harware_PWM(self.MOTORnum, _MAX, _MAX) #high on enable pin to enable motor
        else:
            self._pigpio.hardware_PWM(self.MOTORnum, _OFF, _OFF) #low on enable pin to enable motor

    def set_motor_step(self, STEP: float):
        for x in range(STEP):
            self._pigpio.harware_PWM(self.STEPPIN, _MAX, _MAX) 
            time.sleep(0.001)
            self._pigpio.harware_PWM(self.STEPPIN, _OFF, _OFF) 
            time.sleep(0.001)
            STEP + 1



if __name__ == "__main__":
    