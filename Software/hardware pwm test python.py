import pigpio
import time

pi = pigpio.pi()

pi.hardware_PWM(18, 0, 0) #Turn of PWM
time.sleep (0.1)
for dutycycle in range(1000000,360000, -100): #Slowly dimming the external led
    pi.hardware_PWM(18, 100000, dutycycle) #Hardware pwm setting GPIO18 (pin 12), switching frequency (10000hz) and duty cycle 
    #time.sleep (0)
    print(dutycycle)
pi.hardware_PWM(18, 0, 0) #Turn of PWM