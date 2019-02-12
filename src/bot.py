import discord
import os
import validation

TOKEN = os.environ.get('QUEEN_TOKEN')
client = discord.Client()

reporting = client.get_channel('534191629762822144')
test_channel = client.get_channel('540608326564839439')

arisa = client.get_server('539867992847024149')
@client.event
async def on_message(message):
    me = await client.get_user_info('92708688606793728')
    dyxie = await client.get_user_info('225528966734151680')
    rink = await client.get_user_info('92742418792714240')

    if message.channel.id != '540608326564839439':
        print("[" + message.channel.name + "] " + message.author.name + ": " + message.content)

    if message.author != client.user and message.author == me and message.channel == client.get_channel('540608326564839439'): # and validation.validateMention(message.content):
        if message.content == "!m close":
            client.logout()
            print("didn't close...")
        for usr in message.mentions:
            print (usr.mention)
        # msg = 'Hello {0.author.mention}'.format(message)

        for role in message.server.roles:
            await client.send_message(message.channel, role.id + role.name)
        # await client.send_message(rink, message.content)
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
