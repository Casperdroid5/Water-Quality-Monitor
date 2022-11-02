import time
import pigpio
from enums import State
import constants

class HARDWAREPWM():

    def __init__(self, pi, GPIOPin: int) -> None:
        self._GPIOPin: int = GPIOPin
        self._pigpio = pi
        self.state = None

    def TurnOn(self):
         self._pigpio.hardware_PWM(self._GPIOPin, constants.MAX, constants.MAX)
         self.state = State.ON.name # was State.ON
         return self.state

    def TurnOff(self):
         self._pigpio.hardware_PWM(self._GPIOPin, constants.MIN, constants.MIN)
         self.state = State.OFF.name
         return self.state

    def SetValue(self, DutyCycle: int, Frequency: int):
         self._pigpio.hardware_PWM(self._GPIOPin, Frequency, DutyCycle)
         self.state = State.CUSTOM.name
         return self.state

