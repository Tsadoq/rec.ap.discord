import discord
import recapper

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
        [cmd, url, perc] = split_message = message.content.split(" ")
        if len(split_message) == 2 or len(split_message) == 3:
            r = recapper.Recapper(url=url)
            r.process()
            perc = 0.22 if len(split_message) == 2 else perc = perc
            recap = r.summarize(perc=perc)
            await message.channel.send(recap)
        else:
            await message.channel.send(
                'Wrong syntax, send the link as "!recap <your article> <optional but recommended: a float between 0 '
                'and 1 to choose recap length, eg 0.3>')


client.run(token)
