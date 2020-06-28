import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print("MESSAGE SEEN")

    

TOKEN = open("bot-token").read().rstrip()
client.run(TOKEN)
