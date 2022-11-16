import time
import pigpio
from enums import State
import constants


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
        
    
    StepperMotor1 = STEPPERMOTORS(pi = pigpio.pi(), EnableGPIOPin = 40, DirGPIOPin = 16, StepGPIOPin = 13)
    
    print("Enable/Disable Motor")
    x = StepperMotor1.SetMotorState(constants.OFF)
    print(x)
    time.sleep(1)
    x = StepperMotor1.SetMotorState(constants.ON)
    print(x) 
    time.sleep(1)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = StepperMotor1.SetMotorDir(1)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = StepperMotor1.SetMotorStep(6400)
    print(x)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = StepperMotor1.SetMotorDir(0)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = StepperMotor1.SetMotorStep(6400) #one rotation is 3200 pulses by microstepping 8. motor has 400 steps by full stepping
    print(x)

    x = StepperMotor1.SetMotorState(State.OFF)
    print(x) 

    print("test complete")
        