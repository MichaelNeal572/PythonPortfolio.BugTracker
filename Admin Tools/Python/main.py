import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from SupportClasses import dashboard, login, databaseconnector

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
        return(fields)

class DashboardW:
    def __init__(self):
        self.window = dashboard.QtWidgets.QMainWindow()
        self.ui = dashboard.Ui_MainWindow()
        self.ui.setupUi(self.window)

    ##Input field functions##
    def clear_fields_bugs(self):
        pass

    def populate_fields_bugs(self):
        pass

    def set_fields_bugs(self):
        pass

    def get_fields_bugs(self):
        if (self.ui.rdoBugUnknown.isChecked()):
            resolution_temp="TBD"
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
        return(fields)

    def clear_fields_admins(self):
        pass

    def populate_fields_admins(self):
        pass

    def set_fields_admins(self):
        pass

    def get_fields_admins(self):
        fields={
            "username":self.ui.txtAdminUserName.text(),
            "firstname":self.ui.txtAdminFirstName.text(),
            "lastname":self.ui.txtAdminLastName.text(),
            "password":self.ui.txtAdminPassword.text()
        }
        return(fields)

    def clear_fields_listeners(self):
        pass

    def populate_fields_listeners(self):
        pass

    def set_fields_listeners(self):
        pass

    def get_fields_listeners(self):
        fields={
            "username":str(self.ui.cmbListenersUserName.currentText()),
            "bug_source":str(self.ui.cmbListenersBugSource.currentText())
        }
        return(fields)

    def clear_fields_backup(self):
        pass

    def populate_fields_backup(self):
        pass

    def set_fields_backup(self):
        pass

    def get_fields_backup(self):
        fields={
            "listener":str(self.ui.cmbListener.currentText()),
            "backup":str(self.ui.cmbBackup.currentText())
        }
        return(fields)
    ######################

class Controller:
    def __init__(self):
        self.dbc=databaseconnector.DatabaseConnector()

        self.login = LoginW()
        self.dashboard = DashboardW()
        self.connect_buttons_dashboard()
        self.connect_buttons_login()
    
    ##Button connections##  
    def connect_buttons_login(self):
        self.login.ui.btnLogin.clicked.connect(self.show_dashboard)
        
    def connect_buttons_dashboard(self):
        self.dashboard.ui.actLogOut.triggered.connect(self.show_login)
        self.dashboard.ui.actionRefresh.triggered.connect(self.refresh_tables)
        
        self.dashboard.ui.tblwBugs.clicked.connect(self.dashboard.populate_fields_bugs)
        self.dashboard.ui.tblwAdmin.clicked.connect(self.dashboard.populate_fields_admins)
        self.dashboard.ui.tblwListeners.clicked.connect(self.dashboard.populate_fields_listeners)
        self.dashboard.ui.tblwBackup.clicked.connect(self.dashboard.populate_fields_backup)

        ##Insert buttons
        self.dashboard.ui.btnBugInsert.clicked.connect(self.insert_bug)
        self.dashboard.ui.btnAdminInsert.clicked.connect(self.insert_admin)
        self.dashboard.ui.btnListenersInsert.clicked.connect(self.insert_listener)
        self.dashboard.ui.btnBackupInsert.clicked.connect(self.insert_backup)
        ##Update buttons
        self.dashboard.ui.btnBugUpdate.clicked.connect(self.update_bug)
        self.dashboard.ui.btnAdminUpdate.clicked.connect(self.update_admin)
        self.dashboard.ui.btnListenersUpdate.clicked.connect(self.update_listener)
        self.dashboard.ui.btnBackupUpdate.clicked.connect(self.update_backup)
        ##Delete buttons
        self.dashboard.ui.btnBugDelete.clicked.connect(self.delete_bug)
        self.dashboard.ui.btnAdminDelete.clicked.connect(self.delete_admin)
        self.dashboard.ui.btnListenersDelete.clicked.connect(self.delete_listener)
        self.dashboard.ui.btnBackupDelete.clicked.connect(self.delete_backup)
        ##Clear buttons
        self.dashboard.ui.btnBugClear.clicked.connect(self.dashboard.clear_fields_bugs)
        self.dashboard.ui.btnAdminClear.clicked.connect(self.dashboard.clear_fields_admins)
        self.dashboard.ui.btnListenersClear.clicked.connect(self.dashboard.clear_fields_listeners)
        self.dashboard.ui.btnBackupClear.clicked.connect(self.dashboard.clear_fields_backup)

    ######################

    ##Refresh table displays##
    def refresh_tables(self):
        self.refresh_table_bugs()
        self.refresh_table_admins()
        self.refresh_table_listeners()
        self.refresh_table_backups()

    def refresh_table_bugs(self):
        records = self.dbc.get_bug_records()["resultset"]
        table = self.dashboard.ui.tblwBugs
        self.refresh_table(table, records)

    def refresh_table_admins(self):
        records = self.dbc.get_admin_records()["resultset"]
        table = self.dashboard.ui.tblwAdmin
        self.refresh_table(table, records)

    def refresh_table_listeners(self):
        records = self.dbc.get_listener_records()["resultset"]
        table = self.dashboard.ui.tblwListeners
        self.refresh_table(table, records)

    def refresh_table_backups(self):
        records = self.dbc.get_backup_records()["resultset"]
        table = self.dashboard.ui.tblwBackup
        self.refresh_table(table, records)

    def refresh_table(self, table, records):
        for i in range(table.rowCount())[::-1]:
            table.removeRow(i)

        for record in records:
            nextRow = table.rowCount()
            table.insertRow(nextRow)
            c=0
            for r in record.values():
                table.setItem(nextRow,c,QtWidgets.QTableWidgetItem(str(r)))
                c+=1
    ###########################

    ##Button functions##
    def insert_bug(self):
        fields = self.dashboard.get_fields_bugs()
        self.dbc.insert_bug_record(details=fields["details"], args=fields["args"], kwargs=fields["kwargs"], source=fields["source"], 
            dateCreated=fields["date_created"], status=fields["status"], expectedResolution=fields["expected_resolution"])
        self.refresh_table_bugs()
        
    def insert_admin(self):
        fields = self.dashboard.get_fields_admins()
        table = self.dashboard.ui.tblwAdmin
        self.dbc.insert_admin_record(username=fields["username"], firstname=fields["firstname"], lastname=fields["lastname"], 
            password=fields["password"])
        self.refresh_table_admins()
        
    def insert_listener(self):
        fields = self.dashboard.get_fields_listeners()
        table = self.dashboard.ui.tblwListeners
        self.dbc.insert_listener_record(username=fields["username"], source=fields["bug_source"])
        self.refresh_table_listeners()
        
    def insert_backup(self):
        fields = self.dashboard.get_fields_backup()
        table = self.dashboard.ui.tblwBackup
        self.dbc.insert_backup_record(backupDevID=fields["backup"], devID=fields["listener"])
        self.refresh_table_backups()

    def update_bug(self):
        fields = self.dashboard.get_fields_bugs()
        table = self.dashboard.ui.tblwBugs
        row = table.currentItem().row()
        fields["rowid"] = table.item(row, 0).text()
        self.dbc.update_bug_record(rowID=fields["rowid"], details=fields["details"], args=fields["args"], 
            kwargs=fields["kwargs"], source=fields["source"], dateCreated=fields["date_created"], status=fields["status"], 
            expectedResolution=fields["expected_resolution"])
        self.refresh_table_bugs()

    def update_admin(self):
        fields = self.dashboard.get_fields_admins()
        table = self.dashboard.ui.tblwAdmin
        row = table.currentItem().row()
        fields["rowid"] = table.item(row, 0).text()
        self.dbc.update_admin_record(rowID=fields["rowid"], username=fields["username"], firstname=fields["firstname"], 
            lastname=fields["lastname"], password=fields["password"])
        self.refresh_table_admins()

    def update_listener(self):
        fields = self.dashboard.get_fields_listeners()
        table = self.dashboard.ui.tblwListeners
        row = table.currentItem().row()
        fields["rowid"] = table.item(row, 0).text()
        self.dbc.update_listener_record(rowID=fields["rowid"], username=fields["username"], source=fields["bug_source"])
        self.refresh_table_listeners()

    def update_backup(self):
        fields = self.dashboard.get_fields_backup()
        table = self.dashboard.ui.tblwBackup
        row = table.currentItem().row()
        fields["rowid"] = table.item(row, 0).text()
        self.dbc.update_backup_record(rowID=fields["rowid"], backupDevID=fields["backup"], devID=fields["listener"])
        self.refresh_table_backups()

    def delete_bug(self):
        fields = {}
        table = self.dashboard.ui.tblwBugs
        row = table.currentItem().row()
        fields["rowid"] = table.item(row, 0).text()
        self.dbc.delete_bug_record(rowID=fields["rowid"])
        self.refresh_table_bugs()

    def delete_admin(self):
        fields = {}
        table = self.dashboard.ui.tblwAdmin
        row = self.dashboard.ui.tblwBugs.currentItem().row()
        fields["rowid"] = self.dashboard.ui.tblwAdmin.item(row, 0).text()
        self.dbc.delete_dev_record(rowID=fields["rowid"])
        self.refresh_table_admins()

    def delete_listener(self):
        fields = {}
        table = self.dashboard.ui.tblwListeners
        row = table.currentItem().row()
        fields["rowid"] = table.item(row, 0).text()
        self.dbc.delete_listener_record(rowid=fields["rowid"])
        self.refresh_table_listeners()

    def delete_backup(self):
        fields = {}
        table = self.dashboard.ui.tblwBackup
        row = table.currentItem().row()
        fields["rowid"] = table.item(row, 0).text()
        self.dbc.delete_backup_record(fields["rowid"])
        self.refresh_table_backups()

    ###########################

    ##Window Change functions##
    def show_login(self):
        self.login.window.show()
        self.dashboard.window.close()

    def show_dashboard(self):
        self.dashboard.window.show()
        self.login.window.close()
        self.refresh_tables()
    ###########################

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()