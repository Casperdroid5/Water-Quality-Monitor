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

    def SetTemperature(self, DutyCycle: int, Frequency: int):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MAX, DutyCycle, Frequency)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MAX, DutyCycle, Frequency)
        self.state = 'Custom value: '
        return self.state    



if __name__ == "__main__":
    
    
    Peltier1 = PELTIER(pi = pigpio.pi(), GPIOPin = 12)
    print("full Cool/Heat test")
    x = Peltier1.SetToCooling()
    print(x)
    time.sleep(3)
    x = Peltier1.SetToHeating()
    print(x) 
    time.sleep(3)
    x = Peltier1.SetTemperature(DutyCycle= 25_000, Frequency=100_000)
    print(x)
    time.sleep(3)
    x = Peltier1.TurnOff()
    print(x) 
    time.sleep(3)

    print("Sweep test HOT")
    for x in range(_LOWEST_VALUE, _HIGHEST_VALUE, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetValue(Frequency = 100000, DutyCycle = x)

    print("Sweep test COLD")
    for x in range(_LOWEST_VALUE, _HIGHEST_VALUE, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetValue(Frequency = 100000, DutyCycle = x)

    x = Peltier1.TurnOff()
    print(x)
    print("test complete")
        