# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Michael\Documents\GitHub\PythonPortfolio.BugTracker\PythonPortfolio.BugTracker\Admin Tools\Python\Support Classes\login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginW(object):
    def setupUi(self, LoginW):
        LoginW.setObjectName("LoginW")
        LoginW.resize(310, 202)
        LoginW.setMinimumSize(QtCore.QSize(310, 202))
        LoginW.setMaximumSize(QtCore.QSize(310, 202))
        self.centralwidget = QtWidgets.QWidget(LoginW)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txtUsername.setObjectName("txtUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtUsername)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txtPassword.setInputMask("")
        self.txtPassword.setText("")
        self.txtPassword.setMaxLength(32767)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtPassword)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnExit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout.addWidget(self.btnExit)
        self.btnLogin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout.addWidget(self.btnLogin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        LoginW.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginW)
        QtCore.QMetaObject.connectSlotsByName(LoginW)
        LoginW.setTabOrder(self.txtUsername, self.txtPassword)
        LoginW.setTabOrder(self.txtPassword, self.btnExit)
        LoginW.setTabOrder(self.btnExit, self.btnLogin)

    def retranslateUi(self, LoginW):
        _translate = QtCore.QCoreApplication.translate
        LoginW.setWindowTitle(_translate("LoginW", "BugTracker Admin Login"))
        self.label_3.setText(_translate("LoginW", "Login"))
        self.label.setText(_translate("LoginW", "Username: "))
        self.txtUsername.setWhatsThis(_translate("LoginW", "<html><head/><body><p>Please insert Username</p></body></html>"))
        self.txtUsername.setPlaceholderText(_translate("LoginW", "Username"))
        self.label_2.setText(_translate("LoginW", "Password: "))
        self.txtPassword.setWhatsThis(_translate("LoginW", "<html><head/><body><p>Please insert Password</p></body></html>"))
        self.txtPassword.setPlaceholderText(_translate("LoginW", "Password"))
        self.btnExit.setText(_translate("LoginW", "Exit"))
        self.btnLogin.setText(_translate("LoginW", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginW = QtWidgets.QMainWindow()
    ui = Ui_LoginW()
    ui.setupUi(LoginW)
    LoginW.show()
    sys.exit(app.exec_())

