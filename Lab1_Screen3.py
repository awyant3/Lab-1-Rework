# Form implementation generated from reading ui file 'Lab1_Screen3.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow13(object):
    def setupUi(self, MainWindow13):
        MainWindow13.setObjectName("MainWindow13")
        MainWindow13.resize(300, 450)
        MainWindow13.setMinimumSize(QtCore.QSize(300, 450))
        MainWindow13.setMaximumSize(QtCore.QSize(300, 450))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow13)
        self.centralwidget.setObjectName("centralwidget")
        self.label_header3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_header3.setGeometry(QtCore.QRect(30, 40, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_header3.setFont(font)
        self.label_header3.setObjectName("label_header3")
        self.label_cameron_s3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cameron_s3.setGeometry(QtCore.QRect(30, 140, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cameron_s3.setFont(font)
        self.label_cameron_s3.setObjectName("label_cameron_s3")
        self.label_allison_s3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_allison_s3.setGeometry(QtCore.QRect(30, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_allison_s3.setFont(font)
        self.label_allison_s3.setObjectName("label_allison_s3")
        self.label_diego_s3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_diego_s3.setGeometry(QtCore.QRect(30, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_diego_s3.setFont(font)
        self.label_diego_s3.setObjectName("label_diego_s3")
        self.label_cameron_result = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cameron_result.setGeometry(QtCore.QRect(180, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cameron_result.setFont(font)
        self.label_cameron_result.setObjectName("label_cameron_result")
        self.label_allison_result_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_allison_result_2.setGeometry(QtCore.QRect(180, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_allison_result_2.setFont(font)
        self.label_allison_result_2.setObjectName("label_allison_result_2")
        self.label_diego_result_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_diego_result_3.setGeometry(QtCore.QRect(180, 220, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_diego_result_3.setFont(font)
        self.label_diego_result_3.setObjectName("label_diego_result_3")
        self.button_save_election = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_save_election.setGeometry(QtCore.QRect(110, 330, 75, 23))
        self.button_save_election.setObjectName("button_save_election")
        MainWindow13.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow13)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow13.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow13)
        self.statusbar.setObjectName("statusbar")
        MainWindow13.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow13)
        QtCore.QMetaObject.connectSlotsByName(MainWindow13)

    def retranslateUi(self, MainWindow13):
        _translate = QtCore.QCoreApplication.translate
        MainWindow13.setWindowTitle(_translate("MainWindow13", "MainWindow"))
        self.label_header3.setText(_translate("MainWindow13", "ELECTION RESULTS"))
        self.label_cameron_s3.setText(_translate("MainWindow13", "Cameron"))
        self.label_allison_s3.setText(_translate("MainWindow13", "Allison"))
        self.label_diego_s3.setText(_translate("MainWindow13", "Diego"))
        self.label_cameron_result.setText(_translate("MainWindow13", "0"))
        self.label_allison_result_2.setText(_translate("MainWindow13", "0"))
        self.label_diego_result_3.setText(_translate("MainWindow13", "0"))
        self.button_save_election.setText(_translate("MainWindow13", "Save Election"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow13 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow13()
    ui.setupUi(MainWindow13)
    MainWindow13.show()
    sys.exit(app.exec())
