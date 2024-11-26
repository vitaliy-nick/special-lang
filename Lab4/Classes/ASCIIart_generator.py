class ArtGenerator:

    def __init__(self, char_set, width, height, text):
        self.char_set = char_set
        self.width = width
        self.height = height
        self.text = text

    def generate_art(self):
        ascii_lines = ['' for _ in range(self.height)]
        for char in self.text:
            char_lines = self.char_set.get(char, [' ' * self.width] * self.height)

            if len(char_lines) < self.height:
                char_lines += [' ' * self.width] * (self.height - len(char_lines))

            for i in range(self.height):
                ascii_lines[i] += char_lines[i] + ' '
        return ascii_lines
