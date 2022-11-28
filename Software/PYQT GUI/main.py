
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, 
        QPushButton, QRadioButton, QSlider, QSpinBox, QVBoxLayout)


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        disableWidgetsCheckBox = QCheckBox("&Disable all widgets")

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftGroupBox()    
        self.createBottomRightGroupBox()

        disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addStretch(1)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.bottomLeftGroupBox, 2, 0)

        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)


    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Camera control")
        self.topLeftGroupBox.setCheckable(True)
        self.topLeftGroupBox.setChecked(True)
        
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
        self.topLeftGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Temperature control")
        self.topRightGroupBox.setCheckable(True)
        self.topRightGroupBox.setChecked(True)
        
        EnablePeltier = QPushButton("Enable Peltier")
        EnablePeltier.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        spinBox = QSpinBox(self.topRightGroupBox)
        spinBox.setValue(50)


        layout = QGridLayout()
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(EnablePeltier, 1,2)
        layout.setRowStretch(5, 1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftGroupBox(self):
        self.bottomLeftGroupBox = QGroupBox("Motor control")
        self.bottomLeftGroupBox.setCheckable(True)
        self.bottomLeftGroupBox.setChecked(True)

        EnablePrimeryMotor = QPushButton("Enable primary motor")
        EnablePrimeryMotor.setDefault(True)

        EnableSecondaryMotor = QPushButton("Enable secondary motor")
        EnableSecondaryMotor.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(EnablePrimeryMotor)
        layout.addWidget(EnableSecondaryMotor)
        layout.addStretch(1)
        self.bottomLeftGroupBox.setLayout(layout)

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Light Intensity Control")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        slider = QSlider(Qt.Orientation.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        layout = QGridLayout()
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(slider, 3, 0)

        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec())
