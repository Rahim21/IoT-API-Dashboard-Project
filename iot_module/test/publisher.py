#Creation QR
import qrcode

#Lecture QR
from pyzbar.pyzbar import decode
from PIL import Image

#Initialisation MQTT
import random
from paho.mqtt import client as mqtt_client

broker = 'test.mosquitto.org'
port = 1883
topic = "top"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

#Reception Coap
import datetime
import time
import asyncio
import logging
import aiocoap
import aiocoap.resource as resource



### Creation du QR ###

uuid = "069365fd-1568-4e8f-9f3c-f28c078fad6a"

# ticketencode = qrcode.make(uuid)
# type(ticketencode)

# ticketencode.save("Ticket.png")



# ### Déchiffrement du QR ###

# print("")
# print("----------------------------------------")
# ticketdecode = decode(Image.open("Ticket.png"))
# print(ticketdecode)
# print("----------------------------------------")
# print("")
# print("----------------------------------------")
# print("data {}, type {}".format(ticketdecode[0].data,type(ticketdecode[0].data)))
# transform1 = "{}".format(ticketdecode[0].data, type(ticketdecode[0].data))
# msg = transform1.split("'")[1]
# print("----------------------------------------")
# print("")



### Initalisation MQTT et envoi de l'ID ###

# Connexion au broker

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# Publication d'un message sur un topic

def publish(client):
    time.sleep(1)
    
    # Le msg ici est l'UUID reçu après décryption du QR
    result = client.publish(topic, "coucou")

    # result: [0, 1]
    status = result[0]

    if status == 0:
        print(f"Send coucou to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

# Tourne en boucle

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

# --------------------------------------------------

if __name__ == '__main__':
    run()



# ### COAP Receive ###

# class Hello(resource.Resource):
#     def __init__(self):
#         super().__init__()
#     async def render_get(self, request):
#         msg = aiocoap.Message(payload=b"salut les amis")
#         return msg
# logging.basicConfig(level=logging.INFO)
# logging.getLogger("coap-server").setLevel(logging.DEBUG)

# async def main():
#     root = resource.Site()
#     root.add_resource([], Hello())
#     await aiocoap.Context.create_server_context(root)
#     await asyncio.get_running_loop().create_future()

# if __name__ == "__main__":
#     asyncio.run(main())