import time
import pigpio
from enums import State
from hardwarepwm import HARDWAREPWM
import constants

class MICROSCOPELED(HARDWAREPWM): # Child class from PWM

    def GetState(self):
        print(self.state)


if __name__ == "__main__":
    
    
    MicrosScopeLed1 = MICROSCOPELED(pi = pigpio.pi(), GPIOPin = 18)
    print("On/Off test")
    x = MicrosScopeLed1.TurnOn()
    print(x)
    time.sleep(1)
    x = MicrosScopeLed1.TurnOff()
    print(x) 
    time.sleep(1)
    x = MicrosScopeLed1.TurnOn()
    print(x)
    time.sleep(1)
    x = MicrosScopeLed1.TurnOff()
    print(x) 
    time.sleep(1)

    print("Sweep test")
    for x in range(constants.OFF, constants.MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = MicrosScopeLed1.SetValue(Frequency = 100_000, DutyCycle = x)

    x = MicrosScopeLed1.TurnOff()
    print(x)
    print("test complete")
        

    



