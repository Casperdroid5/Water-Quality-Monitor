import sys
# importing libraries
from tokenize import Pointfloat
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setCentralWidget(self)  # Set the central widget of the Window.


class Button(QMainWindow):
    super().__init__()

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        self.setWindowTitle("My Oneshot App")  # Also change the window title.


class Dial(QMainWindow):
    def __init__(self):
        super().MainWindow()
        dial = QDial("Turn me!")
        dial.rotated.connect(self.the_dial_was_rotated)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
