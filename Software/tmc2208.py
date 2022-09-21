# *** TMC2209 Test Program v0.1  tlfong01  2022jan02hkt1126 ***

# *** Import ***
import pigpio #RPI GPIO library
import utime

pi = pigpio.pi()
hardwareGPIOPin = 18

direction = pi(14)
step = pi(15)
enable = pi(13)

enable.low()

direction.high()

def stepOne():
  step.high()
  utime.sleep(0.001)
  step.low()


while True:
    stepOne()
    utime.sleep(0.1)