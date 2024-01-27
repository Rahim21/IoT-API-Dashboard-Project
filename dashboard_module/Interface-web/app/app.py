from flask import Flask
import secrets
import requests
from flask import jsonify, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required, LoginManager, UserMixin
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash
from bson import ObjectId

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
secret_key= secrets.token_urlsafe(16)
app.config['SECRET_KEY'] = secret_key

# Configuration de la base de données MongoDB
client = MongoClient('mongodb://10.11.9.49:27017/')
db = client['metro_tickets']
users = db['users']
tickets_collection = db['tickets']

from routes.web import *
from routes.auth import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    



