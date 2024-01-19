import pymongo
from datetime import datetime, timedelta

class MongoDB:
    def __init__(self, db_name="ma_base_de_donnees"):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client[db_name]

        # Collections
        self.users_collection = self.database["Users"]
        self.twoH_tickets_collection = self.database["twoHTickets"]
        self.daily_tickets_collection = self.database["DailyTickets"]
        self.badges_collection = self.database["Badges"]


    # Fonction pour attribuer un ID unique lors d'un ajout d'une nouvelle donnée dans une collection
    # Pour l'instant ça ne prend pas en compte les suppressions dans la BDD
    # Ce qui veut dire que les nouveaux ID prendront une valeur toujours plus grande et ne prendront pas des valeurs d'ID supprimés    
    def get_next_id(self, collection):
        max_id = collection.find_one(sort=[("id", pymongo.DESCENDING)]) 
        if max_id:
            return int(max_id["id"]) + 1
        else:
            return 1


#############################################################################################
##################           FONCTIONS POUR LES USERS           #############################


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
##################           FONCTIONS POUR LES TICKETS 2 HEURES           ##################
    

    def insert_twoH_ticket(self, twoH_ticket_data):
        twoH_ticket_data["id"] = str(self.get_next_id(self.twoH_tickets_collection))
        result = self.twoH_tickets_collection.insert_one(twoH_ticket_data)
        if result.deleted_count > 0:
            return "Ticket 2 heures créé avec succès.", True
        else:
            return "Erreur avec la création du ticket 2 heures.", False
        
    def get_twoH_ticket(self, twoH_ticket_id):
        return self.twoH_tickets_collection.find_one({"id": twoH_ticket_id})
        
    def clear_twoH_tickets(self):
        # Supprime tous les "twoH tickets" avec "validité" égale à False
        result = self.twoH_tickets_collection.delete_many({"validite": False})
        
        if result.deleted_count == 1:
            return ("Un ticket invalide a été supprimé."), True
        else: 
            if result.deleted_count > 1:
                return (f"{result.deleted_count} billets invalides supprimés avec succès."), True
            else:
                return ("Aucun ticket n'a été supprimé"), False
            
            
#############################################################################################
##################           FONCTIONS POUR LES TICKETS JOURNALIERS          ################


    def insert_daily_ticket(self, daily_ticket_data):
        daily_ticket_data["id"] = str(self.get_next_id(self.daily_tickets_collection))
        result = self.daily_tickets_collection.insert_one(daily_ticket_data)
        if result.deleted_count > 0:
            return "Ticket journalier créé avec succès.", True
        else:
            return "Erreur avec la création du ticket journalier.", False
        
    def get_daily_ticket(self, daily_ticket_id):
        return self.daily_tickets_collection.find_one({"id": daily_ticket_id})

    def clear_daily_tickets(self):
        # Supprime tous les "twoH tickets" avec "validité" égale à False
        result = self.daily_tickets_collection.delete_many({"validite": False})
        
        if result.deleted_count == 1:
            return ("Un ticket journalier invalide a été supprimé."), True
        else: 
            if result.deleted_count > 1:
                return (f"{result.deleted_count} tickets invalides journaliers supprimés avec succès."), True
            else:
                return ("Aucun ticket journalier n'a été supprimé"), False
            
            
#############################################################################################
##################           FONCTIONS POUR LES ABONNEMENTS 30 JOURS          ###############

            
    def insert_badge(self, badges_data):
        existing_badge = self.badges_collection.find_one({"user_id": badges_data["user_id"]})
        if existing_badge:
            return {"Erreur, un badge pour cet utilisateur est déjà créé."}, False
        badges_data["id"] = str(self.get_next_id(self.badges_collection))
        result = self.badges_collection.insert_one(badges_data)
        if result.deleted_count > 0:
            return "Ticket journalier créé avec succès.", True
        else:
            return "Erreur avec la création du ticket journalier.", False
        
    def get_badge(self, badge_id):
        return self.badges_collection_collection.find_one({"id": badge_id})

    def delete_badge(self, user_id):
        result = self.badges_collection.delete_one({"user_id": user_id})
        if result.deleted_count > 0:
            return "Badge supprimé avec succès.", True
        else:
            return "Erreur avec la suppression du badge.", False
        

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

    twoH_ticket_data = {
        "id": "456",
        "validite": True,
        "date_achat": datetime.now(),
        "date_limite": "",
    }
    mongo_db.insert_twoH_ticket(twoH_ticket_data)

    daily_ticket_data = {
        "id": "456",
        "validite": True,
        "date_achat": datetime.now(),
        "date_limite": "",
    }
    mongo_db.insert_daily_ticket(daily_ticket_data)

    badge_data = {
        "id": "101",
        "user_id": "15",
        "date_fin_validite": datetime.now() + timedelta(days=30),
        "validite": True,
        "nombre_scan": "0"
    }
    mongo_db.insert_badge(badge_data)





####################   FONCTIONS QUE JE SAIS PAS METTRE OU  #######################
    

