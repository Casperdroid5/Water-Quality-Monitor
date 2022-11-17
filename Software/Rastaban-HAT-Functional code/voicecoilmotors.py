import time
import pigpio
from enums import State
import constants


class VOICECOILMOTORS():

    def __init__(self, pi, EnableGPIOPin: int, PhaseGPIOPin: int, SleepGPIOPin: int) -> None:
        self._pigpio = pi
        self._EnableGPIOPin: int = EnableGPIOPin
        self._PhaseGPIOPin: int = PhaseGPIOPin
        self._SleepGPIOPin: int = SleepGPIOPin
        self.state = None

    def SetMotorEnable(self, ENABLE: int): # Enable controls speed
        self._pigpio.set_PWM_dutycycle(self._EnableGPIOPin, ENABLE)

    def SetMotorPhase(self, PHASE: int): # Phase controls direction
        if PHASE == 1:
            self._pigpio.write(self._PhaseGPIOPin, constants.ON) 
            self.state = State.PHASE.name
            return self.state
        else:
            self._pigpio.write(self._PhaseGPIOPin, constants.OFF) 
            self.state = State.PHASE.name
            return self.state

    def SetMotorSleep(self, SLEEP: int):
        if SLEEP == 1:
            self._pigpio.write(self._SleepGPIOPin, constants.OFF)
            self.state = State.SLEEP.name
        else:
            self._pigpio.write(self._SleepGPIOPin, constants.ON) 
            self.state = State.SLEEP.name
            return self.state


if __name__ == "__main__":
        

    Motor1 = VOICECOILMOTORS(pi = pigpio.pi(), EnableGPIOPin = 12, PhaseGPIOPin = 13, SleepGPIOPin = 4)
    
    print("Enable/Disable Motor")
    time.sleep(1)
    x = Motor1.SetMotorSleep(constants.OFF) # off and on constants are reversed for the drv8838
    print(x)
    time.sleep(2)
    x = Motor1.SetMotorSleep(constants.ON)
    print(x) 
    time.sleep(1)
    
    print("Set Motor Direction Test")
    time.sleep(1)
    x = Motor1.SetMotorPhase(1)
    print(x)

    print("Set Motor Drive Test")
    time.sleep(1)
    x = Motor1.SetMotorEnable(255)
    print(x)
    
    print("Set Motor Direction Test")
    time.sleep(3)
    x = Motor1.SetMotorPhase(0)
    print(x)

    print("Set Motor Drive Test")
    time.sleep(1)
    x = Motor1.SetMotorEnable(255)
    print(x)

    print("Sweep test")
    for x in range(constants.MINPWM, constants.MAXPWM, 5): # steps of 5
        time.sleep(0.1)
        print(x)
        Motor1.SetMotorEnable(x)

    time.sleep(1)
    x = Motor1.SetMotorSleep(constants.ON)
    print(x) 

    print("test complete")
        