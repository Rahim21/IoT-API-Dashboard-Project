# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# routes/ticket_route.py
from flask import Blueprint
from controllers.statistics_controller import StatisticsController

statistics_blueprint = Blueprint('statistics', __name__, url_prefix='/statistics')

@statistics_blueprint.route('/total_number_tickets', methods=['GET']) 
def total_number_tickets():
    return StatisticsController.total_number_tickets()

@statistics_blueprint.route('/repartition_types_tickets', methods=['GET']) 
def repartition_types_tickets():
    return StatisticsController.repartition_types_tickets()

@statistics_blueprint.route('/number_expired_tickets', methods=['GET']) 
def number_expired_tickets():
    return StatisticsController.number_expired_tickets()

@statistics_blueprint.route('/turnover', methods=['GET']) 
def turnover():
    return StatisticsController.turnover()

@statistics_blueprint.route('/most_active_users', methods=['GET']) 
def most_active_users():
    return StatisticsController.most_active_users()

@statistics_blueprint.route('/peak_usage_times', methods=['GET']) 
def peak_usage_times():
    return StatisticsController.peak_usage_times()

@statistics_blueprint.route('/repartition_types_personnes', methods=['GET']) 
def repartition_types_personnes():
    return StatisticsController.repartition_types_personnes()