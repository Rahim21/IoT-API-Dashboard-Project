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

    def insert_user(self, user_data):
        self.users_collection.insert_one(user_data)

    def insert_single_ticket(self, single_ticket_data):
        self.single_tickets_collection.insert_one(single_ticket_data)

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
        "id": "123",
        "lastname": "Doe",
        "firstname": "John",
        "username": "johndoe",
        "password": "hashed_password"
    }
    mongo_db.insert_user(user_data)

    single_ticket_data = {
        "id": "456",
        "qr_code": "abc123",
        "validite": True,
        "date_achat": datetime.now(),
        "type": "standard"
    }
    mongo_db.insert_single_ticket(single_ticket_data)

    daily_ticket_data = {
        "id": "789",
        "qr_code": "xyz789",
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