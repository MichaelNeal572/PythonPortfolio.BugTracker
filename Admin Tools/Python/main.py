import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import datetime
import re
from dateutil import parser
from SupportClasses import dashboard, login, databaseconnector

class User:
    def __init__(self, username="", password = ""):
        self.username = username
        self.password = password

    def set_user(self, username, password):
        self.__init__(username, password)

    def check_user(self, username):
        return (username == self.username)

class ErrorW:
    def __init__(self):
        self.window = QtWidgets.QMessageBox()


    def showMessage(self, message, details = "", type = ""):
        self.window.setWindowTitle("");
        self.window.setText(message);
        self.window.setDetailedText(details);
        if type=="Warning":
            self.window.setIcon(QtWidgets.QMessageBox.Warning)
        elif type=="Information":
            self.window.setIcon(QtWidgets.QMessageBox.Information)
        elif type =="Critical":
            self.window.setIcon(QtWidgets.QMessageBox.Critical)
        self.window.show()

class LoginW:
    def __init__(self):
        self.window = login.QtWidgets.QMainWindow()
        self.ui = login.Ui_LoginW()
        self.ui.setupUi(self.window)

    def get_fields(self):
        check = {
            "safe":True,
            "message":""
        }

        fields={
            "username":self.ui.txtUsername.text(),
            "password":self.ui.txtPassword.text()
        }

        if(fields["username"]==""):
            check["safe"]=False
            check["message"]="Please Enter Username"

        elif(fields["password"]==""):
            check["safe"]=False
            check["message"]="Please Enter Password"

        return(check, fields)

class DashboardW:
    def __init__(self):
        self.window = dashboard.QtWidgets.QMainWindow()
        self.ui = dashboard.Ui_MainWindow()
        self.ui.setupUi(self.window)

    ##Input field functions##
    def clear_fields_bugs(self):
        self.ui.txtBugDetails.setText("")
        self.ui.txtBugArgs.setText("")
        self.ui.txtBugKwargs.setText("")
        self.ui.txtBugSource.setText("")
        self.ui.deBugDateCreated.setDate(datetime.datetime.now())
        self.ui.cmbBugStatus.setCurrentIndex(0)
        self.ui.dteBugResolution.setDateTime(datetime.datetime.now())
        self.ui.rdoBugUnknown.setChecked(True)

    def populate_fields_bugs(self):
        table = self.ui.tblwBugs
        row = table.selectedIndexes()[-1].row()
        self.ui.txtBugDetails.setText(table.item(row, 1).text())
        arguements = table.item(row, 2).text()
        regex = r":.*?;"
        split = re.findall(regex, arguements)
        print(split)
        self.ui.txtBugArgs.setText(split[0][2:-1])
        self.ui.txtBugKwargs.setText(split[1][2:-1])
        self.ui.txtBugSource.setText(table.item(row, 3).text())
        self.ui.deBugDateCreated.setDate(parser.parse(table.item(row, 4).text()))
        index = self.ui.cmbBugStatus.findText(table.item(row, 5).text(), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.cmbBugStatus.setCurrentIndex(index)
        if table.item(row, 6).text() == "TBD":
            self.ui.rdoBugUnknown.setChecked(True)
        else:
            self.ui.dteBugResolution.setDateTime(parser.parse(table.item(row, 6).text()))
            self.ui.rdoBugKnown.setChecked(True)
        
    def get_fields_bugs(self):
        if (self.ui.rdoBugUnknown.isChecked()):
            resolution_temp="TBD"
        elif(self.ui.rdoBugKnown.isChecked()):
            resolution_temp=self.ui.dteBugResolution.dateTime().toPyDateTime()
        else:
            resolution_temp=None
        
        check = {
            "safe":True,
            "message":""
        }

        fields={
            "details":self.ui.txtBugDetails.text(),
            "args":self.ui.txtBugArgs.text(),
            "kwargs":self.ui.txtBugKwargs.text(),
            "source":self.ui.txtBugSource.text(),
            "date_created":self.ui.deBugDateCreated.date().toPyDate(),
            "status":str(self.ui.cmbBugStatus.currentText()),
            "expected_resolution":resolution_temp
        }

        if(fields["details"]==""):
            check["safe"]=False
            check["message"]="Please enter details"
        if(fields["source"]==""):
            check["safe"]=False
            check["message"]="Please enter a source"
        if(fields["expected_resolution"]==None):
            check["safe"]=False
            check["message"]="Please check a radio button for expected resolution"

        return(check, fields)

    def clear_fields_admins(self):
        self.ui.txtAdminUserName.setText("")
        self.ui.txtAdminFirstName.setText("")
        self.ui.txtAdminLastName.setText("")
        self.ui.txtAdminEmail.setText("")
        self.ui.txtAdminPassword.setText("")

    def populate_fields_admins(self):
        table = self.ui.tblwAdmin
        row = table.selectedIndexes()[-1].row()
        self.ui.txtAdminUserName.setText(table.item(row, 1).text())
        self.ui.txtAdminFirstName.setText(table.item(row, 2).text())
        self.ui.txtAdminLastName.setText(table.item(row, 3).text())
        self.ui.txtAdminEmail.setText(table.item(row, 4).text())
        self.ui.txtAdminPassword.setText(table.item(row, 5).text())

    def get_fields_admins(self):
        check = {
            "safe":True,
            "message":""
        }

        fields={
            "username":self.ui.txtAdminUserName.text(),
            "firstname":self.ui.txtAdminFirstName.text(),
            "lastname":self.ui.txtAdminLastName.text(),
            "email":self.ui.txtAdminEmail.text(),
            "password":self.ui.txtAdminPassword.text()
        }

        if(fields["username"]==""):
            check["safe"]=False
            check["message"]="Please enter a username"
        if(fields["firstname"]==""):
            check["safe"]=False
            check["message"]="Please enter a firstname"
        if(fields["lastname"]==""):
            check["safe"]=False
            check["message"]="Please enter a username"
        if(fields["password"]==""):
            check["safe"]=False
            check["message"]="Please enter a password"
        if(len(fields["password"])<8):
            check["safe"]=False
            check["message"]="Your password should be at least 8 characters long"

        return(check, fields)

    def clear_fields_listeners(self):
        self.ui.cmbListenersUserName.setCurrentIndex(0)
        self.ui.cmbListenersBugSource.setCurrentIndex(0)

    def populate_fields_listeners(self):
        table = self.ui.tblwListeners
        row = table.selectedIndexes()[-1].row()

        index = self.ui.cmbListenersUserName.findText(table.item(row, 1).text(), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.cmbListenersUserName.setCurrentIndex(index)
        index = self.ui.cmbListenersBugSource.findText(table.item(row, 2).text(), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.cmbListenersBugSource.setCurrentIndex(index)

    def get_fields_listeners(self):
        check = {
            "safe":True,
            "message":""
        }

        fields={
            "username":str(self.ui.cmbListenersUserName.currentText()),
            "bug_source":str(self.ui.cmbListenersBugSource.currentText())
        }

        return(check, fields)

    def clear_fields_backup(self):
        self.ui.cmbListener.setCurrentIndex(0)
        self.ui.cmbBackup.setCurrentIndex(0)

    def populate_fields_backup(self):
        table = self.ui.tblwBackup
        row = table.selectedIndexes()[-1].row()

        index = self.ui.cmbListener.findText(table.item(row, 1).text(), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.cmbListener.setCurrentIndex(index)
        index = self.ui.cmbBackup.findText(table.item(row, 2).text(), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.cmbBackup.setCurrentIndex(index)

    def get_fields_backup(self):
        check = {
            "safe":True,
            "message":""
        }
        
        fields={
            "listener":str(self.ui.cmbListener.currentText()),
            "backup":str(self.ui.cmbBackup.currentText())
        }
        
        if(fields["listener"]==fields["backup"]):
            check["safe"]=False
            check["message"]="Backup and listener cannot be the same user"
        
        return(check, fields)
    ######################

class Controller:
    def __init__(self):
        self.dbc=databaseconnector.DatabaseConnector()
        self.currentUser = User()

        self.login = LoginW()
        self.dashboard = DashboardW()
        self.errorDisplay = ErrorW()
        
        self.connect_buttons_dashboard()
        self.connect_buttons_login()
    
    ##Button connections##  
    def connect_buttons_login(self):
        self.login.ui.btnLogin.clicked.connect(self.log_in)
        self.login.ui.btnExit.clicked.connect(self.exit_program)
        
    def connect_buttons_dashboard(self):
        self.dashboard.ui.actLogOut.triggered.connect(self.show_login)
        self.dashboard.ui.actionRefresh.triggered.connect(self.refresh_tables)
        self.dashboard.ui.actExit.triggered.connect(self.exit_program)
        
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

    ##Window Change functions##
    def show_login(self):
        self.login.window.show()
        self.dashboard.window.close()

    def show_dashboard(self):
        self.dashboard.window.show()
        self.login.window.close()
        self.refresh_tables()

    def log_in(self):
        check, fields = self.login.get_fields()
        if(check["safe"]):
            records = self.dbc.check_user_login(fields["username"], fields["password"])["result"]
            if records==1:
                self.currentUser.set_user(username=fields["username"], password=fields["password"])
                self.show_dashboard()
            else:
                self.errorDisplay.showMessage(message="Login Error", details="login details did not match any details in our database", type ="Warning")
        else:
            self.errorDisplay.showMessage(message="Login Error", details="Please enter login details", type ="Warning")
        

    def exit_program(self):
        sys.exit()

    ###########################

    ##Refresh table displays##
    def refresh_tables(self):
        self.refresh_table_bugs()
        self.refresh_table_admins()
        self.refresh_table_listeners()
        self.refresh_table_backups()

    def refresh_table_bugs(self):
        reply = self.dbc.get_bug_records()
        if reply["status"]=="Success":
            records = reply["result"]
            table = self.dashboard.ui.tblwBugs
            self.refresh_table(table, records)
            self.refresh_combo_boxes_sources()
        else:
            self.errorDisplay.showMessage(message="Database Error", details=reply["result"], type ="Warning")

    def refresh_table_admins(self):
        reply = self.dbc.get_admin_records()
        if reply["status"]=="Success":
            records = reply["result"]
            table = self.dashboard.ui.tblwAdmin
            self.refresh_table(table, records)
            self.refresh_combo_boxes_admins()
        else:
            self.errorDisplay.showMessage(message="Database Error", details=reply["result"], type ="Warning")

    def refresh_table_listeners(self):
        reply = self.dbc.get_listener_records()
        if reply["status"]=="Success":
            records = reply["result"]
            table = self.dashboard.ui.tblwListeners
            self.refresh_table(table, records)
        else:
            self.errorDisplay.showMessage(message="Database Error", details=reply["result"], type ="Warning")

    def refresh_table_backups(self):
        reply = self.dbc.get_backup_records()
        if reply["status"]=="Success":
            records = reply["result"]
            table = self.dashboard.ui.tblwBackup
            self.refresh_table(table, records)
        else:
            self.errorDisplay.showMessage(message="Database Error", details=reply["result"], type ="Warning")

    def refresh_table(self, table, records):
        for i in range(table.rowCount())[::-1]:
            table.removeRow(i)

        for record in records:
            nextRow = table.rowCount()
            table.insertRow(nextRow)
            c=0
            try:
                for r in record:
                    table.setItem(nextRow,c,QtWidgets.QTableWidgetItem(str(r)))
                    c+=1
            except Exception as e:
                print(f"table exception: {str(e)}")

    def refresh_combo_boxes_admins(self):
        devs = self.dbc.get_distinct_admins()
        self.dashboard.ui.cmbListener.clear()
        self.dashboard.ui.cmbBackup.clear()
        self.dashboard.ui.cmbListenersUserName.clear()
        items = [ _[0] for _ in devs["result"]]
        self.dashboard.ui.cmbListener.addItems(items)
        self.dashboard.ui.cmbBackup.addItems([ _[0] for _ in devs["result"]])
        self.dashboard.ui.cmbListenersUserName.addItems([ _[0] for _ in devs["result"]])

    def refresh_combo_boxes_sources(self):
        bugSources = self.dbc.get_distinct_bug_sources()
        self.dashboard.ui.cmbListenersBugSource.clear()
        items = [ _[0] for _ in bugSources["result"]]
        self.dashboard.ui.cmbListenersBugSource.addItems(items)

    ###########################

    ##Button functions##
    def insert_bug(self):
        check, fields = self.dashboard.get_fields_bugs()
        if(check["safe"]):
            self.dbc.insert_bug_record(details=fields["details"], args=fields["args"], kwargs=fields["kwargs"], source=fields["source"], 
                dateCreated=fields["date_created"], status=fields["status"], expectedResolution=fields["expected_resolution"])
            self.refresh_table_bugs()
        else:
            self.errorDisplay.showMessage(message="Please check input fields", details=check["message"], type ="Warning")
        
    def insert_admin(self):
        check, fields = self.dashboard.get_fields_admins()
        if(check["safe"]):
            result = self.dbc.insert_admin_record(username=fields["username"], firstname=fields["firstname"], lastname=fields["lastname"], 
                email=fields["email"], password=fields["password"])
            self.refresh_table_admins()
        else:
            self.errorDisplay.showMessage(message="Please check input fields", details=check["message"], type ="Warning")
        
    def insert_listener(self):
        check, fields = self.dashboard.get_fields_listeners()
        if(check["safe"]):
            self.dbc.insert_listener_record(username=fields["username"], source=fields["bug_source"])
            self.refresh_table_listeners()
        else:
            self.errorDisplay.showMessage(message="Please check input fields", details=check["message"], type ="Warning")
        
    def insert_backup(self):
        check, fields = self.dashboard.get_fields_backup()
        if(check["safe"]):
            self.dbc.insert_backup_record(backupDev=fields["backup"], dev=fields["listener"])
            self.refresh_table_backups()
        else:
            self.errorDisplay.showMessage(message="Please check input fields", details=check["message"], type ="Warning")

    def update_bug(self):
        check, fields = self.dashboard.get_fields_bugs()
        table = self.dashboard.ui.tblwBugs
        row = table.selectedIndexes()[-1].row()

        if not row>-1:
            check["safe"]=False
            check["message"]="Please select a record to update"

        if(check["safe"]):
            
            fields["rowid"] = table.item(row, 0).text()
            self.dbc.update_bug_record(rowID=fields["rowid"], details=fields["details"], args=fields["args"], 
                kwargs=fields["kwargs"], source=fields["source"], dateCreated=fields["date_created"], status=fields["status"], 
                expectedResolution=fields["expected_resolution"])
            self.refresh_table_bugs()
        else:
            self.errorDisplay.showMessage(message="Please check input fields", details=check["message"], type ="Warning")

    def update_admin(self):
        check, fields = self.dashboard.get_fields_admins()
        table = self.dashboard.ui.tblwAdmin
        row = table.selectedIndexes()[-1].row()
        print(f"selected row: {row}")
        if not row>-1:
            check["safe"]=False
            check["message"]="Please select a record to update"

        if(check["safe"]):
            table = self.dashboard.ui.tblwAdmin
            row = table.currentItem().row()
            fields["rowid"] = table.item(row, 0).text()
            self.dbc.update_admin_record(rowID=fields["rowid"], username=fields["username"], firstname=fields["firstname"], 
                lastname=fields["lastname"], email=fields["email"], password=fields["password"])
            self.refresh_table_admins()
        else:
            self.errorDisplay.showMessage(message="Please check input fields", details=check["message"], type ="Warning")

    def update_listener(self):
        check, fields = self.dashboard.get_fields_listeners()
        table = self.dashboard.ui.tblwListeners
        row = table.selectedIndexes()[-1].row()
        
        if not row>-1:
            check["safe"]=False
            check["message"]="Please select a record to update"

        if(check["safe"]):
            
            fields["rowid"] = table.item(row, 0).text()
            self.dbc.update_listener_record(rowID=fields["rowid"], username=fields["username"], source=fields["bug_source"])
            self.refresh_table_listeners()
        else:
            self.errorDisplay.showMessage(message="Please check input fields", details=check["message"], type ="Warning")

    def update_backup(self):
        check, fields = self.dashboard.get_fields_backup()
        table = self.dashboard.ui.tblwBackup
        row = table.selectedIndexes()[-1].row()

        if not row>-1:
            check["safe"]=False
            check["message"]="Please select a record to update"

        if(check["safe"]):
            
            fields["rowid"] = table.item(row, 0).text()
            self.dbc.update_backup_record(rowID=fields["rowid"], backupDev=fields["backup"], dev=fields["listener"])
            self.refresh_table_backups()
        else:
            self.errorDisplay.showMessage(message="Please check input fields", details=check["message"], type ="Warning")

    def delete_bug(self):
        fields = {}
        check = {
            "safe":True,
            "message":""
        }
        table = self.dashboard.ui.tblwBugs
        row = table.currentItem().row()
        
        if not row>-1:
            check["safe"]=False
            check["message"]="Please select a record to delete"
        
        if(check["safe"]):
            fields["rowid"] = table.item(row, 0).text()
            self.dbc.delete_bug_record(rowID=fields["rowid"])
            self.refresh_table_bugs()
        else:
            self.errorDisplay.showMessage(message="Please check input", details=check["message"], type ="Warning")

    def delete_admin(self):
        fields = {}
        check = {
            "safe":True,
            "message":""
        }
        table = self.dashboard.ui.tblwAdmin
        row = table.currentItem().row()
        
        if not row>-1:
            check["safe"]=False
            check["message"]="Please select a record to delete"

        if self.currentUser.check_user(table.item(row, 0).text()):
            check["safe"]=False
            check["message"]="You cannot remove your own record. Please contact another admin"

        if(check["safe"]):
            fields["rowid"] = self.dashboard.ui.tblwAdmin.item(row, 0).text()
            self.dbc.delete_dev_record(rowID=fields["rowid"])
            self.refresh_table_admins()
        else:
            self.errorDisplay.showMessage(message="Please check input", details=check["message"], type ="Warning")

    def delete_listener(self):
        fields = {}
        check = {
            "safe":True,
            "message":""
        }
        table = self.dashboard.ui.tblwListeners
        row = table.currentItem().row()

        if not row>-1:
            check["safe"]=False
            check["message"]="Please select a record to delete"

        if(check["safe"]):
            fields["rowid"] = table.item(row, 0).text()
            self.dbc.delete_listener_record(rowid=fields["rowid"])
            self.refresh_table_listeners()
        else:
            self.errorDisplay.showMessage(message="Please check input", details=check["message"], type ="Warning")

    def delete_backup(self):
        fields = {}
        check = {
            "safe":True,
            "message":""
        }
        table = self.dashboard.ui.tblwBackup
        row = table.currentItem().row()

        if not row>-1:
            check["safe"]=False
            check["message"]="Please select a record to delete"

        if(check["safe"]):
            fields["rowid"] = table.item(row, 0).text()
            self.dbc.delete_backup_record(fields["rowid"])
            self.refresh_table_backups()
        else:
            self.errorDisplay.showMessage(message="Please check input", details=check["message"], type ="Warning")

    ###########################

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()