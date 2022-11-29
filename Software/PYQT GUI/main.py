
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, 
        QPushButton, QRadioButton, QSlider, QSpinBox, QVBoxLayout)


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        disableWidgetsCheckBox = QCheckBox("&Disable all widgets")

        self.CameraControlBox()
        self.TemperatureControlBox()
        self.MotorControlBox()    
        self.LightControlBox()
        self.PowerGPIOBox()
        self.PanicBox()

        disableWidgetsCheckBox.toggled.connect(self.CameraControlBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.TemperatureControlBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.MotorControlBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.LightControlBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.PowerGPIOBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.PanicBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addStretch(1)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.CameraControlBox, 1, 0)
        mainLayout.addWidget(self.TemperatureControlBox, 1, 1)
        mainLayout.addWidget(self.LightControlBox, 2, 1)
        mainLayout.addWidget(self.MotorControlBox, 2, 0)
        mainLayout.addWidget(self.PowerGPIOBox, 3, 0)
        mainLayout.addWidget(self.PanicBox, 3, 1)

        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)


    def CameraControlBox(self):
        self.CameraControlBox = QGroupBox("Camera control")
        self.CameraControlBox.setCheckable(True)
        self.CameraControlBox.setChecked(True)
        
        StartRecordingButton = QPushButton("Start recording")
        StartRecordingButton.setDefault(True)

        StopRecordingButton = QPushButton("Stop recording")
        StopRecordingButton.setDefault(True)

        TakePictureButton = QPushButton("Take picture")
        TakePictureButton.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(StartRecordingButton)
        layout.addWidget(StopRecordingButton)
        layout.addWidget(TakePictureButton)
        layout.addStretch(1)
        self.CameraControlBox.setLayout(layout)

    def TemperatureControlBox(self):
        self.TemperatureControlBox = QGroupBox("Temperature control")
        self.TemperatureControlBox.setCheckable(True)
        self.TemperatureControlBox.setChecked(True)
        
        EnablePeltier = QPushButton("Enable Peltier")
        EnablePeltier.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True) 

        spinBox = QSpinBox(self.TemperatureControlBox)
        spinBox.setValue(50)

        layout = QGridLayout()
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(EnablePeltier, 1,2)
        layout.setRowStretch(5, 1)
        self.TemperatureControlBox.setLayout(layout)

    def MotorControlBox(self):
        self.MotorControlBox = QGroupBox("Motor control")
        self.MotorControlBox.setCheckable(True)
        self.MotorControlBox.setChecked(True)

        EnablePrimeryMotor = QPushButton("Enable primary motor")
        EnablePrimeryMotor.setDefault(True)

        EnableSecondaryMotor = QPushButton("Enable secondary motor")
        EnableSecondaryMotor.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(EnablePrimeryMotor)
        layout.addWidget(EnableSecondaryMotor)
        layout.addStretch(1)
        self.MotorControlBox.setLayout(layout)

    def LightControlBox(self):
        self.LightControlBox = QGroupBox("Light Intensity Control")
        self.LightControlBox.setCheckable(True)
        self.LightControlBox.setChecked(True)

        spinBox = QSpinBox(self.LightControlBox)
        spinBox.setValue(50)

        layout = QGridLayout()
        layout.addWidget(spinBox, 1, 0, 1, 2)

        layout.setRowStretch(5, 1)
        self.LightControlBox.setLayout(layout)

    def PowerGPIOBox(self):
        self.PowerGPIOBox = QGroupBox("Power GPIO Control")
        self.PowerGPIOBox.setCheckable(True)
        self.PowerGPIOBox.setChecked(True)

        PGPIO1SPIN = QSpinBox(self.PowerGPIOBox)
        PGPIO1SPIN.setValue(50)
        
        PGPIO2SPIN = QSpinBox(self.PowerGPIOBox)
        PGPIO2SPIN.setValue(50)

        layout = QGridLayout()
        layout.addWidget(PGPIO1SPIN, 1, 0, 1, 2)
        layout.addWidget(PGPIO2SPIN, 1, 1, 1, 2)

        layout.setRowStretch(5, 1)
        self.PowerGPIOBox.setLayout(layout)
        
    def PanicBox(self):
        self.PanicBox = QGroupBox("Panic buttons")
        self.PanicBox.setCheckable(True)
        self.PanicBox.setChecked(True)

        KillAllPower = QPushButton("Kill all power")
        KillAllPower.setDefault(True)

        ShutdownRaspberryPi = QPushButton("Shutdown RaspberryPi")
        ShutdownRaspberryPi.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(KillAllPower)
        layout.addWidget(ShutdownRaspberryPi)
        layout.addStretch(1)
        self.PanicBox.setLayout(layout)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec())
