import datetime
import time
import asyncio
import logging
import aiocoap
import aiocoap.resource as resource
import random
from paho.mqtt import client as mqtt_client


### COAP server ###

class Multi(resource.Resource):
    def __init__(self):
        super().__init__()
        self.porte = 0
    async def render_get(self, request):
        msg = aiocoap.Message(payload=b"c'est du GET")
        return msg
    async def render_post(self, request):
        msg = aiocoap.Message(payload=b"c'est du POST")
        return msg
    async def render_put(self, request):
        self.porte = request.payload
        msg = aiocoap.Message(payload=self.porte)
        return msg
    async def render_delete(self, request):
        msg = aiocoap.Message(payload=b"c'est du DELETE")
        return msg

class Hello(resource.Resource):
    def __init__(self):
        super().__init__()
    async def render_get(self, request):
        msg = aiocoap.Message(payload=b"salut les amis")
        return msg

        
logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)



async def main():
    root = resource.Site()
    root.add_resource(['multi'], Multi())
    # root.add_resource([], Hello())
    await aiocoap.Context.create_server_context(root)
    await asyncio.get_running_loop().create_future()
    
if __name__ == '__main__':
    print("Lancement du serveur CoAP.")
    asyncio.run(main())
