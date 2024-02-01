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
        return render_template('profil.html', tickets=tickets)
    return render_template('profil.html')

@app.route("/tickets")
def tickets():
    response = requests.get(api_url + "/tickets/")
    if response.status_code in [200, 201]:
        tickets = response.json()["tickets"]
        #format date
        for ticket in tickets:
            date_created = datetime.fromisoformat(ticket["created_at"])
            date_expired = datetime.fromisoformat(ticket["expires_at"])
            ticket["created_at"] = date_created.strftime("%d/%m/%Y %H:%M:%S")
            ticket["expires_at"] = date_expired.strftime("%d/%m/%Y %H:%M:%S")
        return render_template('tickets.html', tickets=tickets)
    return render_template('tickets.html')

# simulation
@app.route("/simulation")
def simulation():
    return render_template('simulation.html')
