import time
import pigpio
from hardwarepwm import PWM
import constants

class HEATINGRESISTOR(PWM): # Child class from PWM

    def GetState(self):
        print(self.state)


if __name__ == "__main__":
    
    
    HeatingResistor1 = HEATINGRESISTOR(pi = pigpio.pi(), GPIOPin = 12)
    
    HeatingResistor1.GetState()
    time.sleep(3)
    print("On/Off test")
    x = HeatingResistor1.TurnOn()
    print(x)
    time.sleep(1)
    x = HeatingResistor1.TurnOff()
    print(x) 
    time.sleep(1)
    x = HeatingResistor1.TurnOn()
    print(x)
    time.sleep(1)
    x = HeatingResistor1.TurnOff()
    print(x) 
    time.sleep(1)

    print("Sweep test")
    for x in range(constants.MIN, constants.MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = HeatingResistor1.SetValue(Frequency = 100_000, DutyCycle = x)

    x = HeatingResistor1.TurnOff()
    print(x)
    print("test complete")        