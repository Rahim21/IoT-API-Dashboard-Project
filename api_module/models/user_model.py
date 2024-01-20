# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# models/user_model.py
class User:
    def __init__(self, email, password, lastname=None, firstname=None, username=None, is_active=True):
        self.email = email
        self.password = password
        self.lastname = lastname
        self.firstname = firstname
        self.username = username
        self.is_active = is_active