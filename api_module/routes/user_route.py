# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# routes/user_route.py
from flask import Blueprint, request, redirect, url_for
from controllers.user_controller import UserController

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users/register', methods=['POST'])
def register():
    return UserController.register_user(request.json)

@user_blueprint.route('/users/login', methods=['POST'])
def login():
    return UserController.login_user()

@user_blueprint.route('/users/logout', methods=['GET'])
def logout():
    return UserController.logout_user()

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    return UserController.get_users()

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@user_blueprint.route('/users/edit/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    return UserController.edit_user(user_id, request.json)

@user_blueprint.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)
