# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# services/ticket_service.py
from api_module.models.ticket_model import Ticket
from flask import jsonify

class TicketService:

    @staticmethod
    def get_tickets():
        pass

    @staticmethod
    def get_ticket(ticket_id):
        pass

    @staticmethod
    def add_ticket(ticket_data):
        pass

    @staticmethod
    def edit_ticket(ticket_id, updated_data):
        pass

    @staticmethod
    def delete_ticket(ticket_id):
        pass