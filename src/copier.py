import discord
import os

TOKEN = os.environ.get('BOT_TOKEN')
client = discord.Client()

@client.event
async def on_message(message):
    me = client.get_user(92708688606793728) # user ID

    post_channel = client.get_channel(539867992847024151) # change this channel ID
    get_channel = client.get_channel(540608326564839439) # original getter channel channel

    if message.author != client.user and message.author == me and message.channel == get_channel: # Change this channel id
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
