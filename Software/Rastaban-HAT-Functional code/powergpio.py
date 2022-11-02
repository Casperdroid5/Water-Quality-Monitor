import time
import pigpio
from pwm import PWM
import constants
class POWERGPIO(PWM): # Child class from PWM

    def GetState(self):
        print(self.state)


if __name__ == "__main__":
    
    
    
    powergpio1 = POWERGPIO(pi = pigpio.pi(), GPIOPin = 12)
    
    powergpio1.GetState()
    time.sleep(3)
    print("On/Off test")
    x = powergpio1.TurnOn()
    print(x)
    time.sleep(1)
    x = powergpio1.TurnOff()
    print(x) 
    time.sleep(1)
    x = powergpio1.TurnOn()
    print(x)
    time.sleep(1)
    x = powergpio1.TurnOff()
    print(x) 
    time.sleep(1)

    print("Sweep test")
    for x in range(constants._MIN, constants._MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = powergpio1.SetValue(Frequency = 100_000, DutyCycle = x)

    x = powergpio1.TurnOff()
    print(x)
    print("test complete")        