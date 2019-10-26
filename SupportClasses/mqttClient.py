import paho.mqtt.client as mqttClientInterface
from datetime import datetime
import time
import json

class Client():
    def __init__(self):
        ##Client configuration variables##
        self.sub_topic = "python/bugReport/Response"
        self.broker_address="192.168.8.201"
        self.user = "pi"
        self.password = "mike"
        self.result = ""
        ##Client Initialization##
        self.client = mqttClientInterface.Client("P1") #create new instance
        self.client.username_pw_set(self.user, password = self.password)
        self.client.on_message = self.on_message #attach function to callback

    def on_message(self, client, userdata, message):
        cl.result = message.payload.decode("utf-8")

    def insert_bug(self, bugDetails, bugArguments, bugSource):
        self.pub_topic = "python/bugReport/InsertBugRecord"
        self.payload = {}
        self.payload['bugDetails'] = bugDetails
        self.payload['bugArguments'] = bugArguments
        self.payload['bugSource'] = bugSource
        self.payload['bugDateCreated'] = str(datetime.now())
        self.payload['bugStatus'] = "New"
        self.payload['bugExpectedDevTime'] = "TBD"
        self.payload=json.dumps(self.payload)
        return(self.send(self.payload, self.pub_topic))

    def send(self, payload, pub_topic):
        self.client.connect(self.broker_address) #connect to broker
        self.client.loop_start() #start the loop
        self.client.subscribe(self.sub_topic)
        self.client.publish(pub_topic, payload)
        time.sleep(4) # wait
        self.client.loop_stop() #stop the loop
        return(self.result)

if __name__ == "__main__":
    ##TESTING LINES
    cl = Client()
    print(cl.insert_bug(4, "test", "test", "test", "test", "test"))