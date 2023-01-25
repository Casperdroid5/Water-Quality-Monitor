import time
import pigpio
from pwm import PWM
from enums import State
import constants


class HEATINGRESISTOR(PWM):  # Child class from PWM

    def GetState(self):
        print(self.state)


if __name__ == "__main__":

    HeatingResistor1 = HEATINGRESISTOR(pi=pigpio.pi(), GPIOPin=5)

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
    time.sleep(20)
    x = HeatingResistor1.TurnOff()
    print(x)
    time.sleep(1)

    print("Sweep test")
    for x in range(constants.MINPWM, constants.MAXPWM, 10):  # steps of 100
        time.sleep(0.1)
        print(x)
        x = HeatingResistor1.SetValue(DutyCycle=x)

    x = HeatingResistor1.TurnOff()
    print(x)
    print("test complete")
