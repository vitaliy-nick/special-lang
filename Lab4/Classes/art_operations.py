import os

from Classes.alignment_manager import AlignmentManager
from Classes.file_manager import FileManager
from Classes.color_manager import ColorManager


class ArtOperations:
    def __init__(self):
        self.color_manager = ColorManager()
        self.char_set = {}
        self.load_characters()
        self.width = 0
        self.height = 0
        self.text = ""
        self.alignment_manager = AlignmentManager()

    def load_characters(self):
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#_+-:,. ":
            if char.isupper():
                filename = f"/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab4/Assets/letters/{char}{char}.txt"
            elif char.islower():
                filename = f"/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab4/Assets/letters/{char}.txt"
            elif char.isdigit():
                filename = f"/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab4/Assets/numbers/{char}.txt"
            else:
                filename = f"/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab4/Assets/symbols/{char}.txt"

            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    self.char_set[char] = [line.rstrip('\n') for line in file.readlines()]
            else:
                self.char_set[char] = [' ' * 10] * 10

    def choose_alignment(self):
        self.alignment_manager.choose_alignment()

    def choose_color(self):
        self.color_manager.choose_color()

    def apply_color(self, text):
        return self.color_manager.apply_color(text)

    def display_art(self, ascii_art):
        for line in ascii_art:
            colored_line = self.apply_color(line)
            aligned_line = self.alignment_manager._align_line(colored_line, self.width * len(self.text))
            print(aligned_line)

    def save_art_to_file(self, ascii_art):
        FileManager.save_art_to_file(ascii_art)
