from src.TMC_2209_StepperDriver import *
import time



print("---")
print("SCRIPT START")
print("---")





#-----------------------------------------------------------------------
# initiate the TMC_2209 class
# use your pin for pin_en here
#-----------------------------------------------------------------------
tmc0 = TMC_2209(27, driver_address=0)
tmc1 = TMC_2209(22, driver_address=1)
tmc2 = TMC_2209(19, driver_address=2)


#-----------------------------------------------------------------------
# set the loglevel of the libary (currently only printed)
# set whether the movement should be relative or absolute
# both optional
#-----------------------------------------------------------------------
tmc0.set_loglevel(Loglevel.DEBUG)
tmc0.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)

#-----------------------------------------------------------------------
# these functions change settings in the TMC register
#-----------------------------------------------------------------------
tmc0.set_direction_reg(False)
tmc0.set_current(300)
tmc0.set_interpolation(True)
tmc0.set_spreadcycle(False)
tmc0.set_microstepping_resolution(2)
tmc0.set_internal_rsense(False)


print("---\n---")

#-----------------------------------------------------------------------
# activate the motor current output
#-----------------------------------------------------------------------
tmc0.set_motor_enabled(True)

#-----------------------------------------------------------------------
# set_vactual_rpm and set_vactual_rps accept "revolutions" and "duration" as keyword parameter
# if duration is set the script will set VActual to that rpm for that duration and stop the motor afterwards
# if revolutions the script will calculate the duration based on the speed and the revolutions
# Movement of the Motor will not be very accurate with this way
#-----------------------------------------------------------------------
tmc0.set_vactual_rpm(30, revolutions=2)
tmc0.set_vactual_rpm(-120, revolutions=2)
time.sleep(1)
tmc0.set_vactual_rpm(30, duration=4)
tmc0.set_vactual_rpm(-120, duration=1)


#-----------------------------------------------------------------------
# deactivate the motor current output
#-----------------------------------------------------------------------
tmc0.set_motor_enabled(False)

print("---\n---")





#-----------------------------------------------------------------------
# deinitiate the TMC_2209 class
#-----------------------------------------------------------------------
tmc0.deinit()
del tmc0

print("---")
print("SCRIPT FINISHED")
print("---")
