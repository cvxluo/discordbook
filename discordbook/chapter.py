
import discord


class Chapter (object) :

    def __init__ (self, title = "Title", lines = []) :
        self.title = title
        self.lines = lines

    # Helpers
    def get_title(self) :
        return self.title

    def get_all_lines(self) :
        return self.lines

    def get_lines(self, start, end) :
        return self.lines[start:end]
    
    def get_line(self, line_num) :
        return self.lines[line_num]

    def is_empty(self) :
        return len(lines) == 0


    # Modifiers
    def add_line(self, line) :
        self.lines.append(line)

    def add_line_at(self, line, pos) :
        self.lines.insert(pos, line)
        
        

    # Magic
    def __len__ (self) :
        return len(self.lines)

    def __str__ (self) :
        line_block = ''
        for line in self.lines :
            line_block += line + '\n'

        return self.title + '\n' + line_block
