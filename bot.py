import discord
import os
import re

TOKEN = os.environ.get('QUEEN_TOKEN')
client = discord.Client()

@client.event
async def on_message(message):
    if message.author is not client.user and message.content.startswith('!'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

client.run(TOKEN)
