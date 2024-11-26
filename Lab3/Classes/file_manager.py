from pathlib import Path

class FileManager:
    @staticmethod
    def save_to_file(ascii_art):
        data_dir = Path('/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab3/data')
        data_dir.mkdir(parents=True, exist_ok=True)

        filename = input("Enter name of file to save (without the extension): ") + '.txt'
        file_path = data_dir / filename

        with file_path.open('w') as f:
            f.write(ascii_art)

        print(f"ASCII-art was saved in file {file_path}")
