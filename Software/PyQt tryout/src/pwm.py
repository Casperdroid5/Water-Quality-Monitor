import pigpio

_MAX: int = 100
_MIN: int = 0
#_FREQUENCY = 100_000

class PWM():

    def __init__(self, pi, GPIOPin: int) -> None:
        self._GPIOPin: int = GPIOPin
        self._pigpio = pi
        self.state = 0

    def TurnOn(self):
         self._pigpio.hardware_PWM(self._GPIOPin, _MAX, _MAX)
         self.state = 1
         return self.state

    def TurnOff(self):
        self._pigpio.hardware_PWM(self._GPIOPin, _MIN, _MIN)
        self.state = 0
        return self.state

    def SetValue(self, DutyCycle: int, Frequency: int):
        self._pigpio.hardware_PWM(self._GPIOPin, Frequency, DutyCycle)
        return self.state



if __name__ == "__main__":
    
    
    led1 = PWM(pi = pigpio.pi(), GPIOPin = 12)
    x = led1.Turnon()
    print(x)
    x = led1.Turnoff()
    print(x)
    x = led1.SetValue(Frequency=10000, DutyCycle= 12500)
    





