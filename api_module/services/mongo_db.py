import pymongo
from datetime import datetime, timedelta

class MongoDB:
    def __init__(self, db_name="ma_base_de_donnees"):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client[db_name]

        # Collections
        self.users_collection = self.database["Users"]
        self.single_tickets_collection = self.database["SingleTickets"]
        self.daily_tickets_collection = self.database["DailyTickets"]
        self.badges_collection = self.database["Badges"]
        self.user_tickets_collection = self.database["UserTickets"]


    # Fonction pour attribuer un ID unique lors d'un ajout d'une nouvelle donnée dans une collection
    def get_next_id(self, collection):
        max_id = collection.find_one(sort=[("id", pymongo.DESCENDING)]) 
        if max_id:
            return int(max_id["id"]) + 1
        else:
            return 1


##################           FONCTIONS POUR LES USERS           ####################

    def insert_user(self, user_data):
        existing_mail = self.users_collection.find_one({"email": user_data["email"]})

        if existing_mail:
            return {"Erreur, le mail est déjà utilisé."}, False
        else:
            user_data["id"] = str(self.get_next_id(self.users_collection))
            self.users_collection.insert_one(user_data)
            return {"Utilisateur ajouté avec succès."}, True
        
    def update_user_email(self, user_id, new_email):
        existing_mail = self.users_collection.find_one({"email": new_email["email"]})
        if existing_mail:
            return "Erreur, le mail est déjà utilisé.", False
        
        result = self.users_collection.update_one({"id": user_id}, {"$set": {"email": new_email}})

        if result.modified_count > 0:
            return "Email mis à jour avec succès.", True
        else:
            return "Erreur avec le changement d'addresse mail", False

    def update_user_password(self, user_id, new_password):
        result = self.users_collection.update_one({"id": user_id}, {"$set": {"password": new_password}})

        if result.modified_count > 0:
            return "Mot de passe mis à jour avec succès.", True
        else:
            return "Erreur avec le changement de mot de passe", False
        
    def delete_user(self, identifier):
        result = self.users_collection.delete_one({"$or": [{"id": identifier}, {"email": identifier}]})

        if result.deleted_count > 0:
            return "Utilisateur supprimé avec succès."
        else:
            return "Erreur avec la suppression"
        
    def get_all_users(self):
        users = self.users_collection.find({}, {"password": 0})
        return list(users)
    
#############################################################################################

    def insert_single_ticket(self, single_ticket_data):
        single_ticket_data["id"] = str(self.get_next_id(self.single_tickets_collection))
        result = self.single_tickets_collection.insert_one(single_ticket_data)
        if result.deleted_count > 0:
            return "Ticket à usage unique créé avec succès.", True
        else:
            return "Erreur avec la création du ticket à usage unique.", False
        
    def clear_single_tickets(self):
        # Supprime tous les "single tickets" avec "validité" égale à False
        result = self.single_tickets_collection.delete_many({"validite": False})
        
        if result.deleted_count == 1:
            return ("Un ticket invalide a été supprimé."), True
        else: 
            if result.deleted_count > 1:
                return (f"{result.deleted_count} billets invalides supprimés avec succès."), True
            else:
                return ("Aucun ticket n'a été supprimé"), False

    def insert_daily_ticket(self, daily_ticket_data):
        self.daily_tickets_collection.insert_one(daily_ticket_data)

    def insert_badge(self, badge_data):
        self.badges_collection.insert_one(badge_data)

    def insert_user_ticket(self, user_ticket_data):
        self.user_tickets_collection.insert_one(user_ticket_data)

# Exemple d'utilisation :
if __name__ == "__main__":
    mongo_db = MongoDB(db_name="bdd")

    user_data = {
        "lastname": "Doe",
        "firstname": "John",
        "email": "johndoe@gmail.com",
        "password": "hashed_password"
    }
    mongo_db.insert_user(user_data)

    single_ticket_data = {
        "id": "456",
        "id_user": "15",
        "validite": True,
        "date_achat": datetime.now(),
    }
    mongo_db.insert_single_ticket(single_ticket_data)

    daily_ticket_data = {
        "id": "789",
        "validite": True
    }
    mongo_db.insert_daily_ticket(daily_ticket_data)

    badge_data = {
        "id": "101",
        "prenom": "Alice",
        "validite": True,
        "actif": True
    }
    mongo_db.insert_badge(badge_data)

    user_ticket_data = {
        "id": "234",
        "etat": "vendu",
        "date_achat": datetime.now(),
        "type": "standard",
        "date_fin_validite": datetime.now() + timedelta(days=30),
        "id_user": "123"
    }
    mongo_db.insert_user_ticket(user_ticket_data)