# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# utils.py
from pymongo import MongoClient
import socket

def connect_mongodb() -> MongoClient:
    # Essayer de se connecter à MongoDB en utilisant localhost (127.0.0.1)
    try:
        mongo_client = MongoClient('mongodb://root:example@10.11.10.17:27017') # IP LOCAL
        mongo_client.server_info()  # Vérifier la connexion
        print("Connecté à MongoDB en utilisant localhost (10.11.9.49)")
        return mongo_client
    except Exception as e1:
        print(f"Erreur lors de la connexion à MongoDB en utilisant localhost : {e1}")

    # Si la connexion à MongoDB en utilisant localhost échoue, essayer avec l'adresse IP de la connexion SSH
    try:
        ssh_ip = socket.gethostbyname(socket.gethostname()) # IP SSH
        mongo_client = MongoClient(f'mongodb://root:example@10.11.9.49:27017')
        mongo_client.server_info()  # Vérifier la connexion
        print(f"Connecté à MongoDB en utilisant l'adresse IP de la connexion SSH : 10.11.9.49")
        return mongo_client
    except Exception as e2:
        print(f"Erreur lors de la connexion à MongoDB en utilisant l'adresse IP de la connexion SSH : 10.11.9.49")

    # Si toutes les tentatives de connexion échouent, retourner None
    return None
