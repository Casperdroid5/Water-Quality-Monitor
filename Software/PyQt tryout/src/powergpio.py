_MAX: int = 100
_MIN: int = 0
#_FREQUENCY = 100_000

class PowerGPIO():
    def __init__(self, pi, POWERGPIOpin: int) -> None:
        self._powergpiopin: int = POWERGPIOpin
        self._pigpio = pi
    
    def TurnOn(self):
         self._pigpio.hardware_PWM(self._POWERGPIOpin, _MAX, _MAX)

    def TurnOff(self):
        self._pigpio.hardware_PWM(self._POWERGPIOpin, _MIN, _MIN)

    def SetValue(self, DutyCycle: int, Frequency: int):
        self._pigpio.hardware_PWM(self._POWERGPIOpin, Frequency, DutyCycle)