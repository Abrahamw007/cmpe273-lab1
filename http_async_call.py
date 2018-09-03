import requests as r
import json as j
import asyncio
import random

async def getresult(url, id):
     MyRequest=r.get(url)
     processtime=random.randint(1,7)
     await asyncio.sleep(processtime)
     print("Couroutine {} , has successfully completd after {} seconds ".format( id,processtime ), MyRequest.headers['Date'])
    # return MyRequest.headers['Date']


async def main():

    tasks =[]
    for i in range(5):
        tasks.append(asyncio.ensure_future(getresult('https://webhook.site/#/5443c001-7a4d-46e3-81a2-af671125128a', i)))

    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()

loop.run_until_complete(main())
# loop.run_until_complete(getresult('https://webhook.site/#/5443c001-7a4d-46e3-81a2-af671125128a'))
# loop.run_until_complete(getresult('https://webhook.site/#/5443c001-7a4d-46e3-81a2-af671125128a'))

loop.close()





