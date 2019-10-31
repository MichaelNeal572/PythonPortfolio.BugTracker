import sys
from PyQt5 import QtCore, QtWidgets
from SupportClasses import dashboard, login

class DatabaseConnector:
    def __init__(self):
        self.URL="http://192.168.8.201:1880/BugTrackerCRUD"

    def send(self, message):
        payload = {"statement":message}
        r = requests.post(self.URL, data=payload)
        response={
            "status_code":r.status_code,
            "reason":r.reason,
            "payload":r.text
        }
        return response["payload"]


class LoginW:
    def __init__(self):
        self.window = login.QtWidgets.QMainWindow()
        self.ui = login.Ui_LoginW()
        self.ui.setupUi(self.window)

    def get_fields(self):
        fields={
            "username":self.ui.txtUsername.text(),
            "password":self.ui.txtPassword.text()
        }

class DashboardW:
    def __init__(self):
        self.window = dashboard.QtWidgets.QMainWindow()
        self.ui = dashboard.Ui_MainWindow()
        self.ui.setupUi(self.window)

    def populate_fields_bugs(self):
        pass

    def get_fields_bugs(self):
        if (self.ui.rdoBugUnknown.isChecked()):
            resolution_temp="Unknown"
        elif(self.ui.rdoBugKnown.isChecked()):
            resolution_temp=self.ui.dteBugResolution.dateTime().toPyDateTime()
        fields={
            "details":self.ui.txtBugDetails.text(),
            "args":self.ui.txtBugArgs.text(),
            "kwargs":self.ui.txtBugKwargs.text(),
            "source":self.ui.txtBugSource.text(),
            "date_created":self.ui.deBugDateCreated.date().toPyDate(),
            "status":str(self.ui.cmbBugStatus.currentText()),
            "expected_resolution":resolution_temp
        }
        print(fields)

    def populate_fields_admins(self):
        pass

    def get_fields_admins(self):
        fields={
            "username":self.ui.txtAdminUserName.text(),
            "firstname":self.ui.txtAdminFirstName.text(),
            "lastname":self.ui.txtAdminLastName.text(),
            "password":self.ui.txtAdminPassword.text()
        }
        print(fields)

    def populate_fields_listeners(self):
        pass

    def get_fields_listeners(self):
        fields={
            "username":str(self.ui.cmbListenersUserName.currentText()),
            "bug_source":str(self.ui.cmbListenersBugSource.currentText())
        }
        print(fields)

    def populate_fields_backup(self):
        pass

    def get_fields_backup(self):
        fields={
            "listener":str(self.ui.cmbListener.currentText()),
            "backup":str(self.ui.cmbBackup.currentText())
        }
        print(fields)

class Controller:
    def __init__(self):
        self.dbc=DatabaseConnector()

        self.login = LoginW()
        self.dashboard = DashboardW()
        self.connect_buttons_dashboard()
        self.connect_buttons_login()
    
    ##Button connections##  
    def connect_buttons_login(self):
        self.login.ui.btnLogin.clicked.connect(self.show_dashboard)
        
    def connect_buttons_dashboard(self):
        self.dashboard.ui.actLogOut.triggered.connect(self.show_login)
        
        self.dashboard.ui.btnBugClear.clicked.connect(self.dashboard.get_fields_bugs)
        self.dashboard.ui.btnAdminClear.clicked.connect(self.dashboard.get_fields_admins)
        self.dashboard.ui.btnListenersClear.clicked.connect(self.dashboard.get_fields_listeners)
        self.dashboard.ui.btnBackupClear.clicked.connect(self.dashboard.get_fields_backup)


    ##Window Change functions##
    def show_login(self):
        self.login.window.show()
        self.dashboard.window.close()

    def show_dashboard(self):
        self.dashboard.window.show()
        self.login.window.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()