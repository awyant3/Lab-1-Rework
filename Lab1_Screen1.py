# Form implementation generated from reading ui file 'Lab1_Screen1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow11(object):
    def setupUi(self, MainWindow11):
        MainWindow11.setObjectName("MainWindow11")
        MainWindow11.resize(300, 450)
        MainWindow11.setMinimumSize(QtCore.QSize(300, 450))
        MainWindow11.setMaximumSize(QtCore.QSize(300, 450))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow11)
        self.centralwidget.setObjectName("centralwidget")
        self.button_vote = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_vote.setGeometry(QtCore.QRect(110, 200, 75, 23))
        self.button_vote.setObjectName("button_vote")
        self.button_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.button_exit.setObjectName("button_exit")
        self.label_header1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_header1.setGeometry(QtCore.QRect(80, 50, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_header1.setFont(font)
        self.label_header1.setObjectName("label_header1")
        MainWindow11.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow11)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow11.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow11)
        self.statusbar.setObjectName("statusbar")
        MainWindow11.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow11)
        QtCore.QMetaObject.connectSlotsByName(MainWindow11)

    def retranslateUi(self, MainWindow11):
        _translate = QtCore.QCoreApplication.translate
        MainWindow11.setWindowTitle(_translate("MainWindow11", "MainWindow"))
        self.button_vote.setText(_translate("MainWindow11", "Vote"))
        self.button_exit.setText(_translate("MainWindow11", "Exit"))
        self.label_header1.setText(_translate("MainWindow11", "VOTE MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow11 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow11()
    ui.setupUi(MainWindow11)
    MainWindow11.show()
    sys.exit(app.exec())
