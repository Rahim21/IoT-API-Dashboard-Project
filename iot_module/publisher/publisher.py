#Reception Coap
import datetime
import time
import asyncio
import logging
import aiocoap
import aiocoap.resource as resource
#Initialisation MQTT
import random
from paho.mqtt import client as mqtt_client

broker = 'test.mosquitto.org'
port = 1883
topic = "topic/iot"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'


uuid = "069365fd-1568-4e8f-9f3c-f28c078fad6a"

### Initalisation MQTT et envoi de l'ID ###

# Connexion au broker
def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# Publication d'un message sur un topic
def publish(client):
    time.sleep(1)
    # Le msg ici est l'UUID reçu après décryption du QR
    result = client.publish(topic, client_id)
    # result: [0, 1]
    status = result[0]

    if status == 0:
        print(f"Send `{client_id}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

# Tourne en boucle

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

# --------------------------------------------------


# ### COAP Receive ###

class Hello(resource.Resource):
    def __init__(self):
        super().__init__()
    async def render_get(self, request):
        msg = aiocoap.Message(payload=b"salut les amis")
        return msg
logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

async def main():
    root = resource.Site()
    root.add_resource([], Hello())
    await aiocoap.Context.create_server_context(root)
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++hello 3" )
    await asyncio.get_running_loop().create_future()
    
    print("////////////////////////////////////////////////////////////////////////////////hello 3" )


if __name__ == '__main__':
    print("Lancement du programme de publication MQTT.")
    run()
    # print("Lancement du serveur CoAP.")
    # asyncio.run(main())





    