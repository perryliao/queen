import discord
import os
import validation

TOKEN = os.environ.get('QUEEN_TOKEN')
client = discord.Client()

@client.event
async def on_message(message):
    me = await client.get_user_info('92708688606793728')
    print(message.author.name + ": " + message.content)
    print(message.channel)
    if message.author != client.user and message.author == me and message.channel.id == '540608326564839439': # and validation.validateMention(message.content):
        if message.content == "!m close":
            client.close()

        for usr in message.mentions:
            print (usr.mention)
        # msg = 'Hello {0.author.mention}'.format(message)

        await client.send_message(client.get_channel('534191629762822144'), message.content)
    else:
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

client.run(TOKEN)
