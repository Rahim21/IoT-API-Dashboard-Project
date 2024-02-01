# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# app.py
from flask import Flask, g
from flask_cors import CORS

from utils import connect_mongodb
from routes.user_route import user_blueprint
from routes.ticket_route import ticket_blueprint
from routes.statistics_route import statistics_blueprint

app = Flask(__name__)

app.secret_key = 'IAD'
CORS(app) # accepter des requêtes provenant de domaines différents

# Connexion à MongoDB
mongo_client = connect_mongodb()
db = mongo_client['TicketLink']

# On stocke l'objet db dans le contexte global g
@app.before_request
def before_request():
    g.mongo_client = mongo_client
    g.db = db

# Méthode pour lister les bases de données et collections
# print(mongo_client.list_database_names())
# print(db.list_collection_names())

# Routes
app.register_blueprint(user_blueprint, prefix='/users')
app.register_blueprint(ticket_blueprint, prefix='/tickets')
app.register_blueprint(statistics_blueprint, prefix='/statistics')

@app.route('/')
def hello_world():
    return 'TicketLink API: For IoT-API-Dashboar Project'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
