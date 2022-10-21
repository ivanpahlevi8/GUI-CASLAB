# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gui3 import Ui_SecondWindow as Main
from dialog1 import Ui_Dialog1 as Dialog1
from dialog2 import Ui_Dialog2 as Dialog2
import sys


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                self.firstWindow = MainWindow
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(997, 737)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(70, 10, 851, 121))
                self.label.setStyleSheet("font: 87 46pt \"Arial Black\";\n"
                "background-color: rgb(187, 183, 200);\n"
                "border-radius: 20px;\n"
                "")
                self.label.setTextFormat(QtCore.Qt.AutoText)
                self.label.setWordWrap(False)
                self.label.setObjectName("label")

                #Username input segment
                self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
                self.usernameInput.setGeometry(QtCore.QRect(470, 280, 251, 41))
                self.usernameInput.setStyleSheet("border: 2px solid rgb(37, 49, 46);\n"
                "border-radius: 20px;\n"
                "font: 18pt \"Arial\";\n"
                "color: Black;\n"
                "padding-left: 20px;\n"
                "padding-right: 20px;\n"
                "background-color: rgb(187, 183, 200);")
                self.usernameInput.setObjectName("usernameInput")

                #Password input segment
                self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
                self.passwordInput.setGeometry(QtCore.QRect(470, 380, 251, 41))
                self.passwordInput.setStyleSheet("border: 2px solid rgb(37, 49, 46);\n"
                "border-radius: 20px;\n"
                "font: 18pt \"Arial\";\n"
                "color: Black;\n"
                "padding-left: 20px;\n"
                "padding-right: 20px;\n"
                "background-color: rgb(187, 183, 200);")
                self.passwordInput.setObjectName("passwordInput")
                
                # Login Button Segment
                self.loginButton = QtWidgets.QPushButton(self.centralwidget)
                self.loginButton.setGeometry(QtCore.QRect(440, 510, 131, 51))
                self.loginButton.setStyleSheet("font: 24pt \"Arial\";\n"
                "border: 3px solid black;\n"
                "border-radius: 15px;\n"
                "background-color: cyan;")
                self.loginButton.setObjectName("loginButton")
                self.loginButton.clicked.connect(self.opeWindow)

                #Username Label Segment
                self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
                self.usernameLabel.setGeometry(QtCore.QRect(300, 280, 151, 41))
                self.usernameLabel.setStyleSheet("font: 16pt \"Arial\";\n"
                "border: 2px solid black;\n"
                "border-radius: 12px;")
                self.usernameLabel.setObjectName("usernameLabel")
                self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
                self.passwordLabel.setGeometry(QtCore.QRect(300, 380, 151, 41))
                self.passwordLabel.setStyleSheet("font: 16pt \"Arial\";\n"
                "border: 2px solid black;\n"
                "border-radius: 12px;")
                self.passwordLabel.setObjectName("passwordLabel")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "Group GUI Program"))
                self.loginButton.setText(_translate("MainWindow", "Login"))
                self.usernameLabel.setText(_translate("MainWindow", "Username :"))
                self.passwordLabel.setText(_translate("MainWindow", "Password :"))

        def opeWindow(self):
                if self.usernameInput.text() == "ivanpahlevi8" and self.passwordInput.text() == "ivan":
                        self.showDialog()
                        self.myDialog1.Window = self.firstWindow
                        self.w = Main()
                        self.myDialog1.SecondWindow = self.w
                else :
                        self.showDialog2()

        
        def showDialog(self):
                self.dialogWindow = QtWidgets.QDialog()
                self.myDialog1 = Dialog1()
                self.myDialog1.setupUi(self.dialogWindow)
                self.dialogWindow.show()
        
        def showDialog2(self):
                self.dialogWindow2 = QtWidgets.QDialog()
                self.myDialog2 = Dialog2()
                self.myDialog2.setupUi(self.dialogWindow2)
                self.dialogWindow2.show()
                


if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
