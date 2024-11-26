from Classes.error_handler import FontError

class FontManager:
    def __init__(self):
        self.fonts = [
            "dot", "shadow", "banner", "dancing", "slant",
            "straight", "block", "caligraphy", "stellar", "ghost", "3d"
        ]

    def display_fonts(self):
        print("\nAvailable fonts:")
        print(", ".join(self.fonts))

    def select_font(self):
        self.display_fonts()

        font_choice = input("Enter a font name from the list: ").strip()

        if font_choice not in self.fonts:
            raise FontError(f"Font '{font_choice}' not found. Please, try again!")

        return font_choice
