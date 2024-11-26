import json

class ColorService:
    def __init__(self, color_file="/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab5/config/colors.json"):
        self.colors = self.load_colors(color_file)

    def load_colors(self, color_file):
        try:
            with open('/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Lab5/Config/colors.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data["colors"]
        except FileNotFoundError:
            raise FileNotFoundError(f"File {color_file} not found.")

    def list_colors(self):
        return list(self.colors.keys())

    def get_color_code(self, color_name):
        return self.colors.get(color_name, "37")
