# Work with Python 3.6
import discord

TOKEN = 'NTA5ODQyODE2MDQ2OTg5MzE1.DsTs0Q.Wq92Pk-G3LU6Pbdv9_bwjLfLBkY'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
