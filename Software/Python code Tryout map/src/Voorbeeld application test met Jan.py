import PWMController.py


pwm_application_test_message = "You should see the green LED on the Pi board turn on for 3 seconds, turn off for 3 seconds, turn half power on for 3 seconds."
def pwm_application_test():
    test_pin = 15
    test_controller: PWMController = PWMController(test_pin)
    test_controller.turn_fully_on()
    sleep(3)
    test_controller.turn_fully_off()
    sleep(3)
    test_controller.change(duty_cycle = 50)
    sleep(3)

template_application_test_message = "What you should see..."
def template_application_test():
    pass

def main():
    print(pwm_application_test_message)
    pwm_application_test()
    print(template_application_test_message)
    template_application_test()



if __name__ == "__main__":
    main()