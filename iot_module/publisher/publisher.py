import datetime
import time
import asyncio
import logging
import aiocoap
import aiocoap.resource as resource
import random
from paho.mqtt import client as mqtt_client

broker = 'test.mosquitto.org'
port = 1883
topic = "topic/iot"

# generate client ID with pub prefix randomly
ticket_id = f'python-mqtt-{random.randint(0, 1000)}'

### Initalisation MQTT et envoi de l'ID ###

# Connexion au broker
def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

def connect_mqtt():
    client = mqtt_client.Client(ticket_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# Publication d'un message sur un topic
def publish(client):
    time.sleep(1)
    # Le msg ici est l'UUID reçu après décryption du QR
    result = client.publish(topic, ticket_id)
    
    status = result[0]

    if status == 0:
        print(f"Send `{ticket_id}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")



def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    print("Lancement du programme de publication MQTT.")
    run()
   





    