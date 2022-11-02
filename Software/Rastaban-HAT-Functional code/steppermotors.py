from ctypes.wintypes import DOUBLE
import time
from tkinter import DoubleVar
import pigpio
from enums import State
import constants


class STEPPERMOTORS():

    def __init__(self, pi, MOTORnum: int, DirPin: int, StepPin: int, EnablePin: int) -> None:
        self._pigpio = pi
        self.MOTORnum: int = MOTORnum 
        self.DirPin: int = DirPin
        self.StepPin: int = StepPin
        self.EnablePin: int = EnablePin
        self.state = None

    def SetMotorState(self, ENABLE: int): 
        if ENABLE == 1:
            self._pigpio.set_PWM_dutycycle(self.MOTORnum, constants.MAX) #high on enable pin to enable motor
            self.state = State.MOTOR_ENABLED.name
            return self.state
        else: 
            self._pigpio.set_PWM_dutycycle(self.MOTORnum, constants.OFF)
            self.state = State.MOTOR_DISABLED.name
            return self.state

    def SetMotorDir(self, DIR: int):
        if DIR == 1:
            self._pigpio.harware_PWM(self.MOTORnum, constants.MAX) 
            self.state = State.CLOCKWISE.name
            return self.state
        else:
            self._pigpio.set_PWM_dutycycle(self.MOTORnum, constants.OFF) 
            self.state = State.MOTOR_COUNTERCLOCKWISE.name
            return self.state

    def SetMotorStep(self, STEP: int):
        for x in range(STEP):
            self._pigpio.harware_PWM(self.STEPPIN, constants.MAX) 
            time.sleep(0.001)
            self._pigpio.harware_PWM(self.STEPPIN, constants.OFF) 
            time.sleep(0.001)
            STEP + 1
            self.state = State.STEP.name
            return self.state


if __name__ == "__main__":
        
    
    Motor1 = STEPPERMOTORS(pi = pigpio.pi(), MOTORnum = 1, DirPin = 16, StepPin = 13, EnablePin = 40)
    
    print("Enable/Disable Motor")
    x = Motor1.SetMotorState(ENABLE = 1)
    print(x)
    time.sleep(2)
    x = Motor1.SetMotorState(ENABLE = 0)
    print(x) 
    time.sleep(2)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = Motor1.SetMotorDir(DIR = 1)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = Motor1.SetMotorStep(STEP = 200)
    print(x)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = Motor1.SetMotorDir(DIR = 0)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = Motor1.SetMotorStep(STEP = 200)
    print(x)

    # print("Sweep test HOT")
    # time.sleep(1)
    # for x in range(constants.MIN, constants.MAX, 100): # steps of 100
    #     #time.sleep(0.1)
    #     print(x)
    #     x = Motor1.SetTemperature(In1DutyCycle = constants.MIN, In1Frequency = constants.MIN, In2DutyCycle = x, In2Frequency = 100_000)

    # print("Sweep test COLD") # assuming in2 is the hot side
    # for x in range(constants.MIN, constants._MAX, 100): # steps of 100
    #     #time.sleep(0.1)
    #     print(x)
    #     x = Motor1.SetTemperature(In1DutyCycle = x, In1Frequency = 100_000, In2DutyCycle = constants.MIN, In2Frequency = constants.MIN)

    print("test complete")
        