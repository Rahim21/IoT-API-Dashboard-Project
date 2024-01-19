from app import *
# Route de la page d'acceuil
@app.route("/")
def index():      
    return render_template('index.html')

@app.route("/acheter_ticket", methods=['GET', 'POST'])
def acheter_ticket():
    return render_template('acheter_ticket.html')

@app.route("/acheter_abonnement", methods=['GET', 'POST'])
@login_required
def acheter_abonnement():
    return render_template('acheter_abonnement.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

# Route de la page administrateur
@app.route("/administrator")
@login_required
def administrator():
    return render_template("administrator.html")

# mon profils
@app.route("/profil")
@login_required
def profil():
    return render_template('profil.html')

# simulation
@app.route("/simulation")
@login_required
def simulation():
    return render_template('simulation.html')
