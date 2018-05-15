import discord
from discord.ext import commands
import random
import sys
import requests
import json
import time
import asyncio
import datetime
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client = discord.Client()


async def KB_feed():        
    await client.wait_until_ready()
    print ('client Ready')
    channel = discord.Object(id='445802170206519310')
    req = requests.Session()
    while not client.is_closed:
        response = req.get("https://redisq.zkillboard.com/listen.php")
        if response.status_code == 200:
            killMail = json.loads(response.content.decode('utf-8'))
            if killMail['package'] != None:
                for attacker in killMail['package']['killmail']['attackers']:
                    if 'corporation_id' in attacker:
                        if attacker['corporation_id'] == 98559478:
                            await client.send_message(channel,'New Kill: \nhttps://zkillboard.com/kill/' + str(killMail['package']['killID']))
                            print("New kill " + str(killMail['package']['killID']) + '\n')
        await asyncio.sleep(600)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(KB_feed())
client.run('NDQ1NzE4ODIzNzczOTI5NDgy.Ddujnw.Zht8NIJDUP-1mM6SeBtuDc8z0Cg')