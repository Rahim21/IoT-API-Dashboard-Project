# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# app.py
from flask import Flask
from flask_cors import CORS
from routes.user_route import user_blueprint
from routes.ticket_route import ticket_blueprint

app = Flask(__name__)
app.secret_key = 'IAD'

CORS(app) # accepter des requêtes provenant de domaines différents

app.register_blueprint(user_blueprint)
# app.register_blueprint(ticket_blueprint)

@app.route('/')
def hello_world():
    return 'IAD: IoT-API-Dashboard'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
