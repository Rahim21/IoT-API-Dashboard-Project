# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# routes/user_route.py
from flask import g, Blueprint, request, redirect, url_for
from controllers.user_controller import UserController

user_blueprint = Blueprint('user', __name__, url_prefix='/users')

@user_blueprint.route('/register', methods=['POST'])
def register():
    return UserController.register_user(request.json)

@user_blueprint.route('/login', methods=['POST'])
def login():
    return UserController.login_user()

@user_blueprint.route('/logout', methods=['GET'])
def logout():
    return UserController.logout_user()

@user_blueprint.route('/', methods=['GET'])
def get_users():
    return UserController.get_users()

@user_blueprint.route('/<string:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@user_blueprint.route('/<string:user_id>/edit', methods=['PUT'])
def edit_user(user_id):
    return UserController.edit_user(user_id, request.json)

@user_blueprint.route('/<string:user_id>/deactivate', methods=['PUT'])
def deactivate_user(user_id):
    return UserController.deactivate_user(user_id)

@user_blueprint.route('/<string:user_id>/delete', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)

@user_blueprint.route('/<string:user_id>/tickets', methods=['GET'])
def get_user_tickets(user_id):
    return UserController.get_user_tickets(user_id)

