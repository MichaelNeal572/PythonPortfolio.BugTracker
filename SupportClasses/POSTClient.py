import requests
from datetime import datetime
import time

class POSTClient():
    def insert_bug(self, bugDetails, bugArguments, bugSource,bugDateCreated, bugStatus, bugExpectedDevTime):
        url = "http://192.168.8.201:1880/InsertBugRecord"
        message={
            "bugDetails":bugDetails, 
            "bugArguments":bugArguments, 
            "bugSource":bugSource,
            "bugDateCreated":bugDateCreated, 
            "bugStatus":bugStatus, 
            "bugExpectedDevTime":bugExpectedDevTime
        }
        return(self.send(message, url))

    def insert_bug_new(self, bugDetails, bugArguements, bugSource):
        return(self.insert_bug(bugDetails, bugArguements, bugSource, datetime.now(), "New", "TBD"))

    def send(self, message, url):
        r = requests.post(url, data=message)
        response={
            "status_code":r.status_code,
            "reason":r.reason,
            "text":r.text
        }
        return response

if __name__ == "__main__":
    ##TESTING LINES
    cl = POSTClient()
    print(cl.insert_bug_new('Test', 'Test', 'Test'))