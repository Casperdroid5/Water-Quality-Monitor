from src.TMC_2209_StepperDriver import *
import time


print("---")
print("SCRIPT START")
print("---")

#-----------------------------------------------------------------------
# initiate the TMC_2209 class
# use your pins for pin_en, pin_step, pin_dir here
#-----------------------------------------------------------------------
tmcPrimary = TMC_2209(pin_en=27, driver_address=0, no_uart=False, loglevel=Loglevel.DEBUG)
tmcSecondary = TMC_2209(pin_en=22, driver_address=1, no_uart=False, loglevel=Loglevel.DEBUG)
tmcFocus = TMC_2209(pin_en=19, driver_address=2, no_uart=False, loglevel=Loglevel.DEBUG)

#-----------------------------------------------------------------------
# these functions read and print the current settings in the TMC register
#-----------------------------------------------------------------------
print("---\n---")
tmcPrimary.test_uart()
print("---\n---")
tmcSecondary.test_uart()
print("---\n---")
tmcFocus.test_uart()
print("---\n---")

#-----------------------------------------------------------------------
# deinitiate the TMC_2209 class
#-----------------------------------------------------------------------
tmcPrimary.deinit()
tmcSecondary.deinit()
tmcFocus.deinit()
del tmcPrimary
del tmcSecondary
del tmcFocus	

print("---")
print("SCRIPT FINISHED")
print("---")
