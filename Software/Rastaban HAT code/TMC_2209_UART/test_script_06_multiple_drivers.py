from src.TMC_2209_StepperDriver import *
import time



print("---")
print("SCRIPT START")
print("---")





#-----------------------------------------------------------------------
# initiate the TMC_2209 class
# use your pins for pin_en, pin_step, pin_dir here (step and dir can be left out)
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

tmc1.set_loglevel(Loglevel.DEBUG)
tmc1.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)

tmc2.set_loglevel(Loglevel.DEBUG)
tmc2.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)


#-----------------------------------------------------------------------
# these functions read and print the current settings in the TMC register
#-----------------------------------------------------------------------

print("---")
print("IOIN tmc0")
print("---")
tmc0.readIOIN()

print("---\n---")


print("---")
print("IOIN tmc1")
print("---")
tmc1.readIOIN()

print("---\n---")


print("---")
print("IOIN tmc2")
print("---")
tmc2.readIOIN()

print("---\n---")



#-----------------------------------------------------------------------
# deinitiate the TMC_2209 class
#-----------------------------------------------------------------------
tmc0.set_motor_enabled(False)
tmc1.set_motor_enabled(False)
tmc2.set_motor_enabled(False)
tmc0.deinit()
tmc1.deinit()
tmc2.deinit()
del tmc0
del tmc1
del tmc2

print("---")
print("SCRIPT FINISHED")
print("---")
