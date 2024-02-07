from flask import Flask
import secrets
import requests
from flask import jsonify, render_template, request, flash, redirect, url_for, session
import json
from datetime import datetime
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
secret_key= secrets.token_urlsafe(16)
app.config['SECRET_KEY'] = secret_key

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()
# Récupération de l'adresse IP du serveur depuis les variables d'environnement
server_ip = os.getenv("SERVER_IP")
api_url = f"http://{server_ip}:5010"

from routes.web import *
from routes.auth import *
from routes.ticket import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5020, debug=True)
    



