import math

class Shape3D:
    def __init__(self, size):
        self.size = size
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.color_code = "37"

    def set_color(self, color_code):
        self.color_code = color_code

    def rotate(self, angle_x=0, angle_y=0, angle_z=0):
        self.angle_x += math.radians(angle_x)
        self.angle_y += math.radians(angle_y)
        self.angle_z += math.radians(angle_z)

    def apply_rotation(self, x, y, z):
        y, z = (y * math.cos(self.angle_x) - z * math.sin(self.angle_x),
                y * math.sin(self.angle_x) + z * math.cos(self.angle_x))
        x, z = (x * math.cos(self.angle_y) + z * math.sin(self.angle_y),
                -x * math.sin(self.angle_y) + z * math.cos(self.angle_y))
        x, y = (x * math.cos(self.angle_z) - y * math.sin(self.angle_z),
                x * math.sin(self.angle_z) + y * math.cos(self.angle_z))
        return int(x), int(y), int(z)

    def draw_line(self, x1, y1, x2, y2, canvas, symbol):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        while True:
            if 0 <= y1 < len(canvas) and 0 <= x1 < len(canvas[0]):
                canvas[int(y1)][int(x1)] = symbol
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def project_to_2d(self):
        raise NotImplementedError("Method project_to_2d must be implemented in a subclass!")

    def render_ascii(self, projection):
        color_code = f"\033[{self.color_code}m"
        reset_code = "\033[0m"
        for row in projection:
            print(color_code + "".join(row) + reset_code)

