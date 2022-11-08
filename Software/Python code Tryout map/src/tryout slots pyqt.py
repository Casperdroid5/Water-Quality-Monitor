# importing libraries
from tokenize import Pointfloat
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import pigpio
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import time

class MicroscopeLed(QObject):
    postMessage = pyqtSignal(str) #output wire

    pi = pigpio.pi()
    hardwareGPIOPin = 18

    def __init__(self,pi):
    self.pi = pi
    
    @pyqtSlot(double)
    def setVal(self, val):
        self.value = round(val,1)
        try:
            if self.pio is not None:
                self.pio.hardware_PWM(self.hardwareGPIOPin, self.DutyCycle, )


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("PWM control knob")

        # setting geometry
        self.setGeometry(100, 100, 500, 500)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):
        # creating QDial object
        dial = QDial(self)

        # setting geometry to the dial
        dial.setGeometry(200, 200, 200, 200)

        # setting minimum value to the dial
        dial.setMinimum(0)

        # setting maximum value to the dial
        dial.setMaximum(62)

        # making notch visible
        dial.setNotchesVisible(True)

        # creating a label
        label = QLabel("Brightness Level not set", self)

        # setting geometry to the label
        label.setGeometry(220, 125, 200, 60)

        # making label multiline
        label.setWordWrap(True)

        # adding action to the dial
        QtCore.QObject.connect(dial, QtCore.SIGNAL("KnobRotated"), KnobRotated())



    def KnobRotated():
        label.setText("Brightness Level = " + str(KnobValue))
        DutyCycle = int((KnobValue*10000)+380000) # typecast str to int. 6200000 steps between fully of and on (dutycycle)  
        print(DutyCycle) # debug value
        pi.set_PWM_range(hardwareGPIOPin, 40000)
        pi.hardware_PWM(hardwareGPIOPin, 100000, DutyCycle)  # Hardware pwm setting GPIO18 (pin 12), switching frequency (10000hz) and duty cycle, only works with hardware attached
        print("DutyCycle set to: " + str(DutyCycle))

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
