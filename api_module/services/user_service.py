# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# services/user_service.py
from models.user_model import User
from flask import g
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:

    @staticmethod
    def create_user(user_data) :
        collection = g.db["users"]
        
        # Vérification si l'utilisateur existe déjà dans la base de données
        existing_user = collection.find_one({"email": user_data["email"]})

        if existing_user:
            return None

        # Création d'un nouvel utilisateur
        new_user = User(
            email=user_data["email"],
            password=user_data["password"],
            lastname=user_data.get("lastname"),
            firstname=user_data.get("firstname"),
            username=user_data.get("username"),
            is_active=True
        )
        
        # Mot de passe  à crypté
        new_user.password = generate_password_hash(new_user.password, method='pbkdf2:sha256')

        # Enregistrement de l'utilisateur dans la base de données MongoDB
        result = collection.insert_one(new_user.__dict__)
        inserted_id = str(result.inserted_id)

        return str(new_user.__dict__)

    @staticmethod
    def get_user_by_credentials(email, password):
        # Récupération de l'utilisateur à l'aide du mail et mot de passe
        collection = g.db["users"]
        user = collection.find_one({"email": email, "password": password})
        return user

    @staticmethod
    def login_user(user_id):
        # Connexion de l'utilisateur (Jeton JWT ou Session & Cookie lib python)
        # Bien vérifier que is_active = True
        pass

    @staticmethod
    def logout_user(response):
        # Méthode de désconnexion
        pass

    @staticmethod
    def get_users():
        # Récupération de tous les utilisateurs de la base de données MongoDB
        collection = g.db["users"]
        users = collection.find()
        return str(list(users))

    @staticmethod
    def get_user_by_id(user_id):
        # Récupération de l'utilisateur à l'aide de son identifiant
        collection = g.db["users"]
        user = collection.find_one({"_id": ObjectId(user_id)})
        return str(user)

    @staticmethod
    def update_user(user_id, updated_data):
        # Mise à jour de l'utilisateur à l'aide de son identifiant
        collection = g.db["users"]
        updated_user = collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": updated_data},
            return_document=True
        )
        return str(updated_user)

    @staticmethod
    def deactivate_user(user_id):
        # Rendre inactif l'utilisateur à l'aide de son identifiant
        collection = g.db["users"]
        deactivated_user = collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": {"is_active": False}},
            return_document=True
        )
        return str(deactivated_user)
    
    @staticmethod
    def delete_user(user_id):
        # Suppression de l'utilisateur à l'aide de son identifiant
        collection = g.db["users"]
        deleted_user = collection.find_one_and_delete({"_id": ObjectId(user_id)})
        return str(deleted_user)

    @staticmethod
    def get_user_tickets(user_id):
        collection = g.db["tickets"]
        tickets = collection.find({"user_id": ObjectId(user_id)})
        return str(list(tickets))