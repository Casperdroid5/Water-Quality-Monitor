from ctypes.wintypes import DOUBLE
import time
from tkinter import DoubleVar
import pigpio
from enums import State
import constants


class VOICECOILMOTORS():

    def __init__(self, pi, MOTORnum: int, EnablePin: int, PhasePin: int, SleepPin: int) -> None:
        self._pigpio = pi
        self.MOTORnum: int = MOTORnum 
        self.EnablePin: int = EnablePin
        self.PhasePin: int = PhasePin
        self.SleepPin: int = SleepPin
        self.state = None

    def SetMotorEnable(self, ENABLE: int, Frequency: int): # Enable controls speed
        self._pigpio.hardware_PWM(self._GPIOPin, Frequency, ENABLE)
        return self.state

    def SetMotorPhase(self, PHASE: bool): # Phase controls direction
        if PHASE == 1:
            self._pigpio.harware_PWM(self.MOTORnum, constants.MAX, constants.MAX) 
            self.state = State.PHASE.name
            return self.state
        else:
            self._pigpio.hardware_PWM(self.MOTORnum, constants.OFF, constants.OFF) 
            self.state = State.PHASE.name
            return self.state

    def SetMotorSleep(self, SLEEP: int):
        if SLEEP == 1:
            self._pigpio.hardware_PWM(self.SleepPin, constants.OFF, constants.LOFF)
        else:
            self._pigpio.hardware_PWM(self.MOTORnum, constants.ON, constants.ON) 
            self.state = State.SLEEP.name
            return self.state


if __name__ == "__main__":
        
    
    Motor1 = VOICECOILMOTORS(pi = pigpio.pi(), MOTORnum = 1, EnablePin = 36, PhasePin = 33, SleepPin = 36)
    
    print("Enable/Disable Motor")
    x = Motor1.SetMotorState(SLEEP = True)
    print(x)
    time.sleep(2)
    x = Motor1.SetMotorState(SLEEP = False)
    print(x) 
    time.sleep(2)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = Motor1.SetMotorDir(PHASE = 1)
    print(x)

    print("Set Motor Drive Test")
    time.sleep(1)
    x = Motor1.SetMotorStep(ENABLE = 100_000)
    print(x)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = Motor1.SetMotorDir(PHASE = 0)
    print(x)

    print("Set Motor Drive Test")
    time.sleep(1)
    x = Motor1.SetMotorStep(ENABLE = 100_000)
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
        