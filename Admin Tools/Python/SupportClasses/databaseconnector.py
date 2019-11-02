import requests
import json
from SupportClasses import POSTClient

class DatabaseConnector:
    def __init__(self):
        self.postClient = POSTClient.POSTClient()

    ##Read##
    def get_bug_records(self):
        message = "SELECT rowId, bugDetails, bugArguments, bugSource, bugDateCreated, bugStatus, bugExpectedResolution FROM bugs"
        return(self.postClient.send(message))

    def get_admin_records(self):
        message = "SELECT rowId, devUserName, devFirstName, devLastName, devPassword FROM devs"
        return(self.postClient.send(message))

    def get_listener_records(self):
        message = "SELECT rowId, devUserName, bugSource FROM listeners"
        return(self.postClient.send(message))

    def get_backup_records(self):
        message = "SELECT rowId, backupDevID, devID FROM backupListeners"
        return(self.postClient.send(message))
    
    #Insert##
    def insert_bug_record(self, details, args, kwargs, source, dateCreated, status, expectedResolution):
        message=f'''INSERT INTO bugs (bugDetails, bugArguments, bugSource, bugDateCreated, bugStatus, bugExpectedResolution)
        VALUES ("{details}", "args: {args} kwargs: {kwargs}", "{source}", "{dateCreated}", "{status}", "{expectedResolution}")
        '''
        return(self.postClient.send(message))

    def insert_admin_record(self, username, firstname, lastname, password):
        message=f'''INSERT INTO devs (devUserName, devFirstName, devLastName, devPassword)
        VALUES ("{username}", "{firstname}", "{lastname}", "{password}")
        '''
        return(self.postClient.send(message))

    def insert_listener_record(self, username, source):
        message=f'''INSERT INTO listeners (devUserName, bugSource)
        VALUES ("{username}", "{source}")
        '''
        return(self.postClient.send(message))

    def insert_backup_record(self, backupDevID, devID):
        message=f'''INSERT INTO backupListeners (backupDevID, devID)
        VALUES ("{backupDevID}", "{devID}")
        '''
        return(self.postClient.send(message))
    
    ##Update##
    def update_bug_record(self, rowID, details, args, kwargs, source, dateCreated, status, expectedResolution):
        message=f'''UPDATE bugs SET
        bugDetails = "{details}", 
        bugArguments = "args: {args} kwargs: {kwargs}", 
        bugSource = "{source}", 
        bugDateCreated = "{dateCreated}", 
        bugStatus = "{status}", 
        bugExpectedResolution = "{expectedResolution}"
        WHERE rowid = {rowID}
        '''
        return(self.postClient.send(message))

    def update_admin_record(self, rowID, username, firstname, lastname, password):
        message=f'''UPDATE devs SET
        devUserName = "{username}", 
        devFirstName = "{firstname}", 
        devLastName = "{lastname}", 
        devPassword = "{password}"
        WHERE rowid = {rowID}
        '''
        return(self.postClient.send(message))

    def update_listener_record(self, rowID, username, source):
        message=f'''UPDATE listeners SET
        devUserName = "{username}", 
        bugSource = "{source}"
        WHERE rowid = {rowID}
        '''
        return(self.postClient.send(message))

    def update_backup_record(self, rowID, backupDevID, devID):
        message=f'''UPDATE backupListeners SET
        backupDevID = "{backupDevID}", 
        devID = "{devID}"
        WHERE rowid = {rowID}
        '''
        return(self.postClient.send(message))
    
    ##Delete##
    def delete_bug_record(self, rowID):
        message=f'''DELETE FROM bugs WHERE rowid="{rowID}"
        '''
        return(self.postClient.send(message))

    def delete_dev_record(self, rowID):
        message=f'''DELETE FROM devs WHERE rowid="{rowID}"
        '''
        return(self.postClient.send(message))

    def delete_listener_record(self, rowID):
        message=f'''DELETE FROM listeners WHERE rowid="{rowID}"
        '''
        return(self.postClient.send(message))

    def delete_backup_record(self, rowID):
        message=f'''DELETE FROM backupListeners WHERE rowid="{rowID}"
        '''
        return(self.postClient.send(message))
