from enums import State
import constants

"""
This is the PWM class, where software PWM is defined.
"""


class PWM():

    def __init__(self, pi, GPIOPin: int) -> None:
        self._GPIOPin: int = GPIOPin
        self._pigpio = pi
        self.state = None

    def TurnOn(self):
        self._pigpio.set_PWM_dutycycle(self._GPIOPin, constants.MAXPWM)
        self.state = State.ON.name
        return self.state

    def TurnOff(self):
        self._pigpio.set_PWM_dutycycle(self._GPIOPin, constants.MINPWM)
        self.state = State.OFF.name
        return self.state

    def SetValue(self, DutyCycle: int):
        self._pigpio.set_PWM_dutycycle(self._GPIOPin, DutyCycle)
        self.state = State.CUSTOM.name
        return self.state
