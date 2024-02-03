# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# models/user_model.py
from app import *
class User():
    def __init__(self, user_id, is_active=True):
        self.user_id = user_id
        self.is_active = is_active

    def get_id(self):
        return str(self.user_id)