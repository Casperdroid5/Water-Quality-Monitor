import time
import pigpio

_MAX: int = 100_0000
_MIN: int = 350_000
_OFF: int = 0
#_FREQUENCY = 100_000
class PWM():

    def __init__(self, pi, GPIOPin: int) -> None:
        self._GPIOPin: int = GPIOPin
        self._pigpio = pi
        self.state = ''

    def TurnOn(self):
         self._pigpio.hardware_PWM(self._GPIOPin, _MAX, _MAX)
         self.state = 'On'
         return self.state

    def TurnOff(self):
        self._pigpio.hardware_PWM(self._GPIOPin, _MIN, _MIN)
        self.state = 'Off'
        return self.state

    def SetValue(self, DutyCycle: int, Frequency: int):
        self._pigpio.hardware_PWM(self._GPIOPin, Frequency, DutyCycle)
        return self.state



if __name__ == "__main__":
    
    
    led1 = PWM(pi = pigpio.pi(), GPIOPin = 12)
    print("On/Off test")
    x = led1.TurnOn()
    print(x)
    time.sleep(1)
    x = led1.TurnOff()
    print(x) 
    time.sleep(1)
    x = led1.TurnOn()
    print(x)
    time.sleep(1)
    x = led1.TurnOff()
    print(x) 
    time.sleep(1)

    print("Sweep test")
    for x in range(_MIN, _MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = led1.SetValue(Frequency = 100_000, DutyCycle = x)

    x = led1.TurnOff()
    print(x)
    print("test complete")
        

    



