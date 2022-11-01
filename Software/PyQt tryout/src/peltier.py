
_MAX: int = 100
_MIN: int = 0
#_FREQUENCY = 100_000

class PELTIER():
    def __init__(self, pi, GPIOpeltier_in1: int, GPIOpeltier_in2: int) -> None:
        self._GPIOpeltier_in1: int = GPIOpeltier_in1
        self._GPIOpeltier_in2: int = GPIOpeltier_in2
        self._pigpio = pi

    def SetToCooling(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MAX, _MAX)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)

    def SetToHeating(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MAX, _MAX)
        
    def TurnOff(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)

    def SetTemperature(self, DutyCycle: int, Frequency: int):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MAX, DutyCycle, Frequency)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MAX, DutyCycle, Frequency)    

