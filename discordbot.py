import os

import discord

client = discord.Client()
token = open('token.txt', 'r').readline()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!recap'):
        splitted_message = message.content.split(" ")
        if len(splitted_message) != 3:
            await message.channel.send('Wrong syntax, send the link as "!recap <your article> <a float between 0 and 1 to choose recap lenght, eg 0.3>')
        else:


client.run(token)