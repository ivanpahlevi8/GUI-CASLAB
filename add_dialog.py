# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add-daialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtGui, QtWidgets
from add_main import Ui_MainWindow_Add


class Ui_Dialog_Daftar(object):
    def setupUi(self, Dialog):
        self.myDialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(352, 294)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonOnClickListener)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 211))
        self.label.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.windowMain = NULL
        self.studentsOnAddDialog = NULL

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Daftar"))
        self.label.setText(_translate("Dialog", "Wajah tidak\n"
"terdeteksi berada pada\n"
"database mahasiswa. \n"
"\n"
"Tekan tombol daftar\n"
"dibawah untuk \n"
"menambahkan ke database!"))

    def buttonOnClickListener(self):
        self.main = Ui_MainWindow_Add()
        self.MainWin = QtWidgets.QMainWindow()
        self.main.setupUi(self.MainWin)
        self.main.studentsOnAddWindow = self.studentsOnAddDialog
        self.myDialog.close()
        self.windowMain.hide()
        self.main.absenWindow = self.windowMain
        self.MainWin.show()


