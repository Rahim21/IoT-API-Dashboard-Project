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
    def migrate():
        # Include your migration method here
        try:
            UserService.migrate_default_admin()
        except:
            return False
        return True

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
        collection.insert_one(new_user.__dict__)
        user = new_user.__dict__
        user["_id"] = str(user["_id"])
        return user

    @staticmethod
    def login_user(email, password):
        # Récupération de l'utilisateur à l'aide du mail et mot de passe
        collection = g.db["users"]
        # user = collection.find_one({"email": email, "password": password})
        user_data = collection.find_one({"email": email})
        if user_data and check_password_hash(user_data['password'], password):
            user_data["_id"] = str(user_data["_id"])
            del user_data['email']
            del user_data['password']
            return user_data
        else:
            return None

    @staticmethod
    def get_users():
        # Récupération de tous les utilisateurs de la base de données MongoDB
        collection = g.db["users"]
        users_data = collection.find()
        users = list(users_data)
        for user in users:
            user["_id"] = str(user["_id"])
            del user['password']
        return users

    @staticmethod
    def get_user_by_id(user_id):
        # Récupération de l'utilisateur à l'aide de son identifiant
        collection = g.db["users"]
        user = collection.find_one({"_id": ObjectId(user_id)})
        user["_id"] = str(user["_id"])
        del user['password']
        return user

    @staticmethod
    def update_user(user_id, updated_data):
        # Mise à jour de l'utilisateur à l'aide de son identifiant
        collection = g.db["users"]
        updated_user = collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": updated_data},
            return_document=True
        )
        updated_user["_id"] = str(updated_user["_id"])
        return updated_user

    @staticmethod
    def deactivate_user(user_id):
        # Rendre inactif l'utilisateur à l'aide de son identifiant
        collection = g.db["users"]
        user = collection.find_one({"_id": ObjectId(user_id)})
        new_status = not user.get("is_active", False)
        deactivated_user = collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": {"is_active": new_status}},
            return_document=True
        )
        deactivated_user["_id"] = str(deactivated_user["_id"])
        return deactivated_user
    
    @staticmethod
    def delete_user(user_id):
        # Suppression de l'utilisateur à l'aide de son identifiant
        collection = g.db["users"]
        deleted_user = collection.find_one_and_delete({"_id": ObjectId(user_id)})
        deleted_user["_id"] = str(deleted_user["_id"])
        return deleted_user

    @staticmethod
    def get_user_tickets(user_id):
        collection = g.db["tickets"]
        tickets_data = collection.find({"user_id": ObjectId(user_id)})

        tickets = list(tickets_data)
        for ticket in tickets:
            ticket["_id"] = str(ticket["_id"])
            ticket["user_id"] = str(ticket["user_id"]) if ticket["user_id"] else None
        return tickets
    
    @staticmethod
    def migrate_default_admin():
        try:
            collection = g.db["users"]
            user = collection.find_one({"email": "admin@ticketgo.com"})
            if not user:
                new_user = User(
                    username="admin",
                    email="admin@ticketgo.com",
                    password="admin",
                    role="admin",
                    is_active=True
                )
                new_user.password = generate_password_hash(new_user.password, method='pbkdf2:sha256')
                collection.insert_one(new_user.__dict__)
        except:
            return False
        return True
