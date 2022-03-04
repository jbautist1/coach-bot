import os

import discord
import random

TOKEN = os.getenv('DISCORD_TOKEN')

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