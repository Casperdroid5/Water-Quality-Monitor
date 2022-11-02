import time
import pigpio
from pwm import PWM
import constants

class Fan(PWM): # Child class from PWM

    def GetState(self):
        print(self.state)


if __name__ == "__main__":
    
    
    Fan1 = Fan(pi = pigpio.pi(), GPIOPin = 31)
    
    Fan1.GetState()
    time.sleep(3)
    print("On/Off test")
    x = Fan1.TurnOn()
    print(x)
    time.sleep(1)
    x = Fan1.TurnOff()
    print(x) 
    time.sleep(1)
    x = Fan1.TurnOn()
    print(x)
    time.sleep(1)
    x = Fan1.TurnOff()
    print(x) 
    time.sleep(1)

    print("Sweep test")
    for x in range(constants.MIN, constants.MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Fan1.SetValue(Frequency = 100_000, DutyCycle = x)

    x = Fan1.TurnOff()
    print(x)
    print("test complete")        