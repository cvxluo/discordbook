
import discord


class Chapter (object) :

    def __init__ (self, title = "Title", lines = []) :
        self.title = title
        self.lines = lines

    def get_title(self) :
        return self.title

    def get_all_lines(self) :
        return self.lines

    def get_lines(self, start, end) :
        return self.lines[start:end]
    
    def get_line(self, line_num) :
        return self.lines[line_num]

    def __len__ (self) :
        return len(self.lines)

    def __str__ (self) :
        line_block = ''
        for line in self.lines :
            line_block += line + '\n'

        return self.title + '\n' + line_block
