# -----------------------------------------------------------------------------
# Auteurs: BERTRAND Hugo & DRIOUCHE Sami & HAYAT Rahim & MTARFI Souhail
# -----------------------------------------------------------------------------
# services/ticket_service.py
from api_module.models.ticket_model import Ticket
from flask import jsonify
from qrcode import make
from pyzbar.pyzbar import decode
from PIL import Image

class Qrcode:
    def __init__(self):
        pass

    def encode_qrcode(self,data):
        # Récupérer différentes données pour le nom de l'image png
        img = make(data)
        type(img)
        return img

    def decode_qrcode(self,img):
        data = decode(Image.open('./'+img+'.png'))
        print("data {}, type {}".format(data[0].data,type(data[0].data)))

        # Requête vers la BDD


class TicketService:

    @staticmethod
    def get_tickets():
        pass

    @staticmethod
    def get_ticket(ticket_id):
        pass

    @staticmethod
    def add_ticket(ticket_data):
        pass

    @staticmethod
    def edit_ticket(ticket_id, updated_data):
        pass

    @staticmethod
    def delete_ticket(ticket_id):
        pass



# classe = Qrcode()    
# img = classe.encode_qrcode(data={"nom" : "olivier", "prenom" : "flauzac"})
# classe.decode_qrcode(img)