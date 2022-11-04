from ctypes.wintypes import BOOL
from turtle import delay
from xmlrpc.client import Boolean
import pigpio

from hardwarepwm import PWM
from peltier import PELTIER
from powergpio import POWERGPIO

pi = pigpio.pi()


pwm_example = PWM(pi, GPIOPin=10, DutyCycle=20, Frequency=30) # instantie
pwm_example.set_value(DutyCycle=30, Frequency=50) # gebruik functie

peltier_example = PELTIER(pi, GPIOpeltier_in1 = 2, GPIOpeltier_in2 = 3) # instantie
peltier_example.SetTemperature(2000, 3000) # set dutycycle and frequency

powergpio_example = POWERGPIO(GPIOPin=18, DutyCycle=2100, Frequency=8000)
powergpio_example.set_value(DutyCycle=390, Frequency=580)



class Motors():
    def __init__(self, MOTORnum: int, DIR, STEP, EN, PHASE, SLEEP) -> None:
        self._gpio_MOTOR: int = MOTORnum 
        self._gpio_DIR: int = DIR
        #self._gpio_STEP: int = STEP
        self._gpio_EN: int = EN
        #self._gpio_PHASE: int = PHASE
        self._gpio_SLEEP: int = SLEEP

    def set_motor_power(self, enabled: bool): 
        if enabled == True:
            pi.hardware_PWM(self.MOTORnum, _MAX, _MAX)
        else: 
            pi.hardware_PWM(self.MOTORnum, _MIN, _MIN)

    def set_motor_dir(self, DIR: bool):
        if DIR == 1:
            pi.harware_PWM(self.MOTORnum, _MAX, _MAX) #high on enable pin to enable motor
        else:
            pi.hardware_PWM(self.MOTORnum, _MIN, _MIN) #low on enable pin to enable motor

    def set_motor_step(self, STEP: float):
        for x in range(STEP):
            pi.harware_PWM(self.STEPPIN, _MAX, _MAX) 
            delay(0.001)
            pi.harware_PWM(self.STEPPIN, _MIN, _MIN) 
            delay(0.001)
            STEP + 1
