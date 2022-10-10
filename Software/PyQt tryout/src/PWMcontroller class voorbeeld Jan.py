import pigpio

_MAX: int = 100
_MIN: int = 0
_FREQUENCY = 100_000
pi = pigpio.pi()

class PWMController():
    def __init__(self, gpio_pin: int) -> None:
        self._gpio_pin: int = gpio_pin

    def turn_fully_on(self):
         pi.hardware_PWM(self._gpio_pin, _MAX, _MAX)

    def turn_off(self):
        pi.hardware_PWM(self._gpio_pin, _MIN, _MIN)

    def change(self, duty_cycle: int):
         pi.hardware_PWM(self._gpio_pin, _FREQUENCY, duty_cycle)

class LEDController():
    def __init__(self, gpio_pin: int) -> None:
        self._gpio_pin: int = gpio_pin

    def turn_fully_on(self):
         pi.hardware_PWM(self._gpio_pin, _MAX, _MAX)

    def turn_off(self):
        pi.hardware_PWM(self._gpio_pin, _MIN, _MIN)

    def change(self, duty_cycle: int):
         pi.hardware_PWM(self._gpio_pin, _FREQUENCY, duty_cycle)


class PeltierController():
    def __init__(self, GPIOpeltier_in2: int, GPIOpeltier_in1) -> None:
        self._gpio_pin: int = GPIOpeltier_in1
        self._gpio_pin: int = GPIOpeltier_in1
    
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
