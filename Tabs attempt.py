# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:52:48 2026

@author: bn23289
"""
#TODO add in visuals, change the way the second tab looks as I don't like it being squished so much :(
#TODO: change default combobox indexes to be useful, not having like, spot diameter in nm (?????)

import sys
from PyQt5.QtWidgets import QCheckBox, QComboBox, QGridLayout, QMainWindow, QApplication, QTextEdit, QLineEdit,  QWidget, QTabWidget, QVBoxLayout, QLabel,QPushButton
import numpy as np

#Creating popup windows with equations:
class PB1Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        image = QLabel(pixmap=QPixmap(r"C:\Users\Arcti\Downloads\AERHGAEHSRTH.png"))
        self.setLayout(layout)

# Creating the main window
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'What I got up to in Bordeaux: a script'
        self.setWindowTitle(self.title)
        self.setGeometry(400, 100, 100, 100)
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()

# Creating tab widgets
class MyTabWidget(QWidget):
    def __init__(self, parent):

        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab1, "Fluence")
        self.tabs.addTab(self.tab2, "Beam stats")
        self.tabs.addTab(self.tab3, "Misc")

        self.combobox = QComboBox(self)
        self.combobox.addItem("nW",1e-9)
        self.combobox.addItem("uW",1e-6)
        self.combobox.addItem("mW",1e-3)
        self.combobox.addItem("W",1)

        self.combobox2 = QComboBox(self)
        self.combobox2.addItem("nm",1e-9)
        self.combobox2.addItem("um",1e-6)
        self.combobox2.addItem("mm",1e-3)
        self.combobox2.addItem("cm",1e-2)

        self.combobox3 = QComboBox(self)
        self.combobox3.addItem("Hz",1)
        self.combobox3.addItem("kHz",1e3)
        self.combobox3.addItem("MHz",1e6)

        self.comboboxA = QComboBox(self)
        self.comboboxA.addItem("nW",1e-9)
        self.comboboxA.addItem("uW",1e-6)
        self.comboboxA.addItem("mW",1e-3)
        self.comboboxA.addItem("W",1)


        self.combobox2A = QComboBox(self)
        self.combobox2A.addItem("nm",1e-9)
        self.combobox2A.addItem("um",1e-6)
        self.combobox2A.addItem("mm",1e-3)
        self.combobox2A.addItem("cm",1e-2)

        self.combobox3A = QComboBox(self)
        self.combobox3A.addItem("Hz",1)
        self.combobox3A.addItem("kHz",1e3)
        self.combobox3A.addItem("MHz",1e6)

        self.combobox4 = QComboBox(self)
        self.combobox4.addItem("fs",1e-15)
        self.combobox4.addItem("ps",1e-12)

        self.combobox6 = QComboBox(self)
        self.combobox6.addItem("Jcm\u207b\u00b2",1e-4)
        self.combobox6.addItem("mJcm\u207b\u00b2",(1e-4*1e3))
        self.combobox6.addItem("μJcm\u207b\u00b2",(1e-4*1e6))
        self.combobox6.addItem("Jmm\u207b\u00b2",1e-6)
        self.combobox6.addItem("mJmm\u207b\u00b2",(1e-6*1e3))
        self.combobox6.addItem("μJmm\u207b\u00b2",(1e-6*1e6))

        self.combobox7 = QComboBox(self)
        self.combobox7.addItem("J",  1)
        self.combobox7.addItem("mJ", 1e3)
        self.combobox7.addItem("μJ", 1e6)
        self.combobox7.addItem("nJ", 1e9)

        self.combobox8 = QComboBox(self)
        self.combobox8.addItem("m\u00b2", 1)
        self.combobox8.addItem("cm\u00b2",1e2)
        self.combobox8.addItem("mm\u00b2",1e3)
        self.combobox8.addItem("μm\u00b2",1e6)
        self.combobox8.addItem("nm\u00b2",1e9)

        self.combobox9 = QComboBox(self) #Peak intensity
        self.combobox9.addItem("Wcm\u00b2", 1e-4)
        self.combobox9.addItem("kWcm\u00b2",1e-3*1e-4)
        self.combobox9.addItem("MWcm\u00b2",1e-6*1e-4)
        self.combobox9.addItem("GWcm\u00b2",1e-9*1e-4)

        self.combobox10 = QComboBox(self) #Peak power
        self.combobox10.addItem("W", 1)
        self.combobox10.addItem("kW",1e-3)
        self.combobox10.addItem("MW",1e-6)
        self.combobox10.addItem("GW",1e-9)

        self.combobox11 = QComboBox(self) #Average intensity
        self.combobox11.addItem("mWcm\u00b2",(1e3*1e-4))
        self.combobox11.addItem("Wcm\u00b2", 1e-4)
        self.combobox11.addItem("kWcm\u00b2",(1e-3*1e-4))
        self.combobox11.addItem("MWcm\u00b2",(1e-6*1e-4))

        self.combobox12 = QComboBox(self) #Pulse separation
        self.combobox12.addItem("s", 1)
        self.combobox12.addItem("ms",1000)
        self.combobox12.addItem("μs",1000000)

        # Create first tab
        vbox = QGridLayout()
        self.Checkbox = QCheckBox("More info", self)
        self.PB1 = QPushButton("Equations", self)
        self.l2 = QLabel("Power")
        self.l3 = QLabel("Spot diameter")
        self.l4 = QLabel("Rep rate")
        self.l2A = QLabel("Power")
        self.l3A = QLabel("Spot diameter")
        self.l4A = QLabel("Rep rate")
        self.l5 = QLabel("Pulse FWHM")
        self.l6 = QLabel("Energy per pulse")
        self.l7 = QLabel("Beam area")
        self.l8 = QLabel("Fluence")
        self.l9 = QLabel("Result shown below")
        self.label2 = QLabel("Peak power")
        self.label3 = QLabel("Average intensity")
        self.label4 = QLabel("Peak intensity")
        self.label5 = QLabel("Pulse separation")
        self.label6 = QLabel("Duty cycle")
        self.label7 = QLabel("Unitless")
        self.le1 = QTextEdit(self)
        self.le1.setReadOnly(True)
        self.le1.setMaximumSize(200,30)
        self.le2 = QTextEdit(self)
        self.le2.setReadOnly(True)
        self.le2.setMaximumSize(200,30)
        self.le3 = QTextEdit(self)
        self.le3.setReadOnly(True)
        self.le3.setMaximumSize(200,30)
        self.le4 = QTextEdit(self)
        self.le4.setReadOnly(True)
        self.le4.setMaximumSize(200,30)
        self.le5 = QTextEdit(self)
        self.le5.setReadOnly(True)
        self.le5.setMaximumSize(200,30)
        self.line_edit1 = QLineEdit("35",    self)
        self.line_edit2 = QLineEdit("6",     self)
        self.line_edit3 = QLineEdit("1000",  self)
        self.line_edit1A = QLineEdit("35",    self)
        self.line_edit2A = QLineEdit("6",     self)
        self.line_edit3A = QLineEdit("1000",  self)
        self.line_edit4 = QLineEdit("100",   self)
        self.line_Text = QTextEdit(self)
        self.line_Text.setReadOnly(True)
        self.line_Text2 = QTextEdit(self)
        self.line_Text2.setReadOnly(True)
        self.line_Text3 = QTextEdit(self)
        self.line_Text3.setReadOnly(True)
        self.line_edit1.setMaximumSize(200,30),self.line_edit2.setMaximumSize(200,30),self.line_edit3.setMaximumSize(200,30)
        self.line_edit1A.setMaximumSize(200,30),self.line_edit2A.setMaximumSize(200,30),self.line_edit3A.setMaximumSize(200,30)
        self.line_edit4.setMaximumSize(200,30),self.line_Text.setMaximumSize(200,30),self.line_Text2.setMaximumSize(200,30)
        self.line_Text3.setMaximumSize(200,30)
        vbox.addWidget(self.l2, 1,0)
        vbox.addWidget(self.l3, 2,0)
        vbox.addWidget(self.l4, 3,0)
        vbox.addWidget(self.l5, 4,0)
        vbox.addWidget(self.l6, 6,0)
        vbox.addWidget(self.l7, 7,0)
        vbox.addWidget(self.l8, 8,0)
        vbox.addWidget(self.line_edit1,1,1)
        vbox.addWidget(self.line_edit2,2,1)
        vbox.addWidget(self.line_edit3,3,1)
        vbox.addWidget(self.line_edit4,4,1)
        vbox.addWidget(self.line_Text,6,1)
        vbox.addWidget(self.line_Text2,7,1)
        vbox.addWidget(self.line_Text3,8,1)
        vbox.addWidget(self.combobox,1,2)
        vbox.addWidget(self.combobox2,2,2)
        vbox.addWidget(self.combobox3,3,2)
        vbox.addWidget(self.combobox4,4,2)
        vbox.addWidget(self.combobox7,6,2)
        vbox.addWidget(self.combobox8,7,2)
        vbox.addWidget(self.combobox6,8,2)
        vbox.addWidget(self.Checkbox, 9,0)
        vbox.addWidget(self.PB1,      9,1)
        vbox.addWidget(self.le1, 10,1)
        vbox.addWidget(self.le2, 11,1)
        vbox.addWidget(self.le3, 12,1)
        vbox.addWidget(self.le4, 13,1)
        vbox.addWidget(self.le5, 14,1)
        vbox.addWidget(self.label2, 10,0)
        vbox.addWidget(self.label3, 11,0)
        vbox.addWidget(self.label4, 12,0)
        vbox.addWidget(self.label5, 13,0)
        vbox.addWidget(self.label6, 14,0)
        vbox.addWidget(self.label7, 14,2)
        vbox.addWidget(self.combobox9, 12,2)
        vbox.addWidget(self.combobox10, 10,2)
        vbox.addWidget(self.combobox11, 11,2)
        vbox.addWidget(self.combobox12, 13,2)
        self.tab1.setLayout(vbox)

        #Create second tab
        vbox2 = QGridLayout()
        self.PB2 = QPushButton("Equations", self)
        self.PB2.setMaximumSize(200,30)
        self.T2Q = QLabel("Optical Density")
        self.T2Q2 = QLabel("No units")
        self.T2Q3 = QLabel("Exciting pulse")
        self.T2Q4 = QLabel("Film thickness")
        self.T2Q5 = QLabel("Excitation density")
        self.T2Q6 = QLabel("Output")
        self.T2Q6.setStyleSheet("border: 1px solid black;")
        self.T2Q7 = QLabel("ditto but cm2 WIP")

        self.line_editT2 = QLineEdit("0.5", self)
        self.line_editT2.setMaximumSize(200,30)
        self.line_edit2T2 = QLineEdit("800", self)
        self.line_edit2T2.setMaximumSize(200,30)
        self.line_edit3T2 = QLineEdit("70", self)
        self.line_edit3T2.setMaximumSize(200,30)
        self.line_edit4T2 = QTextEdit(self)
        self.line_edit4T2.setMaximumSize(200,30)
        self.line_edit4T2.setReadOnly(True)
        self.line_edit5T2 = QTextEdit(self)
        self.line_edit5T2.setMaximumSize(200,30)
        self.line_edit5T2.setReadOnly(True)

        self.cb1T2 = QComboBox(self)
        self.cb1T2.addItem("ʎ (nm)", 1)
        self.cb1T2.addItem("1/ʎ (cm\u00b1)", 1) #Put value here to convert to nm
        self.cb1T2.addItem("1/f (Hz)",1) ##Put value here to convert to nm

        self.cb2T2 = QComboBox(self)
        self.cb2T2.addItem("nm",1e-9)
        self.cb2T2.addItem("μm",1e-6)
        self.cb2T2.addItem("mm",1e-3)
        self.cb2T2.addItem("cm",1e-2)

        self.c3T2 = QComboBox(self)
        self.c3T2.addItem("cm\u207b\u00b3", 1)

        self.c4T2 = QComboBox(self)
        self.c4T2.addItem("cm\u207b\u00b2",1)

        vbox2.addWidget(self.l2A,  1,0)
        vbox2.addWidget(self.l3A,  2,0)
        vbox2.addWidget(self.l4A,  3,0)
        vbox2.addWidget(self.T2Q,  4,0)
        vbox2.addWidget(self.T2Q2, 4,2)
        vbox2.addWidget(self.T2Q3, 5,0)
        vbox2.addWidget(self.T2Q4, 6,0)
        vbox2.addWidget(self.T2Q6, 7,0)
        vbox2.addWidget(self.T2Q5, 8,0)
        vbox2.addWidget(self.T2Q7, 9,0)
        vbox2.addWidget(self.line_edit1A,1,1)
        vbox2.addWidget(self.line_edit2A,2,1)
        vbox2.addWidget(self.line_edit3A,3,1)
        vbox2.addWidget(self.line_editT2, 4,1)
        vbox2.addWidget(self.line_edit2T2, 5,1)
        vbox2.addWidget(self.line_edit3T2, 6,1)
        vbox2.addWidget(self.line_edit4T2, 8,1)
        vbox2.addWidget(self.line_edit5T2, 9,1)
        vbox2.addWidget(self.comboboxA,1,2)
        vbox2.addWidget(self.combobox2A,2,2)
        vbox2.addWidget(self.combobox3A,3,2)
        vbox2.addWidget(self.cb1T2, 5,2)
        vbox2.addWidget(self.cb2T2, 6,2)
        vbox2.addWidget(self.c3T2, 8,2)
        vbox2.addWidget(self.c4T2, 9,2)
        vbox2.addWidget(self.PB2,  7,1)
        self.tab2.setLayout(vbox2)

        #Create third tab
        vbox3 = QGridLayout()
        self.PB3 = QPushButton("Equations", self)
        self.T3Q = QLabel("Wavelength")
        self.T3Q2 = QLabel("Focus length")
        self.T3Q3 = QLabel("Beam diameter")
        self.T3Q4 = QLabel("M\u00b2")
        self.T3Q5 = QLabel("Spot size diameter")
        self.T3Q6 = QLabel("Rayleigh length")
        self.T3Q7 = QLabel("(if needed)")
        self.LET3 = QLineEdit("800", self)
        self.LET3.setMaximumSize(200,30)
        self.LE2T3 = QLineEdit("100", self)
        self.LE2T3.setMaximumSize(200,30)
        self.LE3T3 = QLineEdit("6", self)
        self.LE3T3.setMaximumSize(200,30)
        self.LE4T3 = QLineEdit("1", self)
        self.LE4T3.setMaximumSize(200,30)

        self.cb1T3 = QComboBox(self)
        self.cb1T3.addItem("ʎ (nm)", 1e-9)
        self.cb1T3.addItem("1/ʎ (cm\u00b1)", 1) #Put value here to convert to nm
        self.cb1T3.addItem("1/f (Hz)",1)

        self.cb2T3 = QComboBox(self)
        self.cb2T3.addItem("m", 1)
        self.cb2T3.addItem("cm",1e-2)
        self.cb2T3.addItem("mm",1e-3)
        self.cb2T3.addItem("μm",1e-6)
        self.cb2T3.addItem("nm",1e-9)

        self.cb3T3 = QComboBox(self)
        self.cb3T3.addItem("m", 1)
        self.cb3T3.addItem("cm",1e-2)
        self.cb3T3.addItem("mm",1e-3)
        self.cb3T3.addItem("μm",1e-6)
        self.cb3T3.addItem("nm",1e-9)

        self.cb4T3 = QLabel("No units")

        self.cb5T3 = QComboBox(self)
        self.cb5T3.addItem("m", 1)
        self.cb5T3.addItem("cm",1e2)
        self.cb5T3.addItem("mm",1e3)
        self.cb5T3.addItem("μm",1e6)
        self.cb5T3.addItem("nm",1e9)

        self.cb6T3 = QComboBox(self)
        self.cb6T3.addItem("m",  1)
        self.cb6T3.addItem("cm", 1e2)
        self.cb6T3.addItem("mm", 1e3)
        self.cb6T3.addItem("μm", 1e6)
        self.cb6T3.addItem("nm", 1e9)

        self.cb7T3 = QComboBox(self)
        self.cb7T3.addItem("m\u00b2", 1)

        self.TET2 = QTextEdit(self)
        self.TET2.setMaximumSize(200,30)
        self.TET2.setReadOnly(True)
        self.TE2T2 = QTextEdit(self)
        self.TE2T2.setMaximumSize(200,30)
        self.TE2T2.setReadOnly(True)
        self.TE3T2 = QTextEdit(self)
        self.TE3T2.setMaximumSize(200,30)
        self.TE3T2.setReadOnly(True)

        vbox3.addWidget(self.T3Q,   1,0)
        vbox3.addWidget(self.T3Q2,  2,0)
        vbox3.addWidget(self.T3Q3,  3,0)
        vbox3.addWidget(self.T3Q4,  4,0)
        vbox3.addWidget(self.T3Q5,  5,0)
        vbox3.addWidget(self.T3Q6,  6,0)
        vbox3.addWidget(self.T3Q7,  7,0)
        vbox3.addWidget(self.LET3,  1,1)
        vbox3.addWidget(self.LE2T3, 2,1)
        vbox3.addWidget(self.LE3T3, 3,1)
        vbox3.addWidget(self.LE4T3, 4,1)
        vbox3.addWidget(self.cb1T3, 1,2)
        vbox3.addWidget(self.cb2T3, 2,2)
        vbox3.addWidget(self.cb3T3, 3,2)
        vbox3.addWidget(self.cb4T3, 4,2)
        vbox3.addWidget(self.cb5T3, 5,2)
        vbox3.addWidget(self.cb6T3, 6,2)
        vbox3.addWidget(self.cb7T3, 7,2)
        vbox3.addWidget(self.TET2,  5,1)
        vbox3.addWidget(self.TE2T2,  6,1)
        vbox3.addWidget(self.TE3T2,  7,1)
        vbox3.addWidget(self.PB3,    8,0)

        self.tab3.setLayout(vbox3)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        self.submit2()

        #'submit' trigger conditions for tab 1
        self.line_edit1.editingFinished.connect(self.EnterPressed)
        self.line_edit2.editingFinished.connect(self.EnterPressed)
        self.line_edit3.editingFinished.connect(self.EnterPressed)
        self.line_edit4.editingFinished.connect(self.EnterPressed)
        self.combobox.currentIndexChanged.connect(self.EnterPressed)
        self.combobox2.currentIndexChanged.connect(self.EnterPressed)
        self.combobox3.currentIndexChanged.connect(self.EnterPressed)
        self.combobox4.currentIndexChanged.connect(self.EnterPressed)
        self.combobox6.currentIndexChanged.connect(self.EnterPressed)
        self.combobox7.currentIndexChanged.connect(self.EnterPressed)
        self.combobox8.currentIndexChanged.connect(self.EnterPressed)
        self.combobox9.currentIndexChanged.connect(self.EnterPressed)
        self.combobox10.currentIndexChanged.connect(self.EnterPressed)
        self.combobox11.currentIndexChanged.connect(self.EnterPressed)
        self.combobox12.currentIndexChanged.connect(self.EnterPressed)

        #'submit' trigger conditions for tab 2
        self.comboboxA.currentIndexChanged.connect(self.EnterPressed)
        self.combobox2A.currentIndexChanged.connect(self.EnterPressed)
        self.combobox3A.currentIndexChanged.connect(self.EnterPressed)
        self.line_edit1A.editingFinished.connect(self.EnterPressed)
        self.line_editT2.editingFinished.connect(self.EnterPressed)
        self.line_edit2A.editingFinished.connect(self.EnterPressed)
        self.line_edit3A.editingFinished.connect(self.EnterPressed)
        self.line_edit2T2.editingFinished.connect(self.EnterPressed)
        self.line_edit3T2.editingFinished.connect(self.EnterPressed)
        self.cb1T2.currentIndexChanged.connect(self.EnterPressed)
        self.cb2T2.currentIndexChanged.connect(self.EnterPressed)
        self.c3T2.currentIndexChanged.connect(self.EnterPressed)
        self.c4T2.currentIndexChanged.connect(self.EnterPressed)

        #'submit' trigger conditions for tab 3
        self.LET3.editingFinished.connect(self.EnterPressed)
        self.LE2T3.editingFinished.connect(self.EnterPressed)
        self.LE3T3.editingFinished.connect(self.EnterPressed)
        self.LE4T3.editingFinished.connect(self.EnterPressed)
        self.cb1T3.currentIndexChanged.connect(self.EnterPressed)
        self.cb2T3.currentIndexChanged.connect(self.EnterPressed)
        self.cb3T3.currentIndexChanged.connect(self.EnterPressed)
        self.cb5T3.currentIndexChanged.connect(self.EnterPressed)
        self.cb6T3.currentIndexChanged.connect(self.EnterPressed)
        self.cb7T3.currentIndexChanged.connect(self.EnterPressed)

        self.Checkbox.clicked.connect(self.submit2)

        self.PB1.clicked.connect(self.Button1Push)
        self.PB2.clicked.connect(self.Button2Push)
        self.PB3.clicked.connect(self.Button3Push)

    def submit2(self):
        if self.Checkbox.isChecked():
            self.le1.show()
            self.label2.show()
            self.le2.show()
            self.label3.show()
            self.le3.show()
            self.label4.show()
            self.le4.show()
            self.label5.show()
            self.le5.show()
            self.label6.show()
            self.label7.show()
            self.combobox9.show()
            self.combobox10.show()
            self.combobox11.show()
            self.combobox12.show()

        else:
            self.le1.hide()
            self.label2.hide()
            self.le2.hide()
            self.label3.hide()
            self.le3.hide()
            self.label4.hide()
            self.le4.hide()
            self.label5.hide()
            self.le5.hide()
            self.label6.hide()
            self.label7.hide()
            self.combobox9.hide()
            self.combobox10.hide()
            self.combobox11.hide()
            self.combobox12.hide()

    def Button1Push(self):
        PB1Window.show()

    def Button2Push(self):
        print("Button2Push")

    def Button3Push(self):
        print("Button3Push")

    def EnterPressed(self): #Calculations and whatnot, all done using one defined command, definitely not optimal
        Power = float((self.line_edit1.text()))*(self.combobox.itemData(int(self.combobox.currentIndex())))
        SpotDiameter = float((self.line_edit2.text()))*(self.combobox2.itemData(int(self.combobox2.currentIndex())))
        Rep_rate = float((self.line_edit3.text()))*(self.combobox3.itemData(int(self.combobox3.currentIndex())))
        Pulse_FWHM = float((self.line_edit4.text()))*(self.combobox4.itemData(int(self.combobox4.currentIndex())))
        self.line_Text.setPlainText(f"{((Power/Rep_rate)*(self.combobox7.itemData(int(self.combobox7.currentIndex())))):.3g}")   #Energy per pulse
        self.line_Text2.setPlainText(f"{(((SpotDiameter/2)**2)*np.pi)*(self.combobox8.itemData(int(self.combobox8.currentIndex())))**2:.3g}") #Beam area
        self.line_Text3.setPlainText(f"{((Power/Rep_rate)/(((SpotDiameter/2)**2)*np.pi))*2*(self.combobox6.itemData(int(self.combobox6.currentIndex()))):.3g}") #Fluence
        self.le1.setPlainText(f"{(((Power/Rep_rate))/Pulse_FWHM)*(self.combobox10.itemData(int(self.combobox10.currentIndex()))):.3g}") #Pulse energy
        self.le2.setPlainText(f"{(Power/(((SpotDiameter/2)**2)*np.pi))*2*(self.combobox11.itemData(int(self.combobox11.currentIndex()))):.3g}") #Peak Power
        self.le3.setPlainText(f"{(Power/((((SpotDiameter/2)**2)*np.pi)*Pulse_FWHM*Rep_rate))*2*(self.combobox9.itemData(int(self.combobox9.currentIndex()))):.3g}") #Peak intensity
        self.le4.setPlainText(f"{(1/Rep_rate)*(self.combobox12.itemData(int(self.combobox12.currentIndex()))):.3g}") #Pulse separation
        self.le5.setPlainText(f"{Pulse_FWHM*Rep_rate:.3g}") #Duty cycle

        PowerT2 = float((self.line_edit1A.text()))*(self.comboboxA.itemData(int(self.comboboxA.currentIndex())))
        SpotDiameterT2 = float((self.line_edit2A.text()))*(self.combobox2A.itemData(int(self.combobox2A.currentIndex())))
        Rep_rateT2 = float((self.line_edit3A.text()))*(self.combobox3A.itemData(int(self.combobox3A.currentIndex())))
        ODT2 = float(self.line_editT2.text())
        ExcitingPulseT2 = float(self.line_edit2T2.text()*self.cb1T2.itemData(int(self.cb1T2.currentIndex())))
        # FT2 = float((self.line_edit3T2.text())*(self.cb2T2.itemData(int(self.cb2T2.currentIndex()))))
        FT2 = float(float(self.line_edit3T2.text())*self.cb2T2.itemData(int(self.cb2T2.currentIndex())))
        Fluence = (PowerT2/Rep_rateT2)*2/(((SpotDiameterT2/2)**2)*np.pi) #J/m2
        ExDen = Fluence*ExcitingPulseT2*(1-10**-ODT2)/(6.626e-34*2.998e+8*FT2)
        self.line_edit4T2.setPlainText(f"{ExDen:.4g}")

        SpotDiameter3 = float((self.LE3T3.text()))*(self.cb3T3.itemData(int(self.cb3T3.currentIndex())))
        M = float(self.LE4T3.text())
        LightWavelength = float((self.LET3.text()))*(self.cb1T3.itemData(int(self.cb1T3.currentIndex())))
        FocalLength = float((self.LE2T3.text()))*(self.cb2T3.itemData(int(self.cb2T3.currentIndex())))
        SpotSizeAtFocal=(4*FocalLength*LightWavelength*M)/(np.pi*SpotDiameter3)*self.cb5T3.itemData(int(self.cb5T3.currentIndex()))
        self.TET2.setPlainText(f"{SpotSizeAtFocal:.3g}")
        SpotSizeAtFocalP=(4*FocalLength*LightWavelength*M)/(np.pi*SpotDiameter3)
        self.TE2T2.setPlainText(f"{((np.pi*(SpotSizeAtFocalP**2))/(LightWavelength*M))*self.cb6T3.itemData(int(self.cb6T3.currentIndex())):.3g}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())