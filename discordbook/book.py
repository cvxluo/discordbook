
import discord
import asyncio

# do i need this
from math import ceil


class Book (object) :

    def __init__ (self, chapters = [], title = "\a", description = '\a', color = 1, per_page = 10) :
        self.chapters = chapters
        self.title = title
        self.description = description
        self.color = color
        self.per_page = per_page
        self.page_number = 0
        self.total_page_count = -1

        self.pages = self.generate_pages()


    def generate_pages(self) :
        pages = []
        
        line_count = 0
        chapter_count = []
        for chapter in self.chapters :
            chapter_count.append(len(chapter))
            line_count += len(chapter)

        on_chapter = 0
        on_line = 0

        self.total_page_count = ceil(line_count / self.per_page)
        for page_num in range(self.total_page_count) :
            embed = discord.Embed(title=self.title, description=self.description, color=self.color)

            lines_to_fill = self.per_page

            # Keep iterating through chapters until all the lines needed are filled
            while lines_to_fill > 0 and on_chapter <= len(self.chapters) - 1:

                # If this chapter has enough lines to fill the rest of the page, take as many lines as needed
                if on_line + lines_to_fill < chapter_count[on_chapter] :
                    field_content = ''
                    
                    for line in self.chapters[on_chapter].get_lines(on_line, on_line + lines_to_fill) :
                        field_content += line + '\n'

                    embed.add_field(name = self.chapters[on_chapter].get_title(), value = field_content, inline = False)
                    on_line += lines_to_fill + 1
                    lines_to_fill = 0


                else : # if on_line + lines_to_fill >= chapter_count[on_chapter], in which case we fill out the rest of the chapter and go to the next chapter

                    if chapter_count[on_chapter] : # If this chapter has no lines, skip adding the field
                        field_content = ''

                        # Get rest of chapter
                        for line in self.chapters[on_chapter].get_lines(on_line, chapter_count[on_chapter]) :
                            field_content += line + '\n'

                        embed.add_field(name = self.chapters[on_chapter].get_title(), value = field_content, inline = False) 
                        lines_to_fill -= (chapter_count[on_chapter] - on_line)
                        
                    on_line = 0
                    on_chapter += 1


            embed.set_footer(text = "Page: " + str(page_num + 1) + "/" + str(self.total_page_count))
            pages.append(embed)


        return pages
        


    def set_per_page(self, per_page) :
        self.per_page = per_page


    def one_page_forward(self) :
        self.page_number += 1 if self.page_number + 1 < self.total_page_count else 0

    def one_page_backward(self) :
        self.page_number -= 1 if self.page_number > 0 else 0


    def page_forward(self, num_pages_forward) :
        self.page_number += num_pages_forward if (self.page_number + num_pages_forward) < self.total_page_count else (self.total_page_count - self.page_number - 1)

    def page_backward(self, num_pages_backward) :
        self.page_number -= num_pages_backward if self.page_number - num_pages_backward >= 0 else self.page_number



    def get_current_page(self) :

        """
        Limits
        Embed titles are limited to 256 characters
        Embed descriptions are limited to 2048 characters
        There can be up to 25 fields
        A field's name is limited to 256 characters and its value to 1024 characters
        The footer text is limited to 2048 characters
        The author name is limited to 256 characters
        In addition, the sum of all characters in an embed structure must not exceed 6000 characters
        """

        return self.pages[self.page_number]


    async def open_book(self, discord_client, channel, author = None) :

        book_message = await channel.send(embed = self.get_current_page())

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
            return str(reaction).encode('utf-8') in OPTIONS_ENCODED and (not author or user == author)

        try :
            while True :
                reaction, user = await discord_client.wait_for('reaction_add', timeout=10.0, check=check_response)

                reaction = str(reaction).encode('utf-8')

                if reaction == '\U00002b05'.encode('utf-8') :
                    self.one_page_backward()

                elif reaction == '\U000027a1'.encode('utf-8') :
                    self.one_page_forward()

                elif reaction == '\U000023ea'.encode('utf-8') :
                    self.page_backward(5)

                elif reaction == '\U000023e9'.encode('utf-8') :
                    self.page_forward(5)

                new_embed = self.get_current_page()
                await book_message.edit(embed = new_embed)



        except asyncio.TimeoutError:
            await channel.send('Timed out...')
            await book_message.clear_reactions()
