import art
from Classes.art_operations import ArtOperations

class AsciiArtGenerator:
    def __init__(self, text, font, symbol=None):
        self.text = text
        self.font = font
        self.symbol = symbol
        self.ascii_art = ""

    def generate_art(self):
        self.ascii_art = art.text2art(self.text, font=self.font)

        if self.symbol:
            self.ascii_art = self.add_spaces_between_letters(self.ascii_art)
            self.ascii_art = self.choose_custom_symbols(self.ascii_art, self.symbol)

        return self.ascii_art

    def choose_custom_symbols(self, ascii_art, symbol):
        new_art = ""
        for char in ascii_art:
            if char == ' ':
                new_art += ' '
            elif char != '\n':
                new_art += symbol
            else:
                new_art += char
        return new_art

    def add_spaces_between_letters(self, ascii_art):
        lines = ascii_art.split('\n')
        spaced_art = ""

        for line in lines:
            spaced_line = ""
            for char in line:
                spaced_line += char + ' '
            spaced_art += spaced_line.rstrip() + '\n'
        return spaced_art

    def resize_art(self):
        art_operations = ArtOperations(self.ascii_art)
        while True:
            try:
                width = int(input("Enter new width (1 or more): "))
                height = int(input("Enter new height (1 or more): "))
                return art_operations.scale_art(width, height)
            except ValueError:
                print("Please, enter positive integers!")

    def change_symbol(self, color_choice, color_manager):
        art_operations = ArtOperations(self.ascii_art)
        art_operations.change_symbol(color_choice, color_manager)
