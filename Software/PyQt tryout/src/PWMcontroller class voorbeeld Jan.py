from ctypes.wintypes import BOOL
from turtle import delay
from xmlrpc.client import Boolean
import pigpio


_MAX: int = 100
_MIN: int = 0
_FREQUENCY = 100_000
pi = pigpio.pi()

class PWM():
    def __init__(self, gpio_pin: int) -> None:
        self._gpio_pin: int = gpio_pin

    def turn_fully_on(self):
         pi.hardware_PWM(self._gpio_pin, _MAX, _MAX)

    def turn_off(self):
        pi.hardware_PWM(self._gpio_pin, _MIN, _MIN)

    def change(self, duty_cycle: int):
         pi.hardware_PWM(self._gpio_pin, _FREQUENCY, duty_cycle)

class MicroscopeLED():
    def __init__(self, gpio_pin: int) -> None:
        self._gpio_pin: int = gpio_pin

    def turn_fully_on(self):
         pi.hardware_PWM(self._gpio_pin, _MAX, _MAX)

    def turn_off(self):
        pi.hardware_PWM(self._gpio_pin, _MIN, _MIN)

    def change(self, duty_cycle: int):
         pi.hardware_PWM(self._gpio_pin, _FREQUENCY, duty_cycle)


class Peltier():
    def __init__(self, GPIOpeltier_in2: int, GPIOpeltier_in1: int) -> None:
        self._gpio_pin: int = GPIOpeltier_in1
        self._gpio_pin: int = GPIOpeltier_in2
    
    def turn_cooler_fully_on(self):
        pi.hardware_PWM(self._GPIOpeltier_in1, _MAX, _MAX)
        pi.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)

    def turn_heater_fully_on(self):
        pi.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        pi.hardware_PWM(self._GPIOpeltier_in2, _MAX, _MAX)
        
    def turn_off(self):
        pi.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        pi.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)

    def Change_Temperature(self, DutyCycle: int):
        pi.hardware_PWM(self._GPIOpeltier_in1, _MAX, DutyCycle)
        pi.hardware_PWM(self._GPIOpeltier_in2, _MAX, DutyCycle)    

class PowerGPIO():
    def __init__(self, POWERGPIOpin: int) -> None:
        self._gpio_pin: int = POWERGPIOpin
    
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
