import requests
import json

class POSTClient():
    def __init__(self):
        self.identifier = 'veeQau9PXTPxDLSfkqASokKC7phAc6vgaREIUDOeIqLS5GoCTFGURkFGDDppCIaG8Vq44yUxslPeoXEf3ExquC6oZddR4qHupVsp'

    ##Sends the prepared messages to the available urls and returns the response object##
    def send(self, url, message):
        message["pcIdentifier"]=self.identifier
        URL = f"http://localhost:8000/{url}/"
        r = requests.post(URL, data=message)
        response={
            "status_code":r.status_code,
            "reason":r.reason,
            "payload":r.text
        }
        return json.loads(response["payload"])

if __name__ == "__main__":
    ##TESTING LINES
    cl = POSTClient()
    print(cl.send(url='get-admin-records', message='SELECT * FROM bugs'))