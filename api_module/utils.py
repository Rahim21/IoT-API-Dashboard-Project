# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# utils.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()
# Récupération de l'adresse IP du serveur depuis les variables d'environnement
server_ip = os.getenv("SERVER_IP")

def connect_mongodb() -> MongoClient:
    # Connexion à MongoDB en utilisant l'ip du fichier d'environnement
    try:
        if server_ip == '127.0.0.1':
            mongo_client = MongoClient(f'mongodb://{server_ip}:27017') # IP LOCAL
        else:
            mongo_client = MongoClient(f'mongodb://root:example@{server_ip}:27017')
        print(f"Connecté à MongoDB en utilisant l'adresse : ({server_ip})")
        return mongo_client
    except Exception as e1:
        print(f"Erreur lors de la connexion à MongoDB en utilisant localhost : {e1}")
    return None
