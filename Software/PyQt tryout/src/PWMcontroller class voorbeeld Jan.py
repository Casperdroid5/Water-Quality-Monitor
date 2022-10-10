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
