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
            ticket, qr_code = TicketService.add_ticket(ticket_data)
            if ticket:
                return jsonify({"statusCode": 201, "ticket": ticket, "qr_code": qr_code})
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
    
    @staticmethod
    def get_qrcode_by_ticket_id(request_data):
        try:
            ticket_id = request_data.get('ticket_id')
            qr_code = TicketService.get_qrcode_by_ticket_id(ticket_id)
            if not qr_code:
                return jsonify({"statusCode": 200, "error": "Cannot generate QR code. Ticket not found."})
            return jsonify({"statusCode": 200, "qr_code": qr_code})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})

    @staticmethod
    def decode_qr_code(request_data):
        qr_code = request_data.get('qr_code')
        try:
            ticket = TicketService.decode_qr_code(qr_code)
            if not ticket:
                return jsonify({"statusCode": 200, "ticket": None})
            return jsonify({"statusCode": 200, "ticket": ticket})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
    
    @staticmethod
    def verify_ticket(ticket_data):
        try:
            ticket_id = ticket_data.get('ticket_id')
            if TicketService.check_ticket_validity(ticket_id):
                return jsonify({"statusCode": 200, "valid": True})
            else:
                return jsonify({"statusCode": 400, "valid": False})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
    
    @staticmethod
    def validate_ticket(ticket_data):
        try:
            ticket_id = ticket_data.get('ticket_id')
            route_id = ticket_data.get('route_id')

            TicketService.get_ticket(ticket_id)  # Exception handling for invalid ticket
            # RouteService.get_route(route_id)  # Exception handling for invalid route
            
            if TicketService.add_ticket_to_route(ticket_id, route_id):
                return jsonify({"statusCode": 200, "success": "Ticket validated successfully."})
            else:
                return jsonify({"statusCode": 400, "error": "Ticket already validated for this route."})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Ticket validation failed."})
    
    @staticmethod
    def check_boarding_records(ticket_data):
        try:
            ticket_id = ticket_data.get('ticket_id')
            route_id = ticket_data.get('route_id')

            TicketService.get_ticket(ticket_id)  # Exception handling for invalid ticket
            # RouteService.get_route(route_id)  # Exception handling for invalid route

            if TicketService.check_boarding_records(ticket_id, route_id):
                return jsonify({"statusCode": 200, "success": "Boarding records found."})
            else:
                return jsonify({"statusCode": 400, "error": "No boarding records found for this ticket and route."})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Boarding records check failed."})
    
    @staticmethod
    def get_boarding_records(route_data):
        try:
            route_id = route_data.get('route_id')
            records = TicketService.get_boarding_records(route_id)
            if not records:
                return jsonify({"statusCode": 200, "error": "No boarding records found for this route."})
            return jsonify({"statusCode": 200, "routes": records})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Boarding records retrieval failed."})
