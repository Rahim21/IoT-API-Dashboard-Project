from flask import Flask
import secrets
import requests
from flask import jsonify, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required, LoginManager, UserMixin

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
secret_key= secrets.token_urlsafe(16)
app.config['SECRET_KEY'] = secret_key
login_manager = LoginManager(app)

ip="10.11.9.49"
api_url = "http://"+ip+":5010"

from routes.web import *
from routes.auth import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    



