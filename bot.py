import os

import discord
import random

TOKEN = 'OTQ5NDE1NjQ3Mzc1NDA1MTE3.YiKCOQ.gt2pRHRJdlwlw5HgKqK1EY-F8ts'

pics = [f for f in os.listdir('./pics/')]

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if ('!coach' in message.content):
        if pics:
            pic = random.choice(pics)
            await message.channel.send(file=discord.File(f'./pics/{pic}'))
        else:
            await message.channel.send('I can\'t find any pics :(')

client.run(TOKEN)