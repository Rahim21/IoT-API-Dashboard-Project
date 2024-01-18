# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# models/user_model.py
class User:
    def __init__(self, id, email, password, lastname=None, firstname=None, username=None):
        self.id = id
        self.email = email
        self.password = password
        self.lastname = lastname
        self.firstname = firstname
        self.username = username
