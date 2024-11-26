from colorama import Fore
from Classes.error_handler import ColorError


class ColorManager:
    def __init__(self):
        self.color_mapping = {
            "red": Fore.RED,
            "green": Fore.GREEN,
            "blue": Fore.BLUE,
            "yellow": Fore.YELLOW,
            "white": Fore.WHITE
        }
    def get_colored_art(self, ascii_art, color_choice):
        if color_choice in self.color_mapping:
            return self.color_mapping[color_choice] + ascii_art + Fore.RESET
        else:
            return ascii_art

    def select_color(self):
        while True:
            color_choice = input("Enter a text color (red, green, blue, yellow, white): ").strip().lower()
            if color_choice in self.color_mapping:
                return color_choice
            else:
                raise ColorError(color_choice)
