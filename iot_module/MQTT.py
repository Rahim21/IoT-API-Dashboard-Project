import paho.mqtt.client as mqtt
import time

# Définir le serveur MQTT
mqtt_server = "localhost"
mqtt_port = 1883
mqtt_topic = "test/topic"

# Fonction appelée lorsqu'un message est reçu
def on_message(client, userdata, message):
    print(f"Message reçu sur le topic {message.topic}: {message.payload.decode()}")

# Configurer le client MQTT
client = mqtt.Client()
client.on_message = on_message

# Se connecter au serveur MQTT et s'abonner au topic
client.connect(mqtt_server, mqtt_port, 60)
client.subscribe(mqtt_topic)

# Boucle pour rester connecté et recevoir des messages
try:
    client.loop_start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Arrêt du programme.")
    client.disconnect()
    client.loop_stop()