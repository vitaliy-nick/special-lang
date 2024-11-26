import os
import sys

lab3_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab3_root)


from Classes.art_operations import ArtOperations
from Classes.ascii_art import AsciiArtGenerator
from Classes.color_utils import ColorManager
from Classes.file_manager import FileManager
from Classes.fonts import FontManager
from Classes.error_handler import FontError, ColorError, SymbolError

def main():
    print("\nASCII-ART Generator\n")

    while True:
        print("Select option:")
        print("1 - Create new ASCII-art")
        print("2 - Exit")

        choice = input("Select 1 or 2: ")

        if choice == '1':
            text = input("Enter text for create ASCII-art: ")

            try:
                font_manager = FontManager()
                font_choice = font_manager.select_font()

                symbol = input("Enter symbol for create ASCII-art: ")
                art_generator = AsciiArtGenerator(text, font_choice, symbol)
                ascii_art = art_generator.generate_art()

                color_manager = ColorManager()
                color_choice = color_manager.select_color()
                ascii_art_colored = color_manager.get_colored_art(ascii_art, color_choice)

                print("\nASCII-art with your symbol:")
                print(ascii_art_colored)

                art_operations = ArtOperations(ascii_art)
                art_operations.change_symbol(color_choice, color_manager)

                while True:
                    resize_option = input("Want to resize ASCII-art? (y/n): ").strip().lower()
                    if resize_option in ['y']:
                        resized_art = art_generator.resize_art()
                        ascii_art_colored = color_manager.get_colored_art(resized_art, color_choice)
                        print("\nASCII-art with new size:")
                        print(ascii_art_colored)
                    elif resize_option in ['n', '']:
                        break
                    else:
                        print("Incorrect input: Enter 'y' or 'n'.")

                save_option = input("Save ASCII-art in file? (y/n): ").strip().lower()
                if save_option in ['y']:
                    FileManager.save_to_file(ascii_art)

            except (FontError, ColorError, SymbolError) as e:
                print(e)
            except ValueError as e:
                print(e)

        elif choice == '2':
            print("Exit")
            break

        else:
            print("Wrong choice. Please, select 1 or 2.")

