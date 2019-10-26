import requests
import time

class POSTClient():
    
    def send(self, payload):
        self.r = requests.post("http://192.168.8.201:1880/InsertBugRecord", data={'number': 1234, 'type':'issue', 'action':'show'})
        print(self.r.status_code, self.r.reason)
        print(self.r.text)

if __name__ == "__main__":
    ##TESTING LINES
    cl = POSTClient()
    print(cl.send('test'))