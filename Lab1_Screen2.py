# Form implementation generated from reading ui file 'Lab1_Screen2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow12(object):
    def setupUi(self, MainWindow12):
        MainWindow12.setObjectName("MainWindow12")
        MainWindow12.resize(300, 450)
        MainWindow12.setMinimumSize(QtCore.QSize(300, 450))
        MainWindow12.setMaximumSize(QtCore.QSize(300, 450))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow12)
        self.centralwidget.setObjectName("centralwidget")
        self.label_header2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_header2.setGeometry(QtCore.QRect(30, 50, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_header2.setFont(font)
        self.label_header2.setObjectName("label_header2")
        self.label_cameron = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cameron.setGeometry(QtCore.QRect(40, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cameron.setFont(font)
        self.label_cameron.setObjectName("label_cameron")
        self.label_allison = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_allison.setGeometry(QtCore.QRect(40, 200, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_allison.setFont(font)
        self.label_allison.setObjectName("label_allison")
        self.label_diego = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_diego.setGeometry(QtCore.QRect(40, 240, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_diego.setFont(font)
        self.label_diego.setObjectName("label_diego")
        self.button_add_cameron = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_add_cameron.setGeometry(QtCore.QRect(130, 160, 51, 23))
        self.button_add_cameron.setObjectName("button_add_cameron")
        self.button_add_allison = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_add_allison.setGeometry(QtCore.QRect(130, 200, 51, 23))
        self.button_add_allison.setObjectName("button_add_allison")
        self.button_add_diego = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_add_diego.setGeometry(QtCore.QRect(130, 240, 51, 23))
        self.button_add_diego.setObjectName("button_add_diego")
        self.button_sub_cameron = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_sub_cameron.setGeometry(QtCore.QRect(200, 160, 51, 23))
        self.button_sub_cameron.setObjectName("button_sub_cameron")
        self.button_sub_allison = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_sub_allison.setGeometry(QtCore.QRect(200, 200, 51, 23))
        self.button_sub_allison.setObjectName("button_sub_allison")
        self.button_sub_diego = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_sub_diego.setGeometry(QtCore.QRect(200, 240, 51, 23))
        self.button_sub_diego.setObjectName("button_sub_diego")
        self.button_finish_voting = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_finish_voting.setGeometry(QtCore.QRect(100, 330, 75, 23))
        self.button_finish_voting.setObjectName("button_finish_voting")
        MainWindow12.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow12)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow12.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow12)
        self.statusbar.setObjectName("statusbar")
        MainWindow12.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow12)
        QtCore.QMetaObject.connectSlotsByName(MainWindow12)

    def retranslateUi(self, MainWindow12):
        _translate = QtCore.QCoreApplication.translate
        MainWindow12.setWindowTitle(_translate("MainWindow12", "MainWindow"))
        self.label_header2.setText(_translate("MainWindow12", "CANDIDATE MENU"))
        self.label_cameron.setText(_translate("MainWindow12", "Cameron"))
        self.label_allison.setText(_translate("MainWindow12", "Allison"))
        self.label_diego.setText(_translate("MainWindow12", "Diego"))
        self.button_add_cameron.setText(_translate("MainWindow12", "Add"))
        self.button_add_allison.setText(_translate("MainWindow12", "Add"))
        self.button_add_diego.setText(_translate("MainWindow12", "Add"))
        self.button_sub_cameron.setText(_translate("MainWindow12", "Sub"))
        self.button_sub_allison.setText(_translate("MainWindow12", "Sub"))
        self.button_sub_diego.setText(_translate("MainWindow12", "Sub"))
        self.button_finish_voting.setText(_translate("MainWindow12", "Finish Voting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow12 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow12()
    ui.setupUi(MainWindow12)
    MainWindow12.show()
    sys.exit(app.exec())
