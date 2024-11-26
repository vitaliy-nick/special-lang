class AlignmentManager:

    def __init__(self):
        self.alignment = "center"

    def choose_alignment(self):
        print("Select text alignment:")
        print("1. Left")
        print("2. Center")
        print("3. Right")

        alignment_option = input("Select option 1, 2 or 3: ").strip()
        if alignment_option == '1':
            self.alignment = "left"
        elif alignment_option == '2':
            self.alignment = "center"
        elif alignment_option == '3':
            self.alignment = "right"
        else:
            print("Incorrect option: Default center alignment (center) is set.")
            self.alignment = "center"

    def _align_line(self, line, width):
        if self.alignment == 'left':
            return line.ljust(width)
        elif self.alignment == 'center':
            return line.center(width)
        elif self.alignment == 'right':
            return line.rjust(width)
        else:
            return line
