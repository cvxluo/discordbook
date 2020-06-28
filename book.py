
import discord

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

        total_page_count = ceil(line_count / self.per_page)
        for page_num in range(total_page_count) :
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
                    field_content = ''

                    # Get rest of chapter
                    for line in self.chapters[on_chapter].get_lines(on_line, chapter_count[on_chapter]) :
                        field_content += line + '\n'

                    embed.add_field(name = self.chapters[on_chapter].get_title(), value = field_content, inline = False) 
                    lines_to_fill -= (chapter_count[on_chapter] - on_line)
                    on_line = 0
                    on_chapter += 1


            embed.set_footer(text = "Page: " + str(page_num + 1) + "/" + str(total_page_count))
            pages.append(embed)


        return pages
        


    def set_per_page(self, per_page) :
        self.per_page = per_page


    def one_page_forward(self) :
        self.page_number += 1 if (self.page_number + 1) * self.per_page < sum([len(x) for x in self.chapters.values()]) else 0

    def one_page_backward(self) :
        self.page_number -= 1 if self.page_number > 0 else 0


    def page_forward(self, num_pages_forward) :
        self.page_number += num_pages_forward if (self.page_number + num_pages_forward) * self.per_page < sum([len(x) for x in self.chapters.values()]) else 0

    def page_backward(self, num_pages_backward) :
        self.page_number -= num_pages_backward if self.page_number - num_pages_backward >= 0 else 0



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

