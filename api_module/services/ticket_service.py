# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# services/ticket_service.py
from models.ticket_model import Ticket
from flask import g
from bson import ObjectId
from datetime import datetime, timedelta

class TicketService:

    @staticmethod
    def get_tickets():
        collection = g.db["tickets"]
        tickets = collection.find()
        return str(list(tickets))

    @staticmethod
    def get_ticket(ticket_id):
        collection = g.db["tickets"]
        ticket = collection.find_one({"_id": ObjectId(ticket_id)})
        return str(ticket)

    @staticmethod
    def add_ticket(ticket_data):
        collection = g.db["tickets"]

        # Convertir la chaîne user_id en ObjectId si elle est non vide, sinon None
        user_id = ObjectId(ticket_data["user_id"]) if ticket_data.get("user_id") else None
        # Utiliser la date actuelle par défaut si start_date n'est pas spécifiée (début d'un abonnement)
        start_date = datetime.utcnow().isoformat() if not ticket_data.get("start_date") else ticket_data["start_date"]
        # Calculer la date d'expiration en fonction de la durée de validité définie par ticket_type (1H, 2H, 1J, 1M)
        expiration_duration = TicketService.calculate_expiration_duration(ticket_data.get("ticket_type"))
        expiration_date = (
            datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%f") + expiration_duration
        ).isoformat()

        new_ticket = Ticket(
            name=ticket_data["name"],
            ticket_type=ticket_data["ticket_type"],
            created_at=start_date,
            # expires_at=(datetime.utcnow() + timedelta(hours=1)).isoformat(),
            expires_at=expiration_date,
            user_id=user_id
        )
        collection.insert_one(new_ticket.__dict__)
        return str(new_ticket.__dict__)
    
    # méthode à utiliser dans cette classe
    @staticmethod
    def calculate_expiration_duration(ticket_type):
        durations = {
            "1H": timedelta(hours=1),
            "2H": timedelta(hours=2),
            "1D": timedelta(days=1),
            "1W": timedelta(days=7),
            "1M": timedelta(days=30),
            "6M": timedelta(days=180),
            "1Y": timedelta(days=365),
        }
        # Valeur par défaut si le ticket_type n'est pas spécifié ou non reconnu
        return durations.get(ticket_type, timedelta(hours=1))

    @staticmethod
    def edit_ticket(ticket_id, updated_data):
        collection = g.db["tickets"]
        updated_ticket = collection.find_one_and_update(
            {"_id": ObjectId(ticket_id)},
            {"$set": updated_data},
            return_document=True
        )
        return str(updated_ticket)

    @staticmethod
    def delete_ticket(ticket_id):
        collection = g.db["tickets"]
        deleted_ticket = collection.find_one_and_delete({"_id": ObjectId(ticket_id)})
        return str(deleted_ticket)
