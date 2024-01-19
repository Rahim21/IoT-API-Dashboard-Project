import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("topic/test")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Ajout d'une pause de 2 secondes avant la connexion
time.sleep(2)

# Connexion au broker Mosquitto
client.connect("mosquitto", 1883, 60)

# Lancement de la boucle de réception des messages
client.loop_forever()
