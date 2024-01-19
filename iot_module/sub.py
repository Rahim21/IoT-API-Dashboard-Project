import paho.mqtt.publish as publish
import time

# Définir le serveur MQTT
mqtt_server = "localhost"
mqtt_port = 1883
mqtt_topic = "test/topic"

# Publier un message toutes les 2 secondes
while True:
    message = "Hello, MQTT!"
    publish.single(mqtt_topic, message, hostname=mqtt_server, port=mqtt_port)
    print(f"Message publié : {message}")
    time.sleep(2)