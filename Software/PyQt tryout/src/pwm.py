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
         self._pigpio.hardware_PWM(self._GPIOPin, constants.MAX, constants.MAX)
         self.state = State.ON.name # was State.ON
         return self.state

    def TurnOff(self):
        self._pigpio.hardware_PWM(self._GPIOPin, constants.MIN, constants.MIN)
        self.state = State.OFF.name
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
    for x in range(constants.MIN, constants.MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = led1.SetValue(Frequency = 100_000, DutyCycle = x)

    x = led1.TurnOff()
    print(x)
    print("test complete")
        

    



