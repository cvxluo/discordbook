import discord
from book import Book
from chapter import Chapter

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print("MESSAGE SEEN")

    lines1 = ["test line 1", "test line 2", "test line 3"]
    chapter1 = Chapter("Test Chapter 1", lines1)
    print(chapter1)

    lines2 = ["test line 1", "test line 2", "test line 3"]
    chapter2 = Chapter("Test Chapter 2", lines2)
    print(chapter2)

    lines3 = ["test line 1", "test line 2", "test line 3"]
    chapter3 = Chapter("Test Chapter 3", lines3)
    print(chapter3)

    lines4 = ["test line 1", "test line 2", "test line 3"]
    chapter4 = Chapter("Test Chapter 4", lines4)
    print(chapter4)

    lines5 = ["test line 1", "test line 2", "test line 3"]
    chapter5 = Chapter("Test Chapter 5", lines5)
    print(chapter5)


    book = Book([chapter1, chapter2, chapter3, chapter4, chapter5], "Test Book", "Test book Desc")
    print(book.get_current_page().to_dict())
    print(book.pages[1].to_dict())
    await message.channel.send(embed=book.get_current_page())
    await message.channel.send(embed=book.pages[1])



    '''
    embed = discord.Embed(title="test", description="test", color=1)
    for i in range(30) :
        embed.add_field(name="title", value=i, inline=False)
    await message.channel.send(embed=embed)   
    '''

    

TOKEN = open("bot-token").read().rstrip()
client.run(TOKEN)
