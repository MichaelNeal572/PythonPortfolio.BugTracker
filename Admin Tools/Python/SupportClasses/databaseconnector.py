import requests
import json
from SupportClasses import POSTClient

class DatabaseConnector:
    def __init__(self):
        self.postClient = POSTClient.POSTClient()

    ##Read##
    def get_bug_records(self):
        message = {}
        return(self.postClient.send(url = "get-bug-records", message=message))

    def get_admin_records(self):
        message = {}
        return(self.postClient.send(url = "get-admin-records", message=message))

    def get_listener_records(self):
        message = {}
        return(self.postClient.send(url = "get-listener-records", message=message))

    def get_backup_records(self):
        message = {}
        return(self.postClient.send(url = "get-backup-records", message=message))
    
    #Insert##
    def insert_bug_record(self, details, args, kwargs, source, dateCreated, status, expectedResolution):
        arguments = f'args: {args}; kwargs: {kwargs};'
        message = {
            "bugDetails":details, 
            "bugArguments":arguments,
            "bugSource":source, 
            "bugDateCreated":dateCreated, 
            "bugStatus":status, 
            "bugExpectedResolution":expectedResolution
        }
        return(self.postClient.send(url = "insert-bug-record", message=message))

    def insert_admin_record(self, username, firstname, lastname, email, password):
        message={
            "devUserName":username, 
            "devFirstName":firstname, 
            "devLastName":lastname, 
            "devEmail":email,
            "devPassword":password
        }
        return(self.postClient.send(url="insert-admin-record", message=message))

    def insert_listener_record(self, username, source):
        message={
            "devUserName":username, 
            "bugSource":source
        }
        return(self.postClient.send(url="insert-listener-record", message=message))

    def insert_backup_record(self, backupDev, dev):
        message={
            "backupDev":backupDev, 
            "dev":dev
        }
        return(self.postClient.send(url="insert-backup-record", message=message))
    
    ##Update##
    def update_bug_record(self, rowID, details, args, kwargs, source, dateCreated, status, expectedResolution):
        arguments = f'args: {args}; kwargs: {kwargs};'
        message={
            "rowID":rowID, 
            "bugDetails":details, 
            "bugArguments":arguments,
            "bugSource":source, 
            "bugDateCreated":dateCreated, 
            "bugStatus":status, 
            "bugExpectedResolution":expectedResolution
        }
        return(self.postClient.send(url="update-bug-record", message=message))

    def update_admin_record(self, rowID, username, firstname, lastname, email, password):
        message={
            "rowID":rowID,
            "devUsername":username, 
            "devFirstName":firstname, 
            "devLastName":lastname, 
            "devEmail":email,
            "devPassword":password
        }
        return(self.postClient.send(url="update-admin-record", message=message))

    def update_listener_record(self, rowID, username, source):
        message={
            "rowID":rowID, 
            "devUserName":username, 
            "bugSource":source
        }
        return(self.postClient.send(url="update-listener-record", message=message))

    def update_backup_record(self, rowID, backupDev, dev):
        message={
            "rowID":rowID, 
            "backupDev":backupDev, 
            "dev":dev
        }
        return(self.postClient.send(url="update-backup-record", message=message))
    
    ##Delete##
    def delete_bug_record(self, rowID):
        message={
            "rowID":rowID
        }
        return(self.postClient.send(url="delete-bug-record", message=message))

    def delete_dev_record(self, rowID):
        message={
            "rowID":rowID
        }
        return(self.postClient.send(url="delete-dev-record", message=message))

    def delete_listener_record(self, rowID):
        message={
            "rowID":rowID
        }
        return(self.postClient.send(url="delete-listener-record", message=message))

    def delete_backup_record(self, rowID):
        message={
            "rowID":rowID
        }
        return(self.postClient.send(url="delete-backup-record", message=message))

    def get_distinct_admins(self):
        message = {}
        return(self.postClient.send(url="get-distinct-admins", message=message))

    def get_distinct_bug_sources(self):
        message = {}
        return(self.postClient.send(url="get-distinct-bug-sources", message=message))

    def check_user_login(self, username, password):
        message={
            "username":username, 
            "password":password
        }
        return(self.postClient.send(url="check-user-login", message=message))
