import logging
import asyncio
import aiocoap
import aiocoap.numbers.codes as codes
import aiocoap.resource as resource
import random
from paho.mqtt import client as mqtt_client
from flask import Flask, render_template,request
from flask import Flask, request, jsonify


broker = 'test.mosquitto.org'
port = 1883
topic = "topic/iot"

client_id = f'python-mqtt-{random.randint(0, 100)}'

API_URL = "http://10.11.10.17:5010"

################## Fonction MQTT ####################
def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

def connect_mqtt() -> mqtt_client:
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


async def send_coap_message():
    protocol = await aiocoap.Context.create_client_context()
    request = aiocoap.Message(code=aiocoap.numbers.codes.Code.GET, uri="coap://localhost/multi")
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print("Failed to fetch resource:")
        print(e)
    else:
        print("Result: %s\n%r"%(response.code, response.payload))

def on_message(client, userdata, msg):
        s = str(msg.payload.decode("utf-8"))
        print(f"Received `{s}` from `{msg.topic}` topic")

        asyncio.run(send_coap_message())
    

def subscribe(client: mqtt_client):
    client.subscribe(topic)
    client.on_message = on_message


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

    
logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

async def main_coap():
    root = resource.Site()
    root.add_resource(['multi'], Multi())

    await aiocoap.Context.create_server_context(root)
    await asyncio.get_running_loop().create_future()

async def main_mqtt():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()

async def main():
    await asyncio.gather(main_coap(), main_mqtt())


if __name__ == '__main__':
    print("Lancement du serveur CoAP.")
    asyncio.run(main())
  
 