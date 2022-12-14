# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rule_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtGui, QtWidgets
from gui3 import Ui_SecondWindow as absenWindow
from add_main import Ui_MainWindow_Add as daftarWindow


class Ui_MainWindow_Rule(object):
        def setupUi(self, MainWindow):
                self.myWindow = MainWindow
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(882, 731)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")

                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(50, 40, 811, 71))
                self.label.setStyleSheet("font: 87 22pt \"Arial Black\";\n"
                "border: 2px solid;\n"
                "border-radius: 7px;")
                self.label.setObjectName("label")

                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(50, 180, 781, 81))
                self.label_2.setStyleSheet("font: 16pt \"Arial\";")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)

                self.label_3.setGeometry(QtCore.QRect(50, 270, 781, 81))
                self.label_3.setStyleSheet("font: 16pt \"Arial\";")
                self.label_3.setObjectName("label_3")

                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(50, 370, 811, 131))
                self.label_4.setStyleSheet("font: 16pt \"Arial\";")
                self.label_4.setObjectName("label_4")

                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(50, 510, 781, 81))
                self.label_5.setStyleSheet("font: 16pt \"Arial\";")
                self.label_5.setObjectName("label_5")

                # Push Button for absen segment
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(300, 620, 93, 28))
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.absenButtonOnClickListener)

                #Push Button For Daftar segment
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(470, 620, 93, 28))
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_2.clicked.connect(self.daftarButtonOnClickListener)

                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.daftarLayout = NULL
                self.absenLayout = NULL

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "Face Recognition Attendance Program"))
                self.label_2.setText(_translate("MainWindow", "1. Program ini digunakan untuk mengabsen mahasiswa dengan \n"
                "    menggunakan muka mereka"))
                self.label_3.setText(_translate("MainWindow", "2. Absen dapat dilakukan apabila data mahasiswa telah terdaftar pada program\n"
                "    dengan menekan tombol \"absen\""))
                self.label_4.setText(_translate("MainWindow", "3. Apabila belum terdaftar silahkan mendaftar dengan menekan \n"
                "    tombol \"daftar\" lalu lengkapi semua data yang diperlukan. Tekan \n"
                "    tombol submit ketika data sudah terisi untuk menyimpan data dan \n"
                "    mengambil foto"))
                self.label_5.setText(_translate("MainWindow", "4. Selamat menggunakan!"))
                self.pushButton.setText(_translate("MainWindow", "Absen"))
                self.pushButton_2.setText(_translate("MainWindow", "Daftar"))

        def absenButtonOnClickListener(self):
                MainWindow = QtWidgets.QMainWindow()
                self.absenLayout.setupUi(MainWindow)
                MainWindow.show()
                self.myWindow.close()

        def daftarButtonOnClickListener(self):
                MainWindow = QtWidgets.QMainWindow()
                self.daftarLayout.setupUi(MainWindow)
                self.myWindow.close()
                MainWindow.show()




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
