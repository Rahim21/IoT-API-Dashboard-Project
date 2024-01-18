#!/usr/bin/python3
import logging
import asyncio
import aiocoap

import aiocoap.numbers.codes as codes

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await aiocoap.Context.create_client_context()
    request = aiocoap.Message(code=codes.GET, uri='coap://localhost')
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))
if __name__ == "__main__":
    asyncio.run(main()) 