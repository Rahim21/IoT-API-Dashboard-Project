from app import app, api_url
import requests
from flask import jsonify, render_template, request, flash, redirect, url_for
from flask_simplelogin import Message, SimpleLogin, get_username, login_required

# Route de la page d'acceuil
@app.route("/")
def index():      
    return render_template('index.html')

# Route pour la création d'un compte
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/acheter_ticket", methods=['GET', 'POST'])
def acheter_ticket():
    return render_template('acheter_ticket.html')

@app.route("/acheter_abonnement", methods=['GET', 'POST'])
def acheter_abonnement():
    return render_template('acheter_abonnement.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

# Route de la page administrateur
@app.route("/administrator")
def administrator():
    return render_template("administrator.html")

# mon profils
@app.route("/profil")
def profil():
    return render_template('profil.html')
