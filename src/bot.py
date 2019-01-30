import discord
import os
import validation

TOKEN = os.environ.get('QUEEN_TOKEN')
client = discord.Client()

@client.event
async def on_message(message):
    if message.author is not client.user and validation.validateMention(message.content):
        for usr in message.mentions:
            print (usr.mention)
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    else:
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

client.run(TOKEN)
