import discord
import asyncio
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

    lines2 = ["test line 1", "test line 2", "test line 3"]
    chapter2 = Chapter("Test Chapter 2", lines2)

    lines3 = ["test line 1", "test line 2", "test line 3"]
    chapter3 = Chapter("Test Chapter 3", lines3)

    lines4 = ["test line 1", "test line 2", "test line 3"]
    chapter4 = Chapter("Test Chapter 4", lines4)

    lines5 = ["test line 1", "test line 2", "test line 3"]
    chapter5 = Chapter("Test Chapter 5", lines5)


    item_book = Book([chapter1, chapter2, chapter3, chapter4, chapter5], "Test Book", "Test book Desc")

    book_message = await message.channel.send(embed = item_book.get_current_page())

    OPTIONS = [
        '\U000023ea', # Reverse
        '\U00002b05', # Left Arrow
        '\U000027a1', # Right Arrow
        '\U000023e9', # Fast Forward
    ]

    OPTIONS_EMOJI = [
        '⏪', # Reverse
        '⬅', # Left Arrow
        '➡', # Right Arrrow
        '⏩', # Fast Forward
    ]

    OPTIONS_ENCODED = [
        '\U000023ea'.encode('utf-8'), # Reverse
        '\U00002b05'.encode('utf-8'), # Left Arrow
        '\U000027a1'.encode('utf-8'), # Right Arrow
        '\U000023e9'.encode('utf-8'), # Fast Forward
    ]

    for option in OPTIONS :
        await book_message.add_reaction(option)


    def check_response(reaction, user) :
        # Odd that this reaction check doesn't work well - seems to be some weird matching issue with what wait_for gets and their versions in Python
        # return reaction in OPTIONS_EMOJI and user == message.author
        return str(reaction).encode('utf-8') in OPTIONS_ENCODED and user == message.author

    try :
        while True :
            print("LOOP")
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check_response)
            print("OUT OF CHECK")

            reaction = str(reaction).encode('utf-8')

            if reaction == '\U00002b05'.encode('utf-8') :
                item_book.one_page_backward()

            elif reaction == '\U000027a1'.encode('utf-8') :
                item_book.one_page_forward()

            elif reaction == '\U000023ea'.encode('utf-8') :
                item_book.page_backward(5)

            elif reaction == '\U000023e9'.encode('utf-8') :
                item_book.page_forward(5)

            new_embed = item_book.get_current_page()
            await book_message.edit(embed = new_embed)



    except asyncio.TimeoutError:
        await message.channel.send('Timed out...')
        await book_message.clear_reactions()
    

TOKEN = open("bot-token").read().rstrip()
client.run(TOKEN)
