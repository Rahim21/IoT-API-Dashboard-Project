import datetime
import time
import asyncio
import logging
import aiocoap
import aiocoap.resource as resource
import random
from paho.mqtt import client as mqtt_client
from flask import Flask, render_template,request
from flask import Flask, request, jsonify
import threading

### app flask ###
publisher = Flask(__name__)

# broket mqtt
broker = 'test.mosquitto.org'
port = 1883
topic = "topic/iot"

ticket_id = f'python-mqtt-{random.randint(0, 1000)}'


################## Fonction MQTT ####################

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
    result = client.publish(topic, ticket_id)
    status = result[0]

    if status == 0:
        print(f"Envoi du message `{ticket_id}` au topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

################## Fonction COAP ####################
class Multi(resource.Resource):
    def __init__(self):
        super().__init__()
        self.porte = 0
    async def render_get(self, request):
        msg = aiocoap.Message(payload=b"c'est du GET")
        return msg
    async def render_post(self, request):
        msg = aiocoap.Message(payload=b"c'est du POST")
        return msg
    async def render_put(self, request):
        self.porte = request.payload
        msg = aiocoap.Message(payload=self.porte)
        return msg
    async def render_delete(self, request):
        msg = aiocoap.Message(payload=b"c'est du DELETE")
        return msg

async def coap_server():
    root = resource.Site()
    root.add_resource(('multi',), Multi())
    await aiocoap.Context.create_server_context(root)
    await asyncio.get_running_loop().create_future()

# lancement du flask
def app_flask():
    publisher.run(host="0.0.0.0",debug=True, port=5031, use_reloader=False)

client = connect_mqtt()
client.loop_start()

async def main():
    # serveur flask
    print("Lancement du serveur flask.")
    flask = threading.Thread(target=app_flask)
    flask.start()

    # serveur coap
    print("Lancement du serveur coap.")
    coap = asyncio.create_task(coap_server()) 
    await asyncio.gather(coap)
    flask.join()

# @publisher.route('/tickets/receive_QR', methods=['POST'])
@publisher.route('/tickets/receive_QR')
def receive_QR():
    # request_data = request.get_json()
    # ticket_id = request_data.get('ticket_id')
    print(ticket_id)
    time.sleep(1)
    result = client.publish(topic, ticket_id)
    
    status = result[0]

    if status == 0:
        print(f"Send `{ticket_id}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    return "ok"

@publisher.route('/')
def app():
    return "Prêt à recevoir des requêtes"


if __name__ == '__main__':
    asyncio.run(main())
    
   

    