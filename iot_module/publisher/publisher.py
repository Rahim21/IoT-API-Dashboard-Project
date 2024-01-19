import time
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid):
    print("Message Published")

# mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client()
client.connect("mosquitto", 1883, 60)
# client.connect(mqttBroker)

client.on_publish = on_publish

while True:
    message = "Hello from Publisher"
    result = client.publish("topic/test", message)
    time.sleep(5)
