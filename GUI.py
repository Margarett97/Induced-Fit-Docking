# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QLineEdit, QFileDialog
from PyQt5.uic import loadUi
from back import Ui_Second

if os.path.exists("parameters.py"):
  os.remove("parameters.py")

class Ui_First(object):
    
    def openWindow(self):
        
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Second()
        self.ui.setupUi(self.window)
        First.close()
        self.window.show()
        
    def setupUi(self, First):
        First.setObjectName("First")
        First.resize(335, 136)
        font = QtGui.QFont()
        font.setPointSize(28)
        First.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(First)
        self.gridLayout.setObjectName("gridLayout")
        self.Ch_path = QtWidgets.QLineEdit(First)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Ch_path.setFont(font)
        self.Ch_path.setObjectName("Ch_path")
        self.gridLayout.addWidget(self.Ch_path, 2, 1, 1, 2)
        self.Exit_Button = QtWidgets.QPushButton(First)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Exit_Button.setFont(font)
        self.Exit_Button.setObjectName("Exit_Button")
        self.gridLayout.addWidget(self.Exit_Button, 5, 2, 1, 2)
        self.ag_name = QtWidgets.QLabel(First)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ag_name.setFont(font)
        self.ag_name.setObjectName("ag_name")
        self.gridLayout.addWidget(self.ag_name, 3, 0, 1, 1)
        self.AG_path = QtWidgets.QLineEdit(First)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AG_path.setFont(font)
        self.AG_path.setObjectName("AG_path")
        self.gridLayout.addWidget(self.AG_path, 3, 1, 1, 2)
        self.next_Button = QtWidgets.QPushButton(First)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.next_Button.setFont(font)
        self.next_Button.setObjectName("next_Button")
        self.gridLayout.addWidget(self.next_Button, 5, 1, 1, 1)
        self.ch_name = QtWidgets.QLabel(First)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ch_name.setFont(font)
        self.ch_name.setObjectName("ch_name")
        self.gridLayout.addWidget(self.ch_name, 2, 0, 1, 1)
        self.ad_name = QtWidgets.QLabel(First)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ad_name.setFont(font)
        self.ad_name.setObjectName("ad_name")
        self.gridLayout.addWidget(self.ad_name, 4, 0, 1, 1)
        self.CH_path_button = QtWidgets.QToolButton(First)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CH_path_button.setFont(font)
        self.CH_path_button.setObjectName("CH_path_button")
        self.gridLayout.addWidget(self.CH_path_button, 2, 3, 1, 1)
        self.AD_path_button = QtWidgets.QToolButton(First)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AD_path_button.setFont(font)
        self.AD_path_button.setObjectName("AD_path_button")
        self.gridLayout.addWidget(self.AD_path_button, 4, 3, 1, 1)
        self.AG_path_button = QtWidgets.QToolButton(First)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AG_path_button.setFont(font)
        self.AG_path_button.setObjectName("AG_path_button")
        self.gridLayout.addWidget(self.AG_path_button, 3, 3, 1, 1)
        self.AD_path = QtWidgets.QLineEdit(First)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AD_path.setFont(font)
        self.AD_path.setObjectName("AD_path")
        self.gridLayout.addWidget(self.AD_path, 4, 1, 1, 2)
        self.api_name = QtWidgets.QLabel(First)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 149, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 56, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 149, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 56, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 149, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 56, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.api_name.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        self.api_name.setFont(font)
        self.api_name.setMouseTracking(True)
        self.api_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.api_name.setTextFormat(QtCore.Qt.RichText)
        self.api_name.setScaledContents(False)
        self.api_name.setObjectName("api_name")
        self.gridLayout.addWidget(self.api_name, 1, 1, 1, 1)
        self.ch_name.raise_()
        self.ad_name.raise_()
        self.next_Button.raise_()
        self.Exit_Button.raise_()
        self.Ch_path.raise_()
        self.AG_path.raise_()
        self.AD_path.raise_()
        self.ag_name.raise_()
        self.CH_path_button.raise_()
        self.AD_path_button.raise_()
        self.AG_path_button.raise_()
        self.api_name.raise_()

        self.retranslateUi(First)
        QtCore.QMetaObject.connectSlotsByName(First)
        First.setTabOrder(self.Ch_path, self.AG_path)
        First.setTabOrder(self.AG_path, self.AD_path)
        First.setTabOrder(self.AD_path, self.next_Button)
        First.setTabOrder(self.next_Button, self.Exit_Button)

    def retranslateUi(self, First):
        _translate = QtCore.QCoreApplication.translate
        First.setWindowTitle(_translate("First", "Form"))
        self.Exit_Button.setText(_translate("First", "Exit"))
        self.ag_name.setText(_translate("First", "AutoGrid path:"))
        self.next_Button.setText(_translate("First", "Next"))
        self.ch_name.setText(_translate("First", "Chimera path:"))
        self.ad_name.setText(_translate("First", "AutoDock path:"))
        self.CH_path_button.setText(_translate("First", "..."))
        self.AD_path_button.setText(_translate("First", "..."))
        self.AG_path_button.setText(_translate("First", "..."))
        self.api_name.setText(_translate("First", "                                                            FitDock"))

        self.CH_path_button.clicked.connect(self.AddFilePath1)
        self.AG_path_button.clicked.connect(self.AddFilePath2)
        self.AD_path_button.clicked.connect(self.AddFilePath3)
        self.Exit_Button.clicked.connect(self.Exit)
        
        self.next_Button.clicked.connect(self.openWindow)

        

    def AddFilePath1(self):
        filename= QFileDialog.getOpenFileName()
        chimera_path = filename[0]
        self.Ch_path.setText(chimera_path)
        

        with open('parameters.py','a') as p:
            name="chimera_path='"
            p.write(name + chimera_path+"'\n")
        

    def AddFilePath2(self):
        filename= QFileDialog.getOpenFileName()
        grid_path = filename[0]
        self.AG_path.setText(grid_path)

        with open('parameters.py','a') as p:
            name="grid_path='"
            p.write(name + grid_path+"'\n")

    def AddFilePath3(self):
        filename= QFileDialog.getOpenFileName()
        dock_path = filename[0]
        self.AD_path.setText(dock_path)

        with open('parameters.py','a') as p:
            name="dock_path='"
            p.write(name + dock_path+"'\n")  

    def Exit(self):
        First.close()

 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    First = QtWidgets.QWidget()
    ui = Ui_First()
    ui.setupUi(First)
    First.show()
    sys.exit(app.exec_())