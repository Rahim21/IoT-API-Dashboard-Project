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
        data = decode(Image.open('./'+img+'.png')) # donner le choix au format 
        print("data {}, type {}".format(data[0].data,type(data[0].data)))
