# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# controllers/ticket_controller.py
from flask import jsonify, request
from services.ticket_service import TicketService

class TicketController:

    @staticmethod
    def get_tickets():
        try:
            tickets = TicketService.get_tickets()
            return jsonify({"statusCode": 200, "tickets": tickets})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})

    @staticmethod
    def get_ticket(ticket_id):
        try:
            ticket = TicketService.get_ticket(ticket_id)
            if not ticket:
                return jsonify({"statusCode": 200, "ticket": None})
            return jsonify({"statusCode": 200, "ticket": ticket})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})

    @staticmethod
    def add_ticket(ticket_data):
        try:
            ticket = TicketService.add_ticket(ticket_data)
            if ticket:
                return jsonify({"statusCode": 201, "ticket": ticket})
            else:
                return jsonify({"statusCode": 400, "error": "Erreur lors de l'ajout du film."})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})

    @staticmethod
    def edit_ticket(ticket_id, updated_data):
        try:
            ticket = TicketService.edit_ticket(ticket_id, updated_data)
            if not ticket:
                return jsonify({"statusCode": 200, "ticket": None})
            return jsonify({"statusCode": 200, "ticket": ticket})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})

    @staticmethod
    def delete_ticket(ticket_id):
        try:
            ticket = TicketService.delete_ticket(ticket_id)
            if not ticket:
                return jsonify({"statusCode": 200, "ticket": None})
            return jsonify({"statusCode": 200, "ticket": ticket})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
