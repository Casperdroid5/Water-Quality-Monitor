import time
import pigpio

_MAX: int = 100_0000
_MIN: int = 0
#_FREQUENCY = 100_000

class PELTIER():
    def __init__(self, pi, GPIOpeltier_in1: int, GPIOpeltier_in2: int) -> None:
        self._GPIOpeltier_in1: int = GPIOpeltier_in1
        self._GPIOpeltier_in2: int = GPIOpeltier_in2
        self._pigpio = pi
        self.state = ''

    def SetToCooling(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MAX, _MAX)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)
        self.state = 'COLD'
        return self.state

    def SetToHeating(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MAX, _MAX)
        self.state = 'HOT'
        return self.state
        
    def TurnOff(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)
        self.state = 'OFF'
        return self.state

    def SetTemperature(self, In1DutyCycle: int, In1Frequency: int, In2DutyCycle: int, In2Frequency: int):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MAX, In1DutyCycle, In1Frequency)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MAX, In2DutyCycle, In2Frequency)
        self.state = 'Custom value: '
        return self.state    



if __name__ == "__main__":
    
    
    Peltier1 = PELTIER(pi = pigpio.pi(), GPIOpeltier_in1 = 12, GPIOpeltier_in2 = 13)
    print("full Cool/Heat test")
    x = Peltier1.SetToCooling()
    print(x)
    time.sleep(3)
    x = Peltier1.SetToHeating()
    print(x) 
    time.sleep(3)
    x = Peltier1.SetTemperature(In1DutyCycle = 75_000, In1Frequency = _MAX, In2DutyCycle = 0, In2Frequency = _MIN) 
    print(x)
    time.sleep(3)
    x = Peltier1.TurnOff()
    print(x) 
    time.sleep(3)

    print("Sweep test HOT")
    for x in range(_MIN, _MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetValue(In1DutyCycle = _MIN, In1Frequency = _MAX, In2DutyCycle = x, In2Frequency = _MAX)

    print("Sweep test COLD") # assuming in2 is the hot side
    for x in range(_MIN, _MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetValue(In1DutyCycle = x, In1Frequency = _MAX, In2DutyCycle = _MIN, In2Frequency = _MAX)

    x = Peltier1.TurnOff()
    print(x)
    print("test complete")
        