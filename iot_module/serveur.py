#!/usr/bin/python3
import datetime
import asyncio
import logging
import aiocoap

import aiocoap.resource as resource

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
    root.add_resource([], Hello())
    await aiocoap.Context.create_server_context(root)
    await asyncio.get_running_loop().create_future()
    
if __name__ == "__main__":
    asyncio.run(main())