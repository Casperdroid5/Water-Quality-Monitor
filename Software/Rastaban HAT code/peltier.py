import time
import pigpio
from enums import State
import constants

"""
This code is used to control the peltier module.
"""


class PELTIER():

    def __init__(self, pi, GPIOPin_in1: int, GPIOPin_in2: int) -> None:
        self._GPIOPin_in1: int = GPIOPin_in1
        self._GPIOPin_in2: int = GPIOPin_in2
        self._pigpio = pi
        self.state = None

    def SetToCooling(self):
        self._pigpio.set_PWM_dutycycle(self._GPIOPin_in1, constants.MAXPWM)
        self._pigpio.set_PWM_dutycycle(self._GPIOPin_in2, constants.MINPWM)
        self.state = State.COLD.name
        return self.state

    def SetToHeating(self):
        self._pigpio.set_PWM_dutycycle(self._GPIOPin_in1, constants.MINPWM)
        self._pigpio.set_PWM_dutycycle(self._GPIOPin_in2, constants.MAXPWM)
        self.state = State.HOT.name
        return self.state

    def TurnOff(self):
        self._pigpio.set_PWM_dutycycle(self._GPIOPin_in1, constants.MINPWM)
        self._pigpio.set_PWM_dutycycle(self._GPIOPin_in2, constants.MINPWM)
        self.state = State.OFF.name
        return self.state

    def SetTemperature(self, In1DutyCycle: int, In2DutyCycle: int,):
        self._pigpio.set_PWM_dutycycle(self._GPIOPin_in1, In1DutyCycle)
        self._pigpio.set_PWM_dutycycle(self._GPIOPin_in2, In2DutyCycle)
        self.state = State.CUSTOM.name
        return self.state


if __name__ == "__main__":

    Peltier1 = PELTIER(pi=pigpio.pi(), GPIOPin_in1=8, GPIOPin_in2=7)

    print("full Cool/Heat test")
<< << << < HEAD: Software/Rastaban HAT Functional code/peltier.py
x = Peltier1.SetToCooling()
 print(x)
  time.sleep(15)
   x = Peltier1.SetToHeating()
    print(x)
    time.sleep(15)

    print("SetTemperature 1 Test")
    time.sleep(5)
    x = Peltier1.SetTemperature(
        In1DutyCycle=100, In2DutyCycle=constants.MINPWM)
    print(x)

    print("SetTemperature 2 Test")
    time.sleep(5)
    x = Peltier1.SetTemperature(
        In1DutyCycle=255, In2DutyCycle=constants.MINPWM)
    print(x)

    print("SetTemperature 3 Test")
    time.sleep(5)
    x = Peltier1.SetTemperature(In1DutyCycle=50, In2DutyCycle=constants.MINPWM)
    print(x)

    print("Turn Off Test")
    time.sleep(3)
    x = Peltier1.TurnOff()
    print(x)
== == == =
PeltierA = Peltier1.SetToCooling()
 print(PeltierA)
  time.sleep(2)
   PeltierA = Peltier1.SetToHeating()
    print(PeltierA)
    time.sleep(2)

    print("SetTemperature 1 Test")
    time.sleep(2)
    PeltierA = Peltier1.SetTemperature(
        In1DutyCycle=150, In2DutyCycle=constants.MINPWM)
    print(PeltierA)

    print("SetTemperature 2 Test")
    time.sleep(2)
    PeltierA = Peltier1.SetTemperature(
        In1DutyCycle=255, In2DutyCycle=constants.MINPWM)
    print(PeltierA)

    print("SetTemperature 3 Test")
    time.sleep(1)
    PeltierA = Peltier1.SetTemperature(
        In1DutyCycle=50, In2DutyCycle=constants.MINPWM)
    print(PeltierA)

    print("Turn Off Test")
    time.sleep(1)
    PeltierA = Peltier1.TurnOff()
    print(PeltierA)
>>>>>> > 0fdb98cbe629a3ce098ce77a5fc4393709866c9b: Software/Rastaban HAT code/peltier.py
time.sleep(3)

 print("Sweep test HOT")
  time.sleep(1)
   for PeltierA in range(constants.MINPWM, constants.MAXPWM, 100):  # steps of 100
        # time.sleep(0.1)
        print(PeltierA)
        PeltierA = Peltier1.SetTemperature(
            In1DutyCycle=constants.MINPWM, In2DutyCycle=PeltierA)

    print("Sweep test COLD")  # assuMINPWMg in2 is the hot side
    for PeltierA in range(constants.MINPWM, constants.MAXPWM, 100):  # steps of 100
        # time.sleep(0.1)
        print(PeltierA)
        PeltierA = Peltier1.SetTemperature(In1DutyCycle=PeltierA, In2DutyCycle=constants.MINPWM)

    PeltierA = Peltier1.TurnOff()
    print(PeltierA)
    print("test complete")
