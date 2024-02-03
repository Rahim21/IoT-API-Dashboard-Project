from app import *

@login_manager.user_loader
def load_user(user_id):
    response = requests.get(api_url+"/users/"+user_id)
    if response.status_code == 200:
        user = User(response.json())
        return user
    else:
        return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = None
        
        data = {"email": email, "password": password}

        response = requests.post(api_url+"/users/login", json=data)
        
        if response.status_code == 201:
            flash('Login successful', 'success')
            return redirect(url_for('index'))
        else:
            flash('An error occurred. Please try again later.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    response = requests.get(api_url+"/users/logout")
    if response.status_code == 200:
        logout_user()
        flash('Logout successful', 'success')
    else:
        flash('An error occurred. Please try again later.', 'danger')
    return redirect(url_for('login'))

# Route pour la création d'un compte
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if the username already exists
        if users.find_one({"username": username}):
            flash("Username already exists. Please choose a different username.", "danger")
            return redirect(url_for("register"))

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match. Please enter matching passwords.", "danger")
            return redirect(url_for("register"))
        
        data = {"username": username, "firstname": firstname, "lastname": lastname, "email": email, "password": password}
        
        # Create a new user
        
        response = requests.post(api_url+"/users/register", json=data)
        
        if response.status_code == 201:
            flash("Account created successfully. Please login.", "success")
            return redirect(url_for("login"))
        else:
            flash("An error occurred. Please try again later.", "danger")
            return redirect(url_for("register"))

    return render_template("register.html")

@app.route("/edit_user", methods=["POST"])
def edit_user():
    if request.method == "POST":
        username = request.form.get("username")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if(password != confirm_password):
            flash("Passwords do not match. Please enter matching passwords.", "danger")
            return redirect(url_for("index"))
        
        data = {"username": username, "firstname": firstname, "lastname": lastname, "email": email, "password": password}

        response = requests.put(api_url+"/users/"+current_user.id+"/edit", json=data)
        
        if response.status_code == 200:
            flash("Account edited successfully.", "success")
            return redirect(url_for("index"))
        else:
            flash("An error occurred. Please try again later.", "danger")
            return redirect(url_for("index"))

    return render_template("index.html")

@app.route("/get_users", methods=["POST"])
def get_users():
    
    response = requests.get(api_url+"/users/")
    
    reference = request.headers.get("Referer")
    
    if response.status_code == 200:
        flash("Account edited successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)
    
@app.route("/get_user", methods=["POST"])
def get_user():
    
    user_id = current_user.id
   
    
    if response.status_code == 200:
        flash("Account edited successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)
    
@app.route("/get_user_tickets", methods=["POST"])
def get_user_tickets():
    
    user_id = current_user.id
    
    response = requests.get(api_url+"/users/"+user_id+"/tickets")
    
    reference = request.headers.get("Referer")
    
    if response.status_code == 200:
        flash("Account edited successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)

@app.route("/deactivate_user/<user_id>", methods=["POST" , "GET"])
def deactivate_user():
    user_id = request.form.get("user_id")
    
    response = requests.put(api_url+"/users/"+user_id+"/deactivate")
    
    reference = request.headers.get("Referer")
    
    if response.status_code == 200:
        flash("Account deactivated successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)
    
@app.route("/delete_user/<user_id>", methods=["POST" , "GET"])
def delete_user():
    
    user_id = request.form.get("user_id")
    
    response = requests.delete(api_url+"/users/"+user_id+"/delete")
    
    reference = request.headers.get("Referer")
    
    if response.status_code == 200:
        flash("Account deleted successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)