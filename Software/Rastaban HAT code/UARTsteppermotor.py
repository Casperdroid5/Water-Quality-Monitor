import time
import pigpio
from enums import State
import constants
from TMC_2209_UART.src.TMC_2209_StepperDriver import * # Path to driver, important.

"""
This code is used to control the TMC2209 stepper motors using UART.  
By using UART it is possible to set and read the parameters for the driver.
"""


class UARTSTEPPERMOTOR(TMC_2209):

    def __init__(self, pi, EnableGPIOPin: int) -> None: 
        self._pigpio = pi
        self._EnableGPIOPin : int = EnableGPIOPin   
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
   primarystepper1 = UARTSTEPPERMOTOR(pi = pigpio.pi(), EnableGPIOPin = 27) 
   
   primarystepperA = primarystepper1.SetMotorSettings(900, True, False, 256, False)
   primarystepperA = primarystepper1.PrintCurrentSettings()
   #primarystepper.set_loglevel(Loglevel.DEBUG)
   #primarystepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
   primarystepperA = primarystepper1.ControlMotorMovement(True, 30, 1)
  
   primarystepperA = primarystepper1.set_motor_enabled(False)

   secondarystepper2 = UARTSTEPPERMOTOR(pi = pigpio.pi(), EnableGPIOPin = 22) 
   
   secondarystepperB = secondarystepper2.SetMotorSettings(900, True, False, 2, False)
   secondarystepperB = secondarystepper2.PrintCurrentSettings()
   #primarystepper.set_loglevel(Loglevel.DEBUG)
   #primarystepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
   secondarystepperB = secondarystepper2.ControlMotorMovement(True, 90, 2)
  
   secondarystepperB = secondarystepper2.set_motor_enabled(False)


#primarystepper.deinit()
#del primarystepper

print("---")
print("SCRIPT FINISHED")
print("---")

