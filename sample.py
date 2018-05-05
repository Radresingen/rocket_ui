# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 781, 191))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lcdNumber_4 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_4.setObjectName(_fromUtf8("lcdNumber_4"))
        self.horizontalLayout.addWidget(self.lcdNumber_4)
        self.lcdNumber_3 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.horizontalLayout.addWidget(self.lcdNumber_3)
        self.lcdNumber_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.horizontalLayout.addWidget(self.lcdNumber_2)
        self.lcdNumber = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 470, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 470, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 310, 117, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 340, 117, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 370, 117, 22))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(50, 400, 117, 22))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 781, 80))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_4 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "ROCKET_UI", None))
        self.pushButton.setText(_translate("mainWindow", "STOP", None))
        self.pushButton_2.setText(_translate("mainWindow", "START", None))
        self.radioButton.setText(_translate("mainWindow", "VALVE 1", None))
        self.radioButton_2.setText(_translate("mainWindow", "VALVE 2", None))
        self.radioButton_3.setText(_translate("mainWindow", "VALVE 3", None))
        self.radioButton_4.setText(_translate("mainWindow", "VALVE 4", None))
        self.lineEdit_4.setText(_translate("mainWindow", "                    KM/H", None))
        self.lineEdit_3.setText(_translate("mainWindow", "                  ALTITUDE", None))
        self.lineEdit_2.setText(_translate("mainWindow", "                   EMPTY", None))
        self.lineEdit.setText(_translate("mainWindow", "                    EMPTY", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

