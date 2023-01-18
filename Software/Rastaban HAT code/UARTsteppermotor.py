import time
import pigpio
from enums import State
import constants
from TMC_2209_UART.src.TMC_2209_StepperDriver import TMC_2209 # Path to driver, important.

"""
This code is used to control the TMC2209 stepper motors using UART.  
By using UART it is possible to set and read the parameters for the driver.
"""

class UARTSTEPPERMOTOR(TMC_2209):

    def __init__(self, pi, EnableGPIOPin: int) -> None:
        super().__init__(EnableGPIOPin) 
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
   primarystepper = UARTSTEPPERMOTOR(pi = pigpio.pi(), EnableGPIOPin = 27) 
   
   primarystepper.SetMotorSettings(900, True, False, 256, False)
   primarystepper.PrintCurrentSettings()
   #primarystepper.set_loglevel(Loglevel.DEBUG)
   #primarystepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
   primarystepper.ControlMotorMovement(True, 30, 1, True)
   primarystepper.set_motor_enabled(False)
   print("---\n---") # for readability
   secondarystepper = UARTSTEPPERMOTOR(pi = pigpio.pi(), EnableGPIOPin = 22)   
   secondarystepper.SetMotorSettings(900, True, False, 2, False)
   secondarystepper.PrintCurrentSettings()
   #primarystepper.set_loglevel(Loglevel.DEBUG)
   #primarystepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
   secondarystepper.ControlMotorMovement(True, 90, 2, False)
   secondarystepper.set_motor_enabled(False)
   print("---\n---") # for readability

primarystepper.deinit()
secondarystepper.deinit()
del primarystepper
del secondarystepper

print("---")
print("SCRIPT FINISHED")
print("---")

