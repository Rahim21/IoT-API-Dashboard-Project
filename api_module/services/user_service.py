# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# services/user_service.py
from models.user_model import User
from flask import jsonify

class UserService:

    @staticmethod
    def create_user(user_data):
        users = UserService.get_users()
        return None if users and any(user['email'] == user_data['email'] for user in users) else None
        
        # Verifier si l'email n'est pas en conflit mais différement (faire selon mondoDB)
        # Ajouter l'enregistrement de l'utilisateur dans la base de données mondoDB
        pass

    @staticmethod
    def get_user_by_credentials(email, password):
        # Récupérer l'utilisateur à l'aide du mail et mot de passe
        pass

    @staticmethod
    def login_user(user_id):
        # Connexion de l'utilisateur (Jeton JWT ou Session & Cookie lib python)
        pass
    
    @staticmethod
    def logout_user(response):
        # Méthode de désconnexion
        pass

    @staticmethod
    def get_users():
        # Récupérer tous les utilisateurs de la base de données mondoDB
        pass

    @staticmethod
    def get_user_by_id(user_id):
        # Récupérer l'utilisateur à l'aide de son identifiant
        pass

    @staticmethod
    def update_user(user_id, updated_data):
        # Mettre à jour les données de l'utilisateur à l'aide de son identifiant
        pass

    @staticmethod
    def delete_user(user_id):
        # Supprimer ou rendre inactif le status de l'utilisateur à l'aide de son identifiant
        pass

    @staticmethod
    def _save_users(users):
        # Enregistrer des données de l'utilisateur dans la base de données mondoDB
        pass
