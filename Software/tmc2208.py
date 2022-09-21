# *** TMC2209 Test Program v0.1  tlfong01  2022jan02hkt1126 ***

# *** Import ***
import pigpio #RPI GPIO library
import utime

direction = Pin(14, Pin.OUT)
step = Pin(15, Pin.OUT)
enable = Pin(13, Pin.OUT)

enable.low()

direction.high()

def stepOne():
  step.high()
  utime.sleep(0.001)
  step.low()


while True:
    stepOne()
    utime.sleep(0.1)