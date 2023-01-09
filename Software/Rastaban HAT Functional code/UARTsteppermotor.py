import time
import pigpio
from enums import State
import constants
from src.TMC_2209.TMC_2209_StepperDriver import *

"""
This code is used to control the TMC2209 stepper motors using UART.  
By using UART it is possible to set parameters for the driver.
"""


class UARTSTEPPERMOTORS():

    def __init__(self, pi, EnableGPIOPin: int) -> None: 
        self._pigpio = pi
        self._EnableGPIOPin: int = EnableGPIOPin   
        self.state = None

    def ControlMotorMovement(self, dirreg: bool, rpm: int, revolutions: float, State: bool):    
        tmc.set_direction_reg(dirreg)
        set_vactual_rpm(rpm, revolutions = revolutions)
        tmc.set_motor_enabled(State)
        
    def SetMotorSettings(self, cur: int, interpol: bool, spread: bool, microstepres: int, interrsense: bool): 
        tmc.set_current(cur)
        tmc.set_interpolation(interpol)
        tmc.set_spreadcycle(spread)
        tmc.set_microstepping_resolution(microstepres)
        tmc.set_internal_rsense(interrsense)
    
    def PrintCurrentSettings(self): 
        tmc.readIOIN()
        tmc.readCHOPCONF()
        tmc.readDRVSTATUS()
        tmc.readGCONF()
        print("---\n---") # for readability


if __name__ == "__main__":
   tmc = UARTSTEPPERMOTORS(21)
   #tmc.set_loglevel(Loglevel.DEBUG)
   #tmc.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
   tmc.set_motor_enabled(True)


#-----------------------------------------------------------------------
# deinitiate the TMC_2209 class
#-----------------------------------------------------------------------
tmc.deinit()
del tmc

print("---")
print("SCRIPT FINISHED")
print("---")

