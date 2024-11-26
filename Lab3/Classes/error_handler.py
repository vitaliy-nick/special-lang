class FontError(Exception):
    def __init__(self, font):
        self.message = f"Error: Incorrect font!'{font}'."
        super().__init__(self.message)

class ColorError(Exception):
    def __init__(self, color):
        self.message = f"Error: Incorrect color!'{color}'."
        super().__init__(self.message)

class SymbolError(Exception):
    def __init__(self, symbol):
        self.message = "Error: Symbol cannot be empty!"
        super().__init__(self.message)
