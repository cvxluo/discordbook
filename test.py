import discord
import asyncio
from discordbook.book import Book
from discordbook.alpha_book import AlphabeticalBook
from discordbook.chapter import Chapter

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print("MESSAGE SEEN")

    """
    lines1 = ["test line 1", "test line 2", "test line 3"]
    chapter1 = Chapter("Test Chapter 1", lines1)

    lines2 = ["test line 1", "test line 2", "test line 3"]
    chapter2 = Chapter("Test Chapter 2", lines2)

    lines3 = ["test line 1", "test line 2", "test line 3"]
    chapter3 = Chapter("Test Chapter 3", lines3)

    lines4 = ["test line 1", "test line 2", "test line 3"]
    chapter4 = Chapter("Test Chapter 4", lines4)

    lines5 = ["test line 1", "test line 2", "test line 3"]
    chapter5 = Chapter("Test Chapter 5", lines5)


    item_book = Book([chapter1, chapter2, chapter3, chapter4, chapter5], "Test Book", "Test book Desc")

    await item_book.open_book(client, message.channel, message.author)
    """

    lines1 = ["Test", "test", "Abc", "bc", "D", "asdfkj"]
    a_book = AlphabeticalBook(lines1, "Test Book", "test desc", ignore_caps = False)
    await a_book.open_book(client, message.channel)





    

TOKEN = open("bot-token").read().rstrip()
client.run(TOKEN)
