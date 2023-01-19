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

    def __init__(self, pi, EnableGPIOPin: int, DriverAdress: int) -> None:
        super().__init__(EnableGPIOPin) 
        self._pigpio = pi
        self._EnableGPIOPin : int = EnableGPIOPin   
        self.driver_address : int = DriverAdress
        self.state = None

    def ControlMotorMovement(self, dirreg: bool, rpm: int, revolutions: float):    
        self.set_direction_reg(dirreg)
        self.set_vactual_rpm(rpm, revolutions = revolutions)
        
    def SetMotorSettings(self, cur: int, interpol: bool, spread: bool, microstepres: int, interrsense: bool): 
        self.set_current(cur)
        self.set_interpolation(interpol)
        self.set_spreadcycle(spread)
        self.set_microstepping_resolution(microstepres)
        self.set_internal_rsense(interrsense)
    
    def PrintCurrentDriverSettings(self): 
        print("---\n---") # for readability
        print("---CURRENTDRIVERSETTINGS---") # for readability
        self.readIOIN()
        self.readCHOPCONF()
        self.readDRVSTATUS()
        self.readGCONF()
        print("---ENDING-CURRENTDRIVERSETTINGS---") # for readability
        print("---\n---") # for readability


if __name__ == "__main__":
    
   print("---")
   print("SCRIPT START")
   print("---")
   
   primarystepper = UARTSTEPPERMOTOR(pi = pigpio.pi(), EnableGPIOPin = 27, DriverAdress = 0) # create object
   primarystepper.SetMotorSettings(900, True, True, 8, False)
   primarystepper.PrintCurrentDriverSettings()
   #primarystepper.set_loglevel(Loglevel.DEBUG)
   #primarystepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
   primarystepper.set_motor_enabled(True)
   primarystepper.ControlMotorMovement(True, 30, 2)
   primarystepper.set_motor_enabled(False)
   
   print("---\n---") # for readability
   
   secondarystepper = UARTSTEPPERMOTOR(pi = pigpio.pi(), EnableGPIOPin = 22, DriverAdress = 1) # create object   
   secondarystepper.SetMotorSettings(1200, True, True, 2, False)
   secondarystepper.PrintCurrentDriverSettings()
   #primarystepper.set_loglevel(Loglevel.DEBUG)
   #primarystepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
   secondarystepper.set_motor_enabled(True)
   secondarystepper.ControlMotorMovement(True, 30, 8)
   secondarystepper.set_motor_enabled(False)
   print("---\n---") # for readability

primarystepper.deinit()
secondarystepper.deinit()
del primarystepper
del secondarystepper

print("---")
print("SCRIPT FINISHED")
print("---")

