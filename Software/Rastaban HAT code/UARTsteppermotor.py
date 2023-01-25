import pigpio
from enums import State
import time
import constants
# Path to driver, important.
from TMC_2209_UART.src.TMC_2209_StepperDriver import *

"""
This code is used to control the TMC2209 stepper motors using UART.  
By using UART it is possible to set and read the parameters for the driver.
The goal of this code is to create control blocks for the library code.
"""


class UARTSTEPPERMOTOR(TMC_2209):

    def __init__(self, pi, EnableGPIOPin: int, DriverAddress: int) -> None:
        super().__init__(driver_address=DriverAddress, pin_en=EnableGPIOPin)
        self._pigpio = pi
        self._EnableGPIOPin: int = EnableGPIOPin
        self._driver_address: int = DriverAddress
        self.state = None

    def ControlMotorMovement(self, dirreg: bool, rpm: int, revolutions: float):
        self.set_direction_reg(dirreg)
        self.set_vactual_rpm(rpm, revolutions=revolutions)

    def SetMotorSettings(self, cur: int, interpol: bool, spread: bool, microstepres: int, interrsense: bool):
        self.set_current(cur)
        self.set_interpolation(interpol)
        self.set_spreadcycle(spread)
        self.set_microstepping_resolution(microstepres)
        self.set_internal_rsense(interrsense)

    def PrintCurrentDriverSettings(self):
        print("---\n---")  # for readability
        print("---CURRENTDRIVERSETTINGS---")  # for readability
        self.readIOIN()
        self.readCHOPCONF()
        self.readDRVSTATUS()
        self.readGCONF()
        print("---ENDING-CURRENTDRIVERSETTINGS---")  # for readability
        print("---\n---")  # for readability


if __name__ == "__main__":

    print("---")
    print("SCRIPT START")
    print("---")

    primarystepper = UARTSTEPPERMOTOR(
        pi=pigpio.pi(), EnableGPIOPin=27, DriverAddress=0)  # create object
    secondarystepper = UARTSTEPPERMOTOR(
        pi=pigpio.pi(), EnableGPIOPin=22, DriverAddress=1)  # create object
    focusstepper = UARTSTEPPERMOTOR(
        pi=pigpio.pi(), EnableGPIOPin=19, DriverAddress=2)  # create object

    primarystepper.SetMotorSettings(2000, True, True, 256, False)
    primarystepper.PrintCurrentDriverSettings()
    primarystepper.set_loglevel(Loglevel.DEBUG)
    primarystepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
    primarystepper.set_motor_enabled(True)
    primarystepper.ControlMotorMovement(True, 50, 3)
    time.sleep(1)
    primarystepper.ControlMotorMovement(False, 50, 3)
    primarystepper.set_motor_enabled(False)

    print("---\n---")  # for readability

    secondarystepper.SetMotorSettings(1200, True, True, 256, False)
    secondarystepper.PrintCurrentDriverSettings()
    secondarystepper.set_loglevel(Loglevel.DEBUG)
    secondarystepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
    secondarystepper.set_motor_enabled(True)
    secondarystepper.ControlMotorMovement(True, 150, 3)
    time.sleep(1)
    secondarystepper.ControlMotorMovement(False, 150, 3)
    secondarystepper.set_motor_enabled(False)

    print("---\n---")  # for readability

    focusstepper.SetMotorSettings(1000, True, True, 256, False)
    focusstepper.PrintCurrentDriverSettings()
    focusstepper.set_loglevel(Loglevel.DEBUG)
    focusstepper.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
    focusstepper.set_motor_enabled(True)
    focusstepper.ControlMotorMovement(True, 10, 1.5)  # focus motors up
    time.sleep(2)
    focusstepper.ControlMotorMovement(False, 10, 1.5)  # focus motors down
    focusstepper.set_motor_enabled(False)
    print("---\n---")  # for readability

primarystepper.deinit()
secondarystepper.deinit()
focusstepper.deinit()
del primarystepper
del secondarystepper
del focusstepper

print("---")
print("SCRIPT FINISHED")
print("---")
