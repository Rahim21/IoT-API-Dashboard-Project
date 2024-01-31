from app import *
# Route de la page d'acceuil
@app.route("/")
def index():      
    return render_template('index.html')


@app.route("/acheter_ticket", methods=['GET', 'POST'])
def acheter_ticket():
    return render_template('acheter_ticket.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

# Route de la page administrateur
@app.route("/administrator")
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
def profil():
    response = requests.get(api_url + "/tickets/")
    if response.status_code in [200, 201]:
        tickets = response.json()["tickets"]
        ticket_json = json.dumps(tickets)
        return render_template('profil.html', tickets=ticket_json)
    return render_template('profil.html')

# simulation
@app.route("/simulation")
def simulation():
    return render_template('simulation.html')
