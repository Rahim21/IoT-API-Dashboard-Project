# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# routes/ticket_route.py
from flask import Blueprint, request
from controllers.ticket_controller import TicketController

ticket_blueprint = Blueprint('ticket', __name__, url_prefix='/tickets')

@ticket_blueprint.route('/', methods=['GET'])
def get_tickets():
    return TicketController.get_tickets()

@ticket_blueprint.route('/<string:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    return TicketController.get_ticket(ticket_id)

@ticket_blueprint.route('/add', methods=['POST'])
def add_ticket():
    return TicketController.add_ticket(request.json)

@ticket_blueprint.route('/<string:ticket_id>/edit', methods=['PUT'])
def edit_ticket(ticket_id):
    return TicketController.edit_ticket(ticket_id, request.json)

@ticket_blueprint.route('/<string:ticket_id>/delete', methods=['DELETE'])
def delete_ticket(ticket_id):
    return TicketController.delete_ticket(ticket_id)


@ticket_blueprint.route('/get_qr_code', methods=['POST'])
def get_qr_code():
    return TicketController.get_qrcode_by_ticket_id(request.json)

@ticket_blueprint.route('/decode_qr_code', methods=['POST'])
def decode_qr_code():
    return TicketController.decode_qr_code(request.json)

@ticket_blueprint.route('/verify_ticket', methods=['POST'])
def verify_ticket():
    return TicketController.verify_ticket(request.json)

@ticket_blueprint.route('/validate_ticket', methods=['POST'])
def validate_ticket():
    return TicketController.validate_ticket(request.json)

@ticket_blueprint.route('/check_boarding_records', methods=['POST'])
def check_boarding_records():
    return TicketController.check_boarding_records(request.json)

@ticket_blueprint.route('/boarding_records', methods=['POST'])
def get_boarding_records():
    return TicketController.get_boarding_records(request.json)