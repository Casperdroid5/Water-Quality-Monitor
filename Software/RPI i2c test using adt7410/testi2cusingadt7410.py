import time
import board
import adafruit_adt7410


"""
This code is primarely used to test if an i2c device is connected properly to the raspberry pi.
In this case we are using an temperature sensor.
"""

i2c = board.I2C()  # uses board.SCL and board.SDA
adt = adafruit_adt7410.ADT7410(i2c, address=0x48)
adt.high_resolution = True

while True:
    print(adt.temperature)
    time.sleep(0.5)