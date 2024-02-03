# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# services/statistics_service.py
from flask import g
from datetime import datetime
class StatisticsService: 
    
    @staticmethod 
    def total_number_tickets():
        return g.db["tickets"].count_documents({})

    @staticmethod 
    def repartition_types_tickets():
        query = [
            {
                "$group": {
                "_id": "$ticket_type",
                "count": { "$sum": 1 }
                }
            }
        ]
        return list(g.db["tickets"].aggregate(query))
    
    @staticmethod 
    def repartition_types_personnes(): 
        query = [
            {
                "$group": {
                "_id": "$person_type",
                "count": { "$sum": 1 }
                }
            }
        ]
        return list(g.db["tickets"].aggregate(query))
    
    @staticmethod 
    def number_expired_tickets():
        now = datetime.utcnow().isoformat()
        #now = datetime.now()
        query = [
            {"$match": {"expires_at": {"$lt": now}}},
            {"$group": {"_id": "$person_type", "count": {"$sum": 1}}},
            {"$sort": {"_id": 1}}
        ]
        return list(g.db["tickets"].aggregate(query))

    @staticmethod
    def turnover():
        query = [
            {"$match": {"user_id": {"$exists": True}}},
            {"$group": {"_id": None, "total": {"$sum": "$price"}}}
        ]
        result = list(g.db["tickets"].aggregate(query))
        return result[0]["total"] if result else 0
    
    @staticmethod 
    def most_active_users(): 
        query = [ 
            {"$group": {"_id": "$user_id", "count": {"$sum": 1}}}, 
            {"$sort": {"count": -1}},
            {"$limit": 3}  # Limiter aux 3 utilisateurs les plus actifs
        ]
        result = list(g.db["tickets"].aggregate(query))
        for entry in result:
            entry["_id"] = str(entry["_id"])
        return result
        

    @staticmethod 
    def peak_usage_times(): 
        query = [
        {
        "$addFields": {
            "created_at": {
                "$toDate": "$created_at"
            }
        }
    },
    {
        "$group": {
            "_id": {
                "hour": {"$hour": "$created_at"},
                "day_of_week": {"$dayOfWeek": "$created_at"}
            },
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 3
    }
]
        return list(g.db["tickets"].aggregate(query))
    
