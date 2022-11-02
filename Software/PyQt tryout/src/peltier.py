import time
import pigpio
from enums import State
import constants

class PELTIER():
    
    def __init__(self, pi, GPIOpeltier_in1: int, GPIOpeltier_in2: int) -> None:
        self._GPIOpeltier_in1: int = GPIOpeltier_in1
        self._GPIOpeltier_in2: int = GPIOpeltier_in2
        self._pigpio = pi
        self.state = None

    def SetToCooling(self):
        self._pigpio.set_PWM_dutycycle(self._GPIOpeltier_in1, constants.MAXPWM)
        self._pigpio.set_PWM_dutycycle(self._GPIOpeltier_in2, constants.MINPWM)
        self.state = State.COLD.name
        return self.state

    def SetToHeating(self):
        self._pigpio.set_PWM_dutycycle(self._GPIOpeltier_in1, constants.MINPWM)
        self._pigpio.set_PWM_dutycycle(self._GPIOpeltier_in2, constants.MAXPWM)
        self.state = State.HOT.name
        return self.state
        
    def TurnOff(self):
        self._pigpio.set_PWM_dutycycle(self._GPIOpeltier_in1, constants.MINPWM)
        self._pigpio.set_PWM_dutycycle(self._GPIOpeltier_in2, constants.MINPWM)
        self.state = State.OFF.name
        return self.state

    def SetTemperature(self, In1DutyCycle: int, In2DutyCycle: int,):
        self._pigpio.set_PWM_dutycycle(self._GPIOpeltier_in1, In1DutyCycle)
        self._pigpio.set_PWM_dutycycle(self._GPIOpeltier_in2, In2DutyCycle)
        self.state = State.CUSTOM.name
        return self.state    



if __name__ == "__main__":
    
    
    Peltier1 = PELTIER(pi = pigpio.pi(), GPIOpeltier_in1 = 13, GPIOpeltier_in2 = 12)
    
    print("full Cool/Heat test")
    x = Peltier1.SetToCooling()
    print(x)
    time.sleep(2)
    x = Peltier1.SetToHeating()
    print(x) 
    time.sleep(2)
    
    print("SetTemperature 1 Test")
    time.sleep(1)
    x = Peltier1.SetTemperature(In1DutyCycle = 150, In2DutyCycle = constants.MINPWM) 
    print(x)
    
    print("SetTemperature 2 Test")
    time.sleep(1)
    x = Peltier1.SetTemperature(In1DutyCycle = 255, In2DutyCycle = constants.MINPWM) 
    print(x)
    
    print("SetTemperature 3 Test")
    time.sleep(1)
    x = Peltier1.SetTemperature(In1DutyCycle = 50, In2DutyCycle = constants.MINPWM) 
    print(x)
    
    print("Turn Off Test")
    time.sleep(1)
    x = Peltier1.TurnOff()
    print(x) 
    time.sleep(3)

    print("Sweep test HOT")
    time.sleep(1)
    for x in range(constants.MINPWM, constants.MAXPWM, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetTemperature(In1DutyCycle = constants.MINPWM, In2DutyCycle = x)

    print("Sweep test COLD") # assuMINPWMg in2 is the hot side
    for x in range(constants.MINPWM, constants.MAXPWM, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetTemperature(In1DutyCycle = x, In2DutyCycle = constants.MINPWM)

    x = Peltier1.TurnOff()
    print(x)
    print("test complete")
        