import discord
import os
import validation

TOKEN = os.environ.get('QUEEN_TOKEN')
client = discord.Client()

reporting = client.get_channel('534191629762822144')
get_channel_id = '540608326564839439'
arisa = client.get_server('539867992847024149')

@client.event
async def on_message(message):
    me = await client.get_user_info('92708688606793728')

    if message.channel.id != get_channel_id:
        print("[" + message.channel.name + "] " + message.author.name + ": " + message.content)

    if message.author != client.user and message.author == me and message.channel == get_channel_id: # and validation.validateMention(message.content):
        await client.send_message(reporting, message.content)
    else:
        return

@client.event
async def on_member_join(member):
    # client.get_role('')
    # client.add_role(member, )
    return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Server name: ' + arisa.name)
    print('------------')

client.run(TOKEN)
