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
            self._pigpio.write(self._EnableGPIOPin, constants.ON) #low on enable pin to enable motor
            self.state = State.MOTOR_ENABLED.name
            return self.state
        else: 
            self._pigpio.write(self._EnableGPIOPin, constants.OFF) #high on enable pin to disable motor
            self.state = State.MOTOR_DISABLED.name
            return self.state

    def SetMotorDir(self, DIR: int):
        if DIR == 1:
            self._pigpio.set_PWM_dutycycle(self._DirGPIOPin, constants.MAXPWM) 
            self.state = State.MOTOR_CLOCKWISE.name
            return self.state
        else:
            self._pigpio.set_PWM_dutycycle(self._DirGPIOPin, constants.MINPWM) 
            self.state = State.MOTOR_COUNTERCLOCKWISE.name
            return self.state

    def SetMotorStep(self, STEP: int):
        for x in range(STEP):
            self._pigpio.set_PWM_dutycycle(self._StepGPIOPin, constants.MAXPWM) 
            time.sleep(0.0005)
            self._pigpio.set_PWM_dutycycle(self._StepGPIOPin, constants.MINPWM) 
            time.sleep(0.0005)
            self.state = State.STEP.name
            return self.state


if __name__ == "__main__":
        
    
    StepperMotor1 = STEPPERMOTORS(pi = pigpio.pi(), EnableGPIOPin = 18, DirGPIOPin = 23, StepGPIOPin = 27)
    
    print("Enable/Disable Motor")
    x = StepperMotor1.SetMotorState(1)
    print(x)
    time.sleep(2)
    x = StepperMotor1.SetMotorState(0)
    print(x) 
    time.sleep(2)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = StepperMotor1.SetMotorDir(1)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = StepperMotor1.SetMotorStep(200)
    print(x)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = StepperMotor1.SetMotorDir(0)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = StepperMotor1.SetMotorStep(200)
    print(x)

    x = StepperMotor1.SetMotorState(1)
    print(x) 

    print("test complete")
        