import requests
from datetime import datetime
import time

class POSTClient():
    def __init__(self):
        self.URL="http://192.168.8.201:1880/BugTrackerCRUD"

    ##Sends the prepared messages to the available urls and returns the response object##
    def send(self, message):
        payload = {"statement":message}
        r = requests.post(self.URL, data=payload)
        response={
            "status_code":r.status_code,
            "reason":r.reason,
            "payload":r.text
        }
        return response

if __name__ == "__main__":
    ##TESTING LINES
    cl = POSTClient()
    print(cl.send('SELECT * FROM bugs'))