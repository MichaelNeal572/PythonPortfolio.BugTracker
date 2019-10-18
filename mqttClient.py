import paho.mqtt.client as mqttClientInterface
import time

class mqttClient():
    def __init__(self):
        self.broker_address= "192.168.8.201"
        self.port = 1883
        self.user = "pi"
        self.password = "mike"
        self.Connected=False

        self.client = mqttClientInterface.Client("Python")               #create new instance
        self.client.username_pw_set(self.user, password=self.password)    #set username and password
        print(self.on_connect)
        self.client.on_connect= self.on_connect                 #attach function to callback
        self.client.connect(self.broker_address, port=self.port)          #connect to broker
        print("__init__ complete")
 
    def on_connect(self, client, userdata, flags, rc):
     
        if rc == 0:
            print("Connected to broker")
            self.Connected = True                #Signal connection 
        else:
            print("Connection failed")
            self.Connected = False   #global variable for the state of the connection
 

if __name__=="__main__":
    cl = mqttClient()
    cl.client.loop_start()        #start the loop
     
    while cl.Connected != True:    #Wait for connection
        print("Connected: "+str(cl.Connected))
        time.sleep(0.1)
    try:
        while True:
            value = input('Enter the message:')
            cl.client.publish("python/test",value)
    except KeyboardInterrupt:
        cl.client.disconnect()