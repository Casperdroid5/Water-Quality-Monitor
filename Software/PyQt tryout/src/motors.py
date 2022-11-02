from ctypes.wintypes import DOUBLE
import time
from tkinter import DoubleVar
import pigpio
from enums import State
import constants


class MOTORS():

    def __init__(self, pi, MOTORnum: int, DIR: int, EN: int) -> None:
        self._pigpio = pi
        self._gpio_MOTORnum: int = MOTORnum 
        self._gpio_DIR: int = DIR
        #self._gpio_STEP: int = STEP
        self._gpio_EN: int = EN
        #self._gpio_PHASE: int = PHASE
        #self._gpio_SLEEP: int = SLEEP
        self.state = None

    def SetMotorState(self, ENABLE: bool): 
        if ENABLE == True:
            self._pigpio.hardware_PWM(self.MOTORnum, constants.MAX, constants.MAX) #high on enable pin to enable motor
            self.state = State.MOTOR_ENABLED.name
            return self.state
        else: 
            self._pigpio.hardware_PWM(self.MOTORnum, constants.OFF, constants.OFF)
            self.state = State.MOTOR_DISABLED.name
            return self.state

    def SetMotorDir(self, DIR: bool):
        if DIR == 1:
            self._pigpio.harware_PWM(self.MOTORnum, constants.MAX, constants.MAX) 
            self.state = State.CLOCKWISE.name
            return self.state
        else:
            self._pigpio.hardware_PWM(self.MOTORnum, constants.OFF, constants.OFF) 
            self.state = State.MOTOR_COUNTERCLOCKWISE.name
            return self.state

    def SetMotorStep(self, STEP: int):
        for x in range(STEP):
            self._pigpio.harware_PWM(self.STEPPIN, constants.MAX, constants.MAX) 
            time.sleep(0.001)
            self._pigpio.harware_PWM(self.STEPPIN, constants.OFF, constants.OFF) 
            time.sleep(0.001)
            STEP + 1
            self.state = State.STEP.name
            return self.state


if __name__ == "__main__":
        
    
    Motor1 = MOTORS(pi = pigpio.pi(), GPIOpeltier_in1 = 13, GPIOpeltier_in2 = 12)
    
    print("Enable/Disable Motor")
    x = Motor1.SetMotorState(ENABLE = True)
    print(x)
    time.sleep(2)
    x = Motor1.SetMotorState(ENABLE = False)
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
        