from ctypes.wintypes import BOOL
from turtle import delay
from xmlrpc.client import Boolean
import pigpio


_MAX: int = 100
_MIN: int = 0
_FREQUENCY = 100_000
pi = pigpio.pi()
Microscope_Led_Pin = 12

class PWM():
    def __init__(self, GPIOPin: int) -> None:
        self._GPIOPin: int = GPIOPin

    def turn_fully_on(self):
         pi.hardware_PWM(self._GPIOPin, _MAX, _MAX)

    def turn_off(self):
        pi.hardware_PWM(self._GPIOPin, _MIN, _MIN)

    def set_value(self, DutyCycle: int, Frequency: int):
        pi.hardware_PWM(self._GPIOPin, Frequency, DutyCycle)



pwm_example = PWM(GPIOPin=10, DutyCycle=20, Frequency=30)
pwm_example.set_value(DutyCycle=30, Frequency=50)




print(MicroscopeLED.GPIOPin)
MicroscopeLED.GPIOPin = 25


MicroscopeLED.turn_fully_on()
delay(100)
MicroscopeLED.turn_off() 
MicroscopeLED.set_value(MicroscopeLED, 10000, 34000)

peltier = Peltier()
peltier.heatingon



#class peripheral():
#    MicroscopeLED()
#    Peltier()
#   Motor()

class Peltier():
    def __init__(self, GPIOpeltier_in2: int, GPIOpeltier_in1: int, IN1_val: int, IN2_val: int) -> None:
        self._GPIOpeltier_in1: int = GPIOpeltier_in1
        self._GPIOpeltier_in2: int = GPIOpeltier_in2
        self._gpio_pin3: int = IN1_val
        self._gpio_pin4: int = IN2_val

    def SetToCooling(self):
        pi.hardware_PWM(self._GPIOpeltier_in1, _MAX, _MAX)
        pi.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)

    def SetToHeating(self):
        pi.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        pi.hardware_PWM(self._GPIOpeltier_in2, _MAX, _MAX)
        
    def turn_off(self):
        pi.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        pi.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)

    def SetTemperature(self, DutyCycle: int):
        pi.hardware_PWM(self._GPIOpeltier_in1, _MAX, DutyCycle)
        pi.hardware_PWM(self._GPIOpeltier_in2, _MAX, DutyCycle)    

class PowerGPIO():
    def __init__(self, POWERGPIOpin: int) -> None:
        self._PWM = PWM(PowerGPIOpin)
    
    def turn_fully_on(self):
         pi.hardware_PWM(self._POWERGPIOpin, _MAX, _MAX)

    def turn_off(self):
        pi.hardware_PWM(self._POWERGPIOpin, _MIN, _MIN)

    def change(self, duty_cycle: int):
         pi.hardware_PWM(self._POWERGPIOpin, _FREQUENCY, duty_cycle)

class Motors():
    def __init__(self, MOTORnum: int, DIR, STEP, EN, PHASE, SLEEP) -> None:
        self._gpio_pin: int = MOTORnum 
        self._gpio_pin: int = DIR
        self._gpio_pin: int = STEP
        self._gpio_pin: int = EN
        self._gpio_pin: int = PHASE
        self._gpio_pin: int = SLEEP

    def set_motor_power(self, enabled: bool): 
        if enabled == True:
            pi.hardware_PWM(self.MOTORnum, _MAX, _MAX)
        else: 
            pi.hardware_PWM(self.MOTORnum, _MIN, _MIN)

    def set_motor_dir(self, DIR: bool):
        if DIR == 1:
            pi.harware_PWM(self.MOTORnum, _MAX, _MAX) #high on enable pin to enable motor
        else:
            pi.hardware_PWM(self.MOTORnum, _MIN, _MIN) #low on enable pin to enable motor

    def set_motor_step(self, STEP: float):
        for x in range(STEP):
            pi.harware_PWM(self.STEPPIN, _MAX, _MAX) 
            delay(0.001)
            pi.harware_PWM(self.STEPPIN, _MIN, _MIN) 
            delay(0.001)
            STEP + 1
