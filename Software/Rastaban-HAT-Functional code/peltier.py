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
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, constants.MAX, constants.MAX)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, constants.MIN, constants.MIN)
        self.state = State.COLD.name
        return self.state

    def SetToHeating(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, constants.MIN, constants.MIN)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, constants.MAX, constants.MAX)
        self.state = State.HOT.name
        return self.state
        
    def TurnOff(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, constants.MIN, constants.MIN)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, constants.MIN, constants.MIN)
        self.state = State.OFF.name
        return self.state

    def SetTemperature(self, In1DutyCycle: int, In1Frequency: int, In2DutyCycle: int, In2Frequency: int):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, In1Frequency, In1DutyCycle)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, In2Frequency, In2DutyCycle)
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
    x = Peltier1.SetTemperature(In1DutyCycle = 450_000, In1Frequency = 100_000, In2DutyCycle = constants.MIN, In2Frequency = constants.MIN) 
    print(x)
    
    print("SetTemperature 2 Test")
    time.sleep(1)
    x = Peltier1.SetTemperature(In1DutyCycle = 700_000, In1Frequency = 100_000, In2DutyCycle = constants.MIN, In2Frequency = constants.MIN) 
    print(x)
    
    print("SetTemperature 3 Test")
    time.sleep(1)
    x = Peltier1.SetTemperature(In1DutyCycle = 200_000, In1Frequency = 100_000, In2DutyCycle = constants.MIN, In2Frequency = constants.MIN) 
    print(x)
    
    print("Turn Off Test")
    time.sleep(1)
    x = Peltier1.TurnOff()
    print(x) 
    time.sleep(3)

    print("Sweep test HOT")
    time.sleep(1)
    for x in range(constants.MIN, constants.MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetTemperature(In1DutyCycle = constants.MIN, In1Frequency = constants.MIN, In2DutyCycle = x, In2Frequency = 100_000)

    print("Sweep test COLD") # assuming in2 is the hot side
    for x in range(constants.MIN, constants._MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetTemperature(In1DutyCycle = x, In1Frequency = 100_000, In2DutyCycle = constants.MIN, In2Frequency = constants.MIN)

    x = Peltier1.TurnOff()
    print(x)
    print("test complete")
        