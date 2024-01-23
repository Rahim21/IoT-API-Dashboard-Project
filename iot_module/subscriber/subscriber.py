import paho.mqtt.client as mqtt
import time

# Définir les détails du broker MQTT
broker_address = "test.mosquitto.org"
port = 1883
topic = "topic/test"

# Fonction de rappel lorsqu'un message est reçu
def on_message(client, userdata, msg):
    print(f"Message reçu sur le sujet '{msg.topic}': {msg.payload.decode()}")

if __name__ == "__main__":
    # Créer une instance du client MQTT
    client = mqtt.Client()

    # Configurer la fonction de rappel pour la réception des messages
    client.on_message = on_message

    # Se connecter au broker MQTT
    client.connect(broker_address, port=port)

    # S'abonner au sujet spécifié
    client.subscribe(topic)

    # Démarrer la boucle de communication
    client.loop_start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Arrêter la boucle de communication et déconnecter le client en cas d'interruption du programme
        client.loop_stop()
        client.disconnect()
        print("Interruption du programme.")
