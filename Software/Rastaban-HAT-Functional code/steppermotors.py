import time
import pigpio
from enums import State
import constants


class STEPPERMOTORS():

    def __init__(self, pi, StatePin: int, DirPin: int, StepPin: int, EnablePin: int) -> None:
        self._StatePin: int = StatePin
        self._pigpio = pi
        self._DirPin: int = DirPin
        self._StepPin: int = StepPin
        self._EnablePin: int = EnablePin
        self.state = None

    def SetMotorState(self, ENABLE: int): 
        if ENABLE == 1:
            self._pigpio.set_PWM_dutycycle(self._StatePin, constants.MAXPWM) #high on enable pin to enable motor
            self.state = State.MOTOR_ENABLED.name
            return self.state
        else: 
            self._pigpio.set_PWM_dutycycle(self._StatePin, constants.OFF)
            self.state = State.MOTOR_DISABLED.name
            return self.state

    def SetMotorDir(self, DIR: int):
        if DIR == 1:
            self._pigpio.set_PWM_dutycycle(self._DirPin, constants.MAXPWM) 
            self.state = State.MOTOR_CLOCKWISE.name
            return self.state
        else:
            self._pigpio.set_PWM_dutycycle(self._DirPin, constants.OFF) 
            self.state = State.MOTOR_COUNTERCLOCKWISE.name
            return self.state

    def SetMotorStep(self, STEP: int):
        for x in range(STEP):
            self._pigpio.set_PWM_dutycycle(self._StepPin, constants.MAXPWM) 
            time.sleep(0.001)
            self._pigpio.set_PWM_dutycycle(self._StepPin, constants.OFF) 
            time.sleep(0.001)
            STEP + 1
            self.state = State.STEP.name
            return self.state


if __name__ == "__main__":
        
    
    Motor1 = STEPPERMOTORS(pi = pigpio.pi(), StatePin = 12, DirPin = 16, StepPin = 13, EnablePin = 40)
    
    print("Enable/Disable Motor")
    x = Motor1.SetMotorState(1)
    print(x)
    time.sleep(2)
    x = Motor1.SetMotorState(0)
    print(x) 
    time.sleep(1)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = Motor1.SetMotorDir(1)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = Motor1.SetMotorStep(200)
    print(x)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = Motor1.SetMotorDir(0)
    print(x)

    print("Set Motor Step Test")
    time.sleep(1)
    x = Motor1.SetMotorStep(200)
    print(x)

    print("test complete")
        