import discord
import os
import validation
import io
from discord.utils import get

TOKEN = os.environ.get('QUEEN_TOKEN')
client = discord.Client()
report_id = 539867992847024151

get_channel_id = 540608326564839439

@client.event
async def on_message(message):
    me = client.get_user(92708688606793728)

    print_msg = ""
    if message.channel.id != get_channel_id:
        try:
            print_msg = "[{0}::{1} - {2}]\n  {3}: {4}".format(message.channel.guild.name, message.channel.name, message.channel.id, message.author.name, message.content)
        except:
            print_msg = "[DM::{0} - {1}]\n  {2}: {3}".format(message.channel.recipient.name, message.channel.recipient.id, message.author.name, message.content)
        print(print_msg)

    global report_id
    if message.content.startswith('!setchannel'):
        report_id = int(message.content.replace('!setchannel', '').strip())
    reporting = client.get_channel(report_id) if client.get_channel(report_id) != None else client.get_user(report_id)

    if 'makitoshi best girl' in message.content.lower():
        await message.channel.send(get(client.get_channel(get_channel_id).guild.emojis, name="HaruUvU"))

    command = message.content.split()
    if command[0] == '!m':
        if command[1] == 'avatar':
            if len(command) == 2:
                # return sender's avatar
                await message.channel.send(message.author.avatar)
            elif len(message.mentions) > 0:
                # print avatars of everyone mentioned
                for member of message.mentions:
                    await message.channel.send(member.avatar)
            else:
                # find user based on the rest of the command
                lookup_name = ' '.join(command[2:])
                for member of message.guild.members:
                    if member.display_name.startswith(lookup_name):
                        await message.channel.send(member.avatar)
                        return
                await message.channel.send('No matches found')


    files = []
    for attach in message.attachments:
        f = io.BytesIO()
        await attach.save(f)
        files.append(discord.File(f, attach.filename))

    if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
        await client.get_channel(get_channel_id).send(content=print_msg, files=files)

    if message.author != client.user and message.author == me and message.channel.id == get_channel_id: # and validation.validateMention(message.content):
        if message.content.startswith('!'):
            await client.get_channel(get_channel_id).send("OK")
        else:
            await reporting.send(message.content, files=files)
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
    print('------------')

client.run(TOKEN)
