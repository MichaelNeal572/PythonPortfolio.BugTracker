import sys
from PyQt5 import QtCore, QtWidgets
import dashboard
import login

class LoginW:
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        self.window = login.QtWidgets.QMainWindow()
        self.ui = login.Ui_LoginW()
        self.ui.setupUi(self.window)
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.btnExit.clicked.connect(self.gotoDashboard)

    def gotoDashboard(self):
        self.switch_window.emit()
        self.close()

class DashboardW:
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        self.window = dashboard.QtWidgets.QMainWindow()
        self.ui = dashboard.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.connect_buttons()

    def connect_buttons(self):
        #self.ui.actLogOut.clicked.connect(self.gotoLogin)
        pass

    def gotoLogin(self):
        self.switch_window.emit()
        self.close()

class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login = LoginW()
        self.login.switch_window.connect(self.show_dashboard)
        self.login.window.show()

    def show_dashboard(self):
        self.dashboard = DashboardW()
        self.dashboard.switch_window.connect(self.show_login)
        self.dashboard.window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()