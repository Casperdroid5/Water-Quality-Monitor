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
        self.set_direction_reg(dirreg)
        self.set_vactual_rpm(rpm, revolutions = revolutions)
        self.set_motor_enabled(State)
        
    def SetMotorSettings(self, cur: int, interpol: bool, spread: bool, microstepres: int, interrsense: bool): 
        self.set_current(cur)
        self.set_interpolation(interpol)
        self.set_spreadcycle(spread)
        self.set_microstepping_resolution(microstepres)
        self.set_internal_rsense(interrsense)
    
    def PrintCurrentSettings(self): 
        self.readIOIN()
        self.readCHOPCONF()
        self.readDRVSTATUS()
        self.readGCONF()
        print("---\n---") # for readability


if __name__ == "__main__":
   primarystepper = UARTSTEPPERMOTORS(21) 
   primarystepper = primarystepper.SetMotorSettings(900, True, False, 256, False)
   primarystepper = primarystepper.PrintCurrentSettings()
   #primarystepper.set_loglevel(Loglevel.DEBUG)
   #primarystepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
   primarystepper = primarystepper.ControlMotorMovement(False, )
  
   primarystepper.set_motor_enabled(True)


#primarystepper.deinit()
#del primarystepper

print("---")
print("SCRIPT FINISHED")
print("---")

