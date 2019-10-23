import paho.mqtt.client as mqttClientInterface
import time

class mqttClient():
    def __init__(self):
        ##Client configuration variables##
        self.sub_topic = "python/bugReport/Response"
        self.pub_topic = "python/bugReport/BugReportsCRUD"
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

    def send(self, payload):
        self.client.connect(self.broker_address) #connect to broker
        self.client.loop_start() #start the loop
        self.client.subscribe(self.sub_topic)
        self.client.publish(self.pub_topic, payload)
        time.sleep(4) # wait
        self.client.loop_stop() #stop the loop
        return(self.result)

if __name__ == "__main__":
    ##TESTING LINES
    cl = mqttClient()
    print(cl.send("SELECT * FROM bugs"))