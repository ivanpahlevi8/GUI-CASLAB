# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        self.myDialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(268, 215)
        self.infoLabel = QtWidgets.QLabel(Dialog)
        self.infoLabel.setGeometry(QtCore.QRect(10, 40, 251, 41))
        self.infoLabel.setStyleSheet("font: 75 18pt \"Arial\";\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.infoLabel.setObjectName("infoLabel")
        self.infoButton = QtWidgets.QPushButton(Dialog)
        self.infoButton.setGeometry(QtCore.QRect(80, 150, 93, 28))
        self.infoButton.setObjectName("infoButton")
        self.infoButton.clicked.connect(self.functionOkay)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Ok = False
        self.Window = NULL
        self.SecondWindow = NULL
        self.absen = NULL
        self.daftar = NULL

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.infoLabel.setText(_translate("Dialog", "Login Success"))
        self.infoButton.setText(_translate("Dialog", "OKAYY"))
    
    def functionOkay(self):
        self.Ok = True
        self.myDialog.close()
        self.Window.close()
        self.MainWin = QtWidgets.QMainWindow()
        self.SecondWindow.setupUi(self.MainWin)
        self.SecondWindow.daftarLayout = self.daftar
        self.SecondWindow.absenLayout = self.absen
        self.MainWin.show()

