#MQTT
import random
from paho.mqtt import client as mqtt_client

broker = 'test.mosquitto.org'
port = 1883
topic = "top"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

#Requetes HTTP
import requests


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

    # URL de l'API REST
        # api_url = f"https://10.11.9.209:5051/verifier_expiration/{s}"

        # Paramètres à inclure dans la requête GET
        # parametres = {"uuid": s}

        # Envoi de la requête GET à l'API
        # try:
        #     response = requests.get(api_url, params=parametres)
        #     response.raise_for_status()  # Gère les erreurs HTTP

        #     api_data = response.json()  # Si la réponse est en JSON
        #     print("Réponse de l'API :", api_data)
            
        # except requests.exceptions.RequestException as e:
        #     print(f"Erreur lors de la requête vers l'API : {e}")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()

    try:
        while True:
            # Continue à écouter en boucle
            pass
    except KeyboardInterrupt:
        print("Arrêt du programme.")

if __name__ == '__main__':
    run()


# ### Coap ###
# import logging
# import asyncio
# import aiocoap
# import aiocoap.numbers.codes as codes


# logging.basicConfig(level=logging.INFO)

# async def main():
#     protocol = await aiocoap.Context.create_client_context()
#     request = aiocoap.Message(code=codes.GET, uri="coap://localhost")
                              
#     try:
#         response = await protocol.request(request).response

#     except Exception as e:
#         print("Failed to fetch resource:")
#         print(e)
    
#     else:
#         print("Result: %s\n%r"%(response.code, response.payload))

#     if __name__ == "__main__":
#         asyncio.run(main())