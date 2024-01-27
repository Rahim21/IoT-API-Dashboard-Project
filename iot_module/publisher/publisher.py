import paho.mqtt.publish as publish
import time

# Définir les détails du broker MQTT
broker_address = "test.mosquitto.org"
port = 1883
topic = "topic/test"

# Fonction pour envoyer un message
def publish_message(message):
    publish.single(topic, message, hostname=broker_address, port=port)
    print(f"Message publié: {message}")

if __name__ == "__main__":
    try:
        while True:
            message = "Hello"
            if message.lower() == 'exit':
                break
            publish_message(message)
    except KeyboardInterrupt:
        print("Interruption du programme.")
