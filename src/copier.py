import discord
import os

TOKEN = os.environ.get('BOT_TOKEN')
client = discord.Client()

@client.event
async def on_message(message):
    me = client.get_user(127915903483510784) # dad's ID

    post_channel = client.get_channel(586242433445265419) # change this channel ID
    get_channel = client.get_channel(510514823604207616) # original loli-time channel 

    if message.author != client.user and message.author == me and message.channel == client.get_channel(585940853902802956): # Change this channel id 
        async for message in get_channel.history(limit=None, oldest_first=True): 
            if message.content != "":
              await post_channel.send( "[{0}]: {1}".format( message.author.name, message.content ))
              try:
                await post_channel.send(message.attachments[0].url)
              except:
                continue
            else:
              try:
                await post_channel.send(message.attachments[0].url)
              except:
                continue
    else:
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

client.run(TOKEN)
