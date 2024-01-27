# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# models/ticket_model.py
from bson import ObjectId
class Ticket:
    def __init__(self, ticket_type, name, created_at, expires_at, price, person_type, user_id=None):
        self.name = name
        self.type = ticket_type
        self.created_at = created_at
        self.expires_at = expires_at
        self.user_id = ObjectId(user_id) if user_id else None
        self.price = price
        self.person_type = person_type