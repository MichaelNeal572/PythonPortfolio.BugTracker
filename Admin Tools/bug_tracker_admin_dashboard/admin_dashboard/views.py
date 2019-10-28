from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

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
        y = json.loads(r.text)
        print(y)
        return y



def home(request):
	return render(request, 'admin_dashboard/home.html')

def about(request):
	pc = POSTClient()
	result = pc.send("SELECT * FROM bugs")
	context = {
		'records':result['resultset'],
		'title':'About'
	}
	return render(request, 'admin_dashboard/about.html', context)
