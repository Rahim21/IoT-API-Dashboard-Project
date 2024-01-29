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
    def calculate_price(ticket_type,person_type): 
        prices = { 
            "1H": 1.0, 
            "2H": 1.8, 
            "1D": 4.0, 
            "1W": 15.0, 
            "1M": 40.0, 
            "6M": 200.0, 
            "1Y": 350.0, 
        }

        type_multiplier = {
            "C": 0.5,   # Enfant
            "A": 1,     # Adulte
            "S": 0.8,   # Etudiant
            "O": 0.7,   # Senior
        }
        ticket_type = prices.get(ticket_type, prices.get("1H"))
        person_type = type_multiplier.get(person_type, type_multiplier.get("A"))
        return ticket_type * person_type

    @staticmethod 
    def create_name(ticket_type,person_type): 
        duration = { 
            "1H": "une heure", 
            "2H": "deux heures", 
            "1D": "une journée", 
            "1W": "une semaine", 
            "1M": "un mois", 
            "6M": "six mois", 
            "1Y": "un an", 
        }

        type = {
            "C": "enfant",   
            "A": "adulte",    
            "S": "étudiant", 
            "O": "senior",
        }
        return f"Ticket {type.get(person_type, 'adulte')} ({duration.get(ticket_type, 'une heure')})"


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
        price = TicketService.calculate_price(ticket_data.get("ticket_type"),ticket_data.get("person_type"))
        name = TicketService.create_name(ticket_data.get("ticket_type"),ticket_data.get("person_type"))

        new_ticket = Ticket(
            name=name,
            ticket_type=ticket_data["ticket_type"],
            created_at=start_date,
            expires_at=expiration_date,
            user_id=user_id,
            price=price,
            person_type=ticket_data.get("person_type")
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
