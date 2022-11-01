
_MAX: int = 100
_MIN: int = 0
#_FREQUENCY = 100_000

class PWM():
    def __init__(self, pi, GPIOPin: int) -> None:
        self._GPIOPin: int = GPIOPin
        self._pigpio = pi

    def TurnOn(self):
         self._pigpio.hardware_PWM(self._GPIOPin, _MAX, _MAX)

    def TurnOff(self):
        self._pigpio.hardware_PWM(self._GPIOPin, _MIN, _MIN)

    def SetValue(self, DutyCycle: int, Frequency: int):
        self._pigpio.hardware_PWM(self._GPIOPin, Frequency, DutyCycle)


