import pigpio

pi = pigpio.pi()

DIR = 20  # Direction GPIO Pin
STEP = 16  # Step GPIO Pin
EN = 21  # enable or dissable stepper driver

CW = 1  # Clockwise Rotation
CCW = 0  # Counterclockwise Rotation
# SPR = 200  # Steps per Revolution (360 / 1.8) = 200 <-- source code has 7.5 degree steps for SPR of 48.


pi.set_mode(DIR, pigpio.OUTPUT)  # Set GPIO DIR as output
pi.set_mode(STEP, pigpio.OUTPUT)  # Set GPIO STEP as output
pi.set_mode(EN, pigpio.OUTPUT)  # Set GPIO EN as output

pi.write(EN, 1)
pi.write(DIR, CW)
pi.set_PWM_frequency(STEP, 50)

# def move(val):
# value = int(round(255 * abs(val)/100)) #value 0-255 scaled to 0-100
# pi.write(EN,0) # write to enable
# pi.write(DIR,CW) # give direction


