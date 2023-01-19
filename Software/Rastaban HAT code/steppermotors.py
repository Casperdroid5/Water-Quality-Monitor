import time
import pigpio
from enums import State
import constants

"""
This code is used to control the TMC2209 stepper motors using step, dir and enable pins. This is the "legacy" way to control stepper motors. 
However, it is nowadays more common to control stepper motors via UART (sometimes in combination with step/dir/en), 
since this gives the user more control over the stepper motors and enables extra features. 
This code can not be used by PCB V0.3 (Only UART).
"""

class STEPPERMOTORS():

    def __init__(self, pi, EnableGPIOPin: int, DirGPIOPin: int, StepGPIOPin: int) -> None: 
        self._pigpio = pi
        self._EnableGPIOPin: int = EnableGPIOPin
        self._DirGPIOPin: int = DirGPIOPin
        self._StepGPIOPin: int = StepGPIOPin
        self.state = None

    def SetMotorState(self, ENABLE: int): 
        if ENABLE == 1:
            self._pigpio.write(self._EnableGPIOPin, constants.OFF) #low on enable pin to enable motordriver, tmc 2209
            self.state = State.MOTOR_ENABLED.name
            return self.state
        else: 
            self._pigpio.write(self._EnableGPIOPin, constants.ON) #high on enable pin to disable motordriver, tmc 2209
            self.state = State.MOTOR_DISABLED.name
            return self.state

    def SetMotorDir(self, DIR: int):
        if DIR == 1:
            self._pigpio.write(self._DirGPIOPin, constants.ON) 
            self.state = State.MOTOR_CLOCKWISE.name
            return self.state
        else:
            self._pigpio.write(self._DirGPIOPin, constants.OFF) 
            self.state = State.MOTOR_COUNTERCLOCKWISE.name
            return self.state

    def SetMotorStep(self, STEP: int):
        for x in range(STEP):
            self._pigpio.write(self._StepGPIOPin, constants.ON) 
            time.sleep(0.00005)
            self._pigpio.write(self._StepGPIOPin, constants.OFF) 
            time.sleep(0.00005)
            print(x)
        


if __name__ == "__main__":
        
    
    PrimaryStepper = STEPPERMOTORS(pi = pigpio.pi(), EnableGPIOPin = 21, DirGPIOPin = 23, StepGPIOPin = 27)
    SecondaryStepper = STEPPERMOTORS(pi = pigpio.pi(), EnableGPIOPin = 20, DirGPIOPin = 22, StepGPIOPin = 24)
    FocusStepper = STEPPERMOTORS(pi = pigpio.pi(), EnableGPIOPin = 16, DirGPIOPin = 26, StepGPIOPin = 19)

    print("Enable/Disable Motor")
    x = PrimaryStepper.SetMotorState(constants.OFF)
    print(x)
    time.sleep(1)
    x = PrimaryStepper.SetMotorState(constants.ON)
    print(x) 
    time.sleep(1)

    print("Enable/Disable Motor")
    x = SecondaryStepper.SetMotorState(constants.OFF)
    print(x)
    time.sleep(1)
    x = SecondaryStepper.SetMotorState(constants.ON)
    print(x) 
    time.sleep(1)

    print("Set Motor Direction Test")
    time.sleep(1)
    x = PrimaryStepper.SetMotorDir(1)
    print(x)

    print("Set Motor Direction Test")
    time.sleep(1)
    x = SecondaryStepper.SetMotorDir(1)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = SecondaryStepper.SetMotorStep(6400)
    print(x) 

    print("Set Motor Step Test")
    time.sleep(1)
    x = PrimaryStepper.SetMotorStep(6400)
    print(x)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = PrimaryStepper.SetMotorDir(0)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = PrimaryStepper.SetMotorStep(6400) #one rotation is 3200 pulses by microstepping 8. motor has 400 steps by full stepping
    print(x)

    print("Set Motor Direction Test")
    time.sleep(1)
    x = SecondaryStepper.SetMotorDir(0)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = SecondaryStepper.SetMotorStep(6400) #one rotation is 3200 pulses by microstepping 8. motor has 400 steps by full stepping
    print(x)

    x = PrimaryStepper.SetMotorState(State.OFF)
    print(x) 

    x = SecondaryStepper.SetMotorState(constants.OFF)
    print(x) 
    time.sleep(1)

    print("test complete")
        