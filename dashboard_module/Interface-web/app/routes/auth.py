from app import *

class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        # Example: fetch user from the database by user_id
        return users.get(user_id)



#initialisation de login_manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    user_data = users.find_one({'_id': ObjectId(user_id)})
    if user_data:
        return User(user_data['_id'], user_data['username'], user_data['password'])
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = None

        user_data = users.find_one({'username': username})

        if user_data:
            if(check_password_hash(user_data['password'], password)):
                user = User(user_data['_id'], user_data['username'], user_data['password'])

        if user:
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Route pour la création d'un compte
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
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

        # Hash the password before storing it
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        # Insert the new user into the MongoDB 'users' collection
        user_data = {"username": username, "password": hashed_password}
        
        result = users.insert_one(user_data)

        if result.inserted_id:
            # Log in the user after successful registration
            new_user = User(result.inserted_id, username, hashed_password)
            login_user(new_user)
            
            flash("Registration successful! You are now logged in.", "success")
            return redirect(url_for("index"))
        else:
            flash("Error occurred during registration. Please try again.", "danger")

    return render_template("register.html")
