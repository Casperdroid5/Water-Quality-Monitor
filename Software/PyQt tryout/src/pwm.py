import time
import pigpio
from enums import State
import constants

class PWM():

    def __init__(self, pi, GPIOPin: int) -> None:
        self._GPIOPin: int = GPIOPin
        self._pigpio = pi
        self.state = None

    def TurnOn(self):
         self._pigpio.set_PWM_dutycycle(self._GPIOPin, constants.MAXPWM)

    def TurnOff(self):
         self._pigpio.set_PWM_dutycycle(self._GPIOPin, constants.MINPWM)

    def SetValue(self, DutyCycle: int):
         self._pigpio.set_PWM_dutycycle(self._GPIOPin, DutyCycle)