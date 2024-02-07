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
    if "user_id" in session:
        reponse_total_number_tickets = requests.get(api_url + "/statistics/total_number_tickets")
        reponse_repartition_types_tickets = requests.get(api_url + "/statistics/repartition_types_tickets")
        reponse_number_expired_tickets = requests.get(api_url + "/statistics/number_expired_tickets")
        reponse_turnover = requests.get(api_url + "/statistics/turnover")
        reponse_most_active_users = requests.get(api_url + "/statistics/most_active_users")
        reponse_peak_usage_times = requests.get(api_url + "/statistics/peak_usage_times")
        reponse_repartition_types_personnes = requests.get(api_url + "/statistics/repartition_types_personnes")
        return render_template('dashboard.html', 
            total_number_tickets=reponse_total_number_tickets.json(),
            repartition_types_tickets=reponse_repartition_types_tickets.json(),
            number_expired_tickets=reponse_number_expired_tickets.json(),
            turnover=reponse_turnover.json(),
            most_active_users=reponse_most_active_users.json(),
            peak_usage_times=reponse_peak_usage_times.json(),
            repartition_types_personnes=reponse_repartition_types_personnes.json()
        )
    else:
            return redirect(url_for('login'))

# Route de la page administrateur
@app.route("/administrator")
def administrator():
    if "user_id" in session and session["user_role"] == "admin":
        response_users = requests.get(api_url+"/users/")
        if response_users.status_code == 200:
            response = requests.get(api_url + "/tickets/")
            if response.status_code in [200, 201]:
                tickets = response.json()["tickets"]
                #format date
                for ticket in tickets:
                    reponse_qr_code = requests.post(api_url + "/tickets/get_qr_code", json={"ticket_id": ticket["_id"]})   
                    #ajouter le qr code au ticket
                    ticket["qr_code"] = reponse_qr_code.json()["qr_code"]
                    date_created = datetime.fromisoformat(ticket["created_at"])
                    date_expired = datetime.fromisoformat(ticket["expires_at"])
                    ticket["created_at"] = date_created.strftime("%d/%m/%Y %H:%M:%S")
                    ticket["expires_at"] = date_expired.strftime("%d/%m/%Y %H:%M:%S")
                users = response_users.json()
                return render_template("administrator.html", users=users,tickets=tickets)
        else:
            flash("An error occurred. Please try again later.", "danger")
        return render_template("administrator.html")
    else:
        flash("You must be logged in to access this page.", "danger")
        return redirect(url_for('login'))

# mon profils
@app.route("/profil")
def profil():
    if "user_id" in session:
        response = requests.get(api_url + "/tickets/")
        if response.status_code in [200, 201]:
            tickets = response.json()["tickets"]
            return render_template('profil.html', tickets=tickets)
        return render_template('profil.html')
    else:
        return redirect(url_for('login'))

@app.route("/tickets")
def tickets():
    if "user_id" in session:
        user_id = session["user_id"]
        response = requests.get(api_url+"/users/"+user_id+"/tickets")
        if response.status_code in [200, 201]:
            tickets = response.json()["tickets"]
            #format date
            for ticket in tickets:
                reponse_qr_code = requests.post(api_url + "/tickets/get_qr_code", json={"ticket_id": ticket["_id"]})   
                #ajouter le qr code au ticket
                ticket["qr_code"] = reponse_qr_code.json()["qr_code"]
                date_created = datetime.fromisoformat(ticket["created_at"])
                date_expired = datetime.fromisoformat(ticket["expires_at"])
                ticket["created_at"] = date_created.strftime("%d/%m/%Y %H:%M:%S")
                ticket["expires_at"] = date_expired.strftime("%d/%m/%Y %H:%M:%S")
            return render_template('tickets.html', tickets=tickets)
        return render_template('tickets.html')
    else:
        return redirect(url_for('login'))

# simulation
@app.route("/simulation")
def simulation():
    return render_template('simulation.html')
