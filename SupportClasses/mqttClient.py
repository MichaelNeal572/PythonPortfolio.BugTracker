import paho.mqtt.client as mqttClientInterface
import time

class mqttClient():
    def __init__(self):
        self.broker_address= "192.168.8.201"
        self.port = 1883
        self.user = "pi"
        self.password = "mike"
        self.connected=False
        self.response=False
        self.sub_topic="python/bugReport/Response"
        self.pub_topic="python/bugReport/BugReportsCRUD"

        self.client = mqttClientInterface.Client("Python")               #create new instance
        self.client.username_pw_set(self.user, password=self.password)    #set username and password
        self.client.on_connect= self.on_connect                 #attach function to callback
        self.client.on_message=self.on_message
        self.client.on_log=self.on_log
    
    def on_log(client, userdata, level, buf):
        print("log: ",buf)

    def on_message(client, userdata, message):
        print(f"message payload: {message.payload}")
        print(f"massage topic: {message.topic}")
        self.response=True
 
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            self.connected = True                #Signal connection 
        else:
            print("Connection failed")
            self.connected = False   #global variable for the state of the connection

    def send(self, payload):
        self.client.connect(self.broker_address, port=self.port)          #connect to broker
        self.client.loop_start()
        self.client.subscribe(self.sub_topic)

        while (not self.connected):
            time.sleep(0.1)
        self.client.publish(self.pub_topic, payload)
        
        
        while (not self.response):
            time.sleep(0.1)
            print("waiting")

        print("Complete")
        self.client.loop_stop()
 

if __name__=="__main__":
    ##TESTING LINES
    cl = mqttClient()
    cl.send("Test")