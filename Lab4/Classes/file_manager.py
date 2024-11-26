import os

class FileManager:
    @staticmethod
    def save_art_to_file(ascii_art):
        if not os.path.exists('/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab4/Data'):
            os.makedirs('/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab4/Data')

        filename = input("Enter a file name to save ASCII-art with extension .txt: ")
        filepath = os.path.join('/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab4/Data', filename)

        with open(filepath, 'w') as file:
            for line in ascii_art:
                file.write(line + '\n')

        print(f"ASCII-art was saved in file {filepath}")
