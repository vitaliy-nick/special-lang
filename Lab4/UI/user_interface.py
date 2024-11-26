from Classes.ASCIIart_generator import ArtGenerator
from Classes.art_operations import ArtOperations

def main():
    while True:
        print("Generator ASCII-arts")
        print("1. Create new ASCII-art")
        print("2. Exit")
        choice = input("Select option, 1 or 2: ").strip()

        if choice == '1':
            generator = ArtOperations()

            generator.text = input("Enter a word to convert to ASCII-art: ")
            generator.width = int(input("Enter width (default 5): ") or 5)
            generator.height = int(input("Enter the height (default is 5): ") or 5)

            generator.choose_alignment()
            generator.choose_color()

            art_generator = ArtGenerator(generator.char_set, generator.width, generator.height, generator.text)
            ascii_art = art_generator.generate_art()

            generator.display_art(ascii_art)

            print("Want to save ASCII-art in file?")
            print("1. Yes")
            print("2. No")
            save_option = input("Select option 1 or 2: ").strip()

            if save_option == '1':
                generator.save_art_to_file(ascii_art)
            elif save_option == '2':
                print("ASCII-art is not saved.")
            else:
                print("Incorrect option: ASCII art is not saved.")

        elif choice == '2':
            print("Exit from generator!")
            break
        else:
            print("Incorrect option: Please, try again!")

