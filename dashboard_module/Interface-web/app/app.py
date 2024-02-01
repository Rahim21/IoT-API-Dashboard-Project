from flask import Flask
import secrets
import requests
from flask import jsonify, render_template, request, flash, redirect, url_for, session
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
secret_key= secrets.token_urlsafe(16)
app.config['SECRET_KEY'] = secret_key

ip="127.0.0.1"
api_url = "http://"+ip+":5010"

from routes.web import *
from routes.auth import *
from routes.ticket import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    



