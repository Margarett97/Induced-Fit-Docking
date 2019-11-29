# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'back.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QLineEdit, QFileDialog
from PyQt5.uic import loadUi


class Ui_Second(object):
    def setupUi(self, Second):
        Second.setObjectName("Second")
        Second.resize(478, 269)
        self.gridLayout = QtWidgets.QGridLayout(Second)
        self.gridLayout.setObjectName("gridLayout")
        self.spacing_value = QtWidgets.QLineEdit(Second)
        self.spacing_value.setObjectName("spacing_value")
        self.gridLayout.addWidget(self.spacing_value, 14, 9, 1, 2)
        self.ReferenceButton = QtWidgets.QToolButton(Second)
        self.ReferenceButton.setObjectName("ReferenceButton")
        self.gridLayout.addWidget(self.ReferenceButton, 6, 5, 2, 1)
        self.z_value = QtWidgets.QLineEdit(Second)
        self.z_value.setObjectName("z_value")
        self.gridLayout.addWidget(self.z_value, 7, 10, 1, 1)
        self.x_value = QtWidgets.QLineEdit(Second)
        self.x_value.setObjectName("x_value")
        self.gridLayout.addWidget(self.x_value, 4, 10, 1, 1)
        self.y_center_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.y_center_name.setFont(font)
        self.y_center_name.setObjectName("y_center_name")
        self.gridLayout.addWidget(self.y_center_name, 5, 9, 1, 1)
        self.ligand_value = QtWidgets.QLineEdit(Second)
        self.ligand_value.setObjectName("ligand_value")
        self.gridLayout.addWidget(self.ligand_value, 9, 2, 2, 3)
        self.z_center_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.z_center_name.setFont(font)
        self.z_center_name.setObjectName("z_center_name")
        self.gridLayout.addWidget(self.z_center_name, 7, 9, 1, 1)
        self.y_value = QtWidgets.QLineEdit(Second)
        self.y_value.setObjectName("y_value")
        self.gridLayout.addWidget(self.y_value, 5, 10, 1, 1)
        self.z_dim_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.z_dim_name.setFont(font)
        self.z_dim_name.setObjectName("z_dim_name")
        self.gridLayout.addWidget(self.z_dim_name, 13, 9, 1, 1)
        self.PathButton = QtWidgets.QToolButton(Second)
        self.PathButton.setObjectName("PathButton")
        self.gridLayout.addWidget(self.PathButton, 2, 5, 2, 1)
        self.ReceptorButton = QtWidgets.QToolButton(Second)
        self.ReceptorButton.setObjectName("ReceptorButton")
        self.gridLayout.addWidget(self.ReceptorButton, 4, 5, 2, 1)
        self.spacing_label = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spacing_label.setFont(font)
        self.spacing_label.setObjectName("spacing_label")
        self.gridLayout.addWidget(self.spacing_label, 14, 7, 1, 2)
        self.path_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_name.setFont(font)
        self.path_name.setObjectName("path_name")
        self.gridLayout.addWidget(self.path_name, 2, 0, 2, 1)
        self.rec_chain_value = QtWidgets.QLineEdit(Second)
        self.rec_chain_value.setObjectName("rec_chain_value")
        self.gridLayout.addWidget(self.rec_chain_value, 11, 4, 1, 1)
        self.exit2_button = QtWidgets.QPushButton(Second)
        self.exit2_button.setObjectName("exit2_button")
        self.gridLayout.addWidget(self.exit2_button, 16, 10, 1, 1)
        self.x_dim_value = QtWidgets.QLineEdit(Second)
        self.x_dim_value.setObjectName("x_dim_value")
        self.gridLayout.addWidget(self.x_dim_value, 11, 10, 1, 1)
        self.y_dim_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.y_dim_name.setFont(font)
        self.y_dim_name.setObjectName("y_dim_name")
        self.gridLayout.addWidget(self.y_dim_name, 12, 9, 1, 1)
        self.x_center_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.x_center_name.setFont(font)
        self.x_center_name.setObjectName("x_center_name")
        self.gridLayout.addWidget(self.x_center_name, 4, 9, 1, 1)
        self.api_name = QtWidgets.QLabel(Second)
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
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.api_name.setFont(font)
        self.api_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.api_name.setObjectName("api_name")
        self.gridLayout.addWidget(self.api_name, 0, 0, 2, 11)
        self.y_dim_value = QtWidgets.QLineEdit(Second)
        self.y_dim_value.setObjectName("y_dim_value")
        self.gridLayout.addWidget(self.y_dim_value, 12, 10, 1, 1)
        self.OK_button = QtWidgets.QPushButton(Second)
        self.OK_button.setObjectName("OK_button")
        self.gridLayout.addWidget(self.OK_button, 16, 9, 1, 1)
        self.LigandButton = QtWidgets.QToolButton(Second)
        self.LigandButton.setObjectName("LigandButton")
        self.gridLayout.addWidget(self.LigandButton, 10, 5, 1, 1)
        self.z_dim_value = QtWidgets.QLineEdit(Second)
        self.z_dim_value.setObjectName("z_dim_value")
        self.gridLayout.addWidget(self.z_dim_value, 13, 10, 1, 1)
        self.ligand_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ligand_name.setFont(font)
        self.ligand_name.setObjectName("ligand_name")
        self.gridLayout.addWidget(self.ligand_name, 9, 0, 2, 2)
        self.path_value = QtWidgets.QLineEdit(Second)
        self.path_value.setObjectName("path_value")
        self.gridLayout.addWidget(self.path_value, 2, 1, 2, 4)
        self.x_dim_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.x_dim_name.setFont(font)
        self.x_dim_name.setObjectName("x_dim_name")
        self.gridLayout.addWidget(self.x_dim_name, 11, 9, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Second)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 15, 0, 1, 11)
        self.dim_label = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dim_label.setFont(font)
        self.dim_label.setObjectName("dim_label")
        self.gridLayout.addWidget(self.dim_label, 10, 8, 1, 2)
        self.lig_chamin_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lig_chamin_name.setFont(font)
        self.lig_chamin_name.setObjectName("lig_chamin_name")
        self.gridLayout.addWidget(self.lig_chamin_name, 12, 0, 2, 2)
        self.lig_chain_value = QtWidgets.QLineEdit(Second)
        self.lig_chain_value.setObjectName("lig_chain_value")
        self.gridLayout.addWidget(self.lig_chain_value, 12, 2, 2, 3)
        self.ref_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ref_name.setFont(font)
        self.ref_name.setObjectName("ref_name")
        self.gridLayout.addWidget(self.ref_name, 6, 0, 2, 2)
        self.ref_value = QtWidgets.QLineEdit(Second)
        self.ref_value.setObjectName("ref_value")
        self.gridLayout.addWidget(self.ref_value, 6, 2, 2, 3)
        self.receptor_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receptor_name.setFont(font)
        self.receptor_name.setObjectName("receptor_name")
        self.gridLayout.addWidget(self.receptor_name, 4, 0, 2, 2)
        self.receptor_value = QtWidgets.QLineEdit(Second)
        self.receptor_value.setObjectName("receptor_value")
        self.gridLayout.addWidget(self.receptor_value, 4, 2, 2, 3)
        self.rec_chain_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rec_chain_name.setFont(font)
        self.rec_chain_name.setObjectName("rec_chain_name")
        self.gridLayout.addWidget(self.rec_chain_name, 11, 0, 1, 3)
        self.grid_label = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grid_label.setFont(font)
        self.grid_label.setObjectName("grid_label")
        self.gridLayout.addWidget(self.grid_label, 2, 8, 1, 2)

        self.retranslateUi(Second)
        QtCore.QMetaObject.connectSlotsByName(Second)

    def retranslateUi(self, Second):
        _translate = QtCore.QCoreApplication.translate
        Second.setWindowTitle(_translate("Second", "Form"))
        self.ReferenceButton.setText(_translate("Second", "..."))
        self.y_center_name.setText(_translate("Second", "Y-center:"))
        self.z_center_name.setText(_translate("Second", "Z-center:"))
        self.z_dim_name.setText(_translate("Second", "Z-dimension:"))
        self.PathButton.setText(_translate("Second", "..."))
        self.ReceptorButton.setText(_translate("Second", "..."))
        self.spacing_label.setText(_translate("Second", "       Spacing:"))
        self.path_name.setText(_translate("Second", "Path:"))
        self.exit2_button.setText(_translate("Second", "Exit"))
        self.y_dim_name.setText(_translate("Second", "Y-dimension:"))
        self.x_center_name.setText(_translate("Second", "X-center:"))
        self.api_name.setText(_translate("Second", "         INDUCED FIT DOCKING"))
        self.OK_button.setText(_translate("Second", "OK"))
        self.LigandButton.setText(_translate("Second", "..."))
        self.ligand_name.setText(_translate("Second", "Ligand ID:"))
        self.x_dim_name.setText(_translate("Second", "X-dimension:"))
        self.dim_label.setText(_translate("Second", "Number of points in:"))
        self.lig_chamin_name.setText(_translate("Second", "Ligand chain:"))
        self.ref_name.setText(_translate("Second", "Referential ID:"))
        self.receptor_name.setText(_translate("Second", "Receptor ID:"))
        self.rec_chain_name.setText(_translate("Second", "Receptor chain to delete:"))
        self.grid_label.setText(_translate("Second", "Gridbox center:"))


        self.PathButton.clicked.connect(self.AddFilePath4)
        self.ReceptorButton.clicked.connect(self.ReceptorID)
        self.ReferenceButton.clicked.connect(self.ReferenceID)
        self.LigandButton.clicked.connect(self.LigandID)

        self.x_dim_value.setPlaceholderText('40')
        self.y_dim_value.setPlaceholderText('40')
        self.z_dim_value.setPlaceholderText('40')

        self.spacing_value.setPlaceholderText('0.375')

        

        self.OK_button.clicked.connect(self.OK)
        self.exit2_button.clicked.connect(self.Exit2)


    def AddFilePath4(self):
        work_dir= QFileDialog.getExistingDirectory()
        self.path_value.setText(work_dir)

        with open('parameters.py','a') as p:
            name="work_dir='"
            p.write(name + work_dir+"'\n")

    def ReceptorID(self):
        filename= QFileDialog.getOpenFileName()
        file =filename[0]
        folder, name = os.path.split(file)
        receptor, ext = os.path.splitext(name)
        self.receptor_value.setText(receptor)
        

        with open('parameters.py','a') as p:
            name="receptor='"
            p.write(name + receptor+"'\n")


    def ReferenceID(self):
        filename= QFileDialog.getOpenFileName()
        reference = filename[0]
        self.ref_value.setText(reference)

        with open('parameters.py','a') as p:
            name="reference='"
            p.write(name + reference+"'\n")

            
    def LigandID(self):
        filename= QFileDialog.getOpenFileName()
        file = filename[0]
        folder, name = os.path.split(file)
        ligand, ext = os.path.splitext(name)
        self.ligand_value.setText(ligand)

        with open('parameters.py','a') as p:
            name="ligand='"
            p.write(name + ligand+"'\n")



    def OK(self):
        
    
        chain_del_value=self.rec_chain_value.text()
        lig_chain_value=self.lig_chain_value.text()

        x=self.x_value.text()
        y=self.y_value.text()
        z=self.z_value.text()

        x_dim=self.x_dim_value.text()
        y_dim=self.y_dim_value.text()
        z_dim=self.z_dim_value.text()

        spacing=self.spacing_value.text()

        with open('parameters.py','a') as p:
            name="chain_del='"
            p.write(name + chain_del_value+"'\n")
            name="chain_lig='"
            p.write(name + lig_chain_value+"'\n")
            name="x="
            p.write(name + x+"\n")
            name="y="
            p.write(name + y+"\n")
            name="z="
            p.write(name + z+"\n")

            if x_dim!='' :
                name="x_dim='"
                p.write(name + x_dim+"'\n")
            elif y_dim!='':
                name="y_dim='"
                p.write(name + y_dim+"'\n")
            elif z_dim!='':
                name="z_dim='"
                p.write(name + z_dim+"'\n")
            elif spacing!='':
                name="spacing='"
                p.write(name+spacing+"'\n")

            else:
                name1="x_dim="
                p.write(name1 +"40\n")
                name2="y_dim="
                p.write(name2+"40\n")
                name3="z_dim="
                p.write(name3+"40\n")
                name4="spacing="
                p.write(name4+"0.375\n")
                

    def Exit2(self):
        Second.close()
        
        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Second = QtWidgets.QWidget()
    ui = Ui_Second()
    ui.setupUi(Second)
    Second.show()
    sys.exit(app.exec_())
