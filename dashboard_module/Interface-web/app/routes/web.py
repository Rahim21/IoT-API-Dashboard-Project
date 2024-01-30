from app import *
# Route de la page d'acceuil
@app.route("/")
def index():      
    return render_template('index.html')


@app.route("/acheter_ticket", methods=['GET', 'POST'])
@login_required
def acheter_ticket():
    return render_template('acheter_ticket.html')


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

# Route de la page administrateur
@app.route("/administrator")
@login_required
def administrator():
     
    response = requests.get(api_url+"/users/")
    
    if response.status_code == 200:
        users = response.json()
        return render_template("administrator.html", users=users)
    else:
        flash("An error occurred. Please try again later.", "danger")
    return render_template("administrator.html")

# mon profils
@app.route("/profil")
@login_required
def profil():
    
    response = requests.get(api_url+"/tickets/")
    
    return render_template('profil.html', tickets=response.json())

# simulation
@app.route("/simulation")
@login_required
def simulation():
    return render_template('simulation.html')
