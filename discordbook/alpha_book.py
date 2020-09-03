
import discord
import asyncio

from .book import Book
from .chapter import Chapter


class AlphabeticalBook (Book) :

    def __init__ (self, content = [], title = "\a", description = '\a', color = 1, image = None, per_page = 10, ignore_caps = True) :
        self.content = content
        self.chapters = []
        self.title = title
        self.description = description
        self.color = color
        self.image = image
        self.per_page = per_page
        self.page_number = 0
        self.total_page_count = -1

        # If ignore_caps is True, content will be ordered as if all lowercase
        # Otherwise, capital and lowercase will be separated
        self.ignore_caps = ignore_caps
        self.generate_chapters()

        self.pages = self.generate_pages()



    def generate_chapters(self) :

        if self.ignore_caps :
            sorted_content = sorted(self.content, key = str.casefold)
            line_num = 0
            for i in range(65, 91) :
                chapter_lines = []
                letter_title = chr(i)

                while line_num < len(sorted_content) and sorted_content[line_num][0].upper() == letter_title :
                    chapter_lines.append(sorted_content[line_num])
                    line_num += 1

                chapter = Chapter(title = letter_title, lines = chapter_lines)
                self.chapters.append(chapter)

        else :
            sorted_content = sorted(self.content, key = lambda line: line[0].lower())
            line_num = 0
            for i in range(65, 91) :
                upper_chapter_lines = []
                lower_chapter_lines = []
                upper_letter_title = chr(i)
                lower_letter_title = chr(i + 32) 

                while line_num < len(sorted_content) and sorted_content[line_num][0] == upper_letter_title :
                    upper_chapter_lines.append(sorted_content[line_num])
                    line_num += 1

                while line_num < len(sorted_content) and sorted_content[line_num][0] == lower_letter_title :
                    lower_chapter_lines.append(sorted_content[line_num])
                    line_num += 1

                upper_chapter = Chapter(title = upper_letter_title, lines = upper_chapter_lines)
                lower_chapter = Chapter(title = lower_letter_title, lines = lower_chapter_lines)
                self.chapters.append(upper_chapter)
                self.chapters.append(lower_chapter)

