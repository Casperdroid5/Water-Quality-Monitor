import pigpio
import time

pi = pigpio.pi()
Highest_value = 1000000
Lowest_value = 350000
hardwareGPIOPin = 18

pi.hardware_PWM(hardwareGPIOPin, 0, 0) #Turn of PWM
time.sleep (0.1)
for dutycycle in range(Highest_value,Lowest_value, -100): #Slowly dimming the external led
    pi.hardware_PWM(hardwareGPIOPin, 100000, dutycycle) #Hardware pwm setting GPIO18 (pin 12), switching frequency (10000hz) and duty cycle 
    #time.sleep (0)
    print(dutycycle)
pi.hardware_PWM(hardwareGPIOPin, 0, 0) #Turn of PWM

time.sleep (0.1)
for dutycycle in range(Lowest_value, Highest_value, 100): #Slowly brightening the external led
    pi.hardware_PWM(hardwareGPIOPin, 100000, dutycycle) #Hardware pwm setting GPIO18 (pin 12), switching frequency (10000hz) and duty cycle 
    #time.sleep (0)
    print(dutycycle)
pi.hardware_PWM(hardwareGPIOPin, 0, 0) #Turn of PWM