# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# controllers/user_controller.py
from flask import jsonify, request
from services.user_service import UserService

class UserController:

    @staticmethod
    def register_user(user_data):
        try:
            user = UserService.create_user(user_data)
            if user:
                return jsonify({"statusCode": 201, "user": user})
            else:
                return jsonify({"statusCode": 400, "error": "L'utilisateur existe déjà."})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})

    @staticmethod
    def login_user():
        try:
            data = request.get_json()
            user = UserService.login_user(data['email'], data['password'])
            if user:
                    return jsonify({"statusCode": 201, "user": user})
            else:
                return jsonify({"statusCode": 400, "error": "Identifiants incorrects."})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})

    @staticmethod
    def get_users():
        try:
            users = UserService.get_users()
            return jsonify({"statusCode": 200, "users": users})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})

    @staticmethod
    def get_user(user_id):
        try:
            user = UserService.get_user_by_id(user_id)
            if not user:
                return jsonify({"statusCode": 200, "user": None})
            return jsonify({"statusCode": 200, "user": user})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
   
    @staticmethod 
    def edit_user(user_id, updated_data):
        try:
            user = UserService.update_user(user_id, updated_data)
            if not user:
                return jsonify({"statusCode": 200, "user": None})
            return jsonify({"statusCode": 200, "user": user})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})

    @staticmethod
    def deactivate_user(user_id):
        try:
            user = UserService.deactivate_user(user_id)
            if not user:
                return jsonify({"statusCode": 200, "user": None})
            return jsonify({"statusCode": 200, "user": user})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
    
    @staticmethod
    def delete_user(user_id):
        try:
            user = UserService.delete_user(user_id)
            if not user:
                return jsonify({"statusCode": 200, "user": None})
            return jsonify({"statusCode": 200, "user": user})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
        
    @staticmethod
    def get_user_tickets(user_id):
        try:
            tickets = UserService.get_user_tickets(user_id)
            return jsonify({"statusCode": 200, "tickets": tickets})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
