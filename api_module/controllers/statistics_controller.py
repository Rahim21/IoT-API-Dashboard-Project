# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# controllers/ticket_controller.py
from flask import jsonify
from services.statistics_service import StatisticsService

class StatisticsController:

    @staticmethod
    def total_number_tickets():
        try:
            total_number_tickets = StatisticsService.total_number_tickets()
            return jsonify({"statusCode": 200, "total_number_tickets": total_number_tickets})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
        

    @staticmethod
    def repartition_types_tickets():
        try:
            repartition_types_tickets = StatisticsService.repartition_types_tickets()
            return jsonify({"statusCode": 200, "repartition_types_tickets": repartition_types_tickets})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})


    @staticmethod
    def number_expired_tickets():
        try:
            number_expired_tickets = StatisticsService.number_expired_tickets()
            return jsonify({"statusCode": 200, "number_expired_tickets": number_expired_tickets})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})


    @staticmethod
    def turnover():
        try:
            turnover = StatisticsService.turnover()
            return jsonify({"statusCode": 200, "turnover": turnover})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})


    @staticmethod
    def most_active_users():
        try:
            most_active_users = StatisticsService.most_active_users()
            return jsonify({"statusCode": 200, "most_active_users": most_active_users})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
        

    @staticmethod
    def peak_usage_times():
        try:
            peak_usage_times = StatisticsService.peak_usage_times()
            return jsonify({"statusCode": 200, "peak_usage_times": peak_usage_times})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})
        

    @staticmethod
    def repartition_types_personnes():
        try:
            repartition_types_personnes = StatisticsService.repartition_types_personnes()
            return jsonify({"statusCode": 200, "repartition_types_personnes": repartition_types_personnes})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": f"Erreur interne. {str(e)}"})