### Coap ###
import logging
import asyncio
import aiocoap
import aiocoap.numbers.codes as codes
#MQTT
import random
from paho.mqtt import client as mqtt_client

broker = 'test.mosquitto.org'
port = 1883
topic = "top"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'



### MQTT ###

# --------------------------------------------------

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# --------------------------------------------------

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        s = str(msg.payload.decode("utf-8"))
        print(f"Received `{s}` from `{msg.topic}` topic")
        
    client.subscribe(topic)
    client.on_message = on_message


logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await aiocoap.Context.create_client_context()
    request = aiocoap.Message(code=codes.GET, uri="coap://localhost")
                              
    try:
        response = await protocol.request(request).response

    except Exception as e:
        print("Failed to fetch resource:")
        print(e)
    
    else:
        print("Result: %s\n%r"%(response.code, response.payload))


def run():
    client = connect_mqtt()
    
    subscribe(client)
    
    client.loop_start()
   
    print("Lancement du programme de souscription CoAP.")
    asyncio.run(main())
    try:
        while True:
            # Continue à écouter en boucle
            pass
    except KeyboardInterrupt:
        print("Arrêt du programme.")

if __name__ == '__main__':
    print("Lancement du programme de souscription MQTT.")
    run()