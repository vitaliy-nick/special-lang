import math
from Classes.shape3d import Shape3D

class Cylinder(Shape3D):
    def __init__(self, size, height):
        super().__init__(size)
        self.height = height

    def project_to_2d(self):
        projection_height = self.height * 2
        projection_width = self.size * 2
        projection = [[" " for _ in range(int(projection_width * 2))] for _ in range(int(projection_height))]
        radius = self.size // 2

        points_top = [(radius * math.cos(theta), radius * math.sin(theta), self.height // 2)
                      for theta in [i * math.pi / 8 for i in range(16)]]
        points_bottom = [(radius * math.cos(theta), radius * math.sin(theta), -self.height // 2)
                         for theta in [i * math.pi / 8 for i in range(16)]]

        rotated_top = [self.apply_rotation(x, y, z) for x, y, z in points_top]
        rotated_bottom = [self.apply_rotation(x, y, z) for x, y, z in points_bottom]

        for i in range(len(rotated_top)):
            x1, y1, z1 = rotated_top[i]
            x2, y2, z2 = rotated_top[(i + 1) % len(rotated_top)]
            x1 += self.size
            y1 += self.size
            x2 += self.size
            y2 += self.size
            symbol = "." if z1 > 0 and z2 > 0 else "#"
            self.draw_line(x1 * 2, y1, x2 * 2, y2, projection, symbol)

        for i in range(len(rotated_bottom)):
            x1, y1, z1 = rotated_bottom[i]
            x2, y2, z2 = rotated_bottom[(i + 1) % len(rotated_bottom)]
            x1 += self.size
            y1 += self.size
            x2 += self.size
            y2 += self.size
            symbol = "." if z1 > 0 and z2 > 0 else "#"
            self.draw_line(x1 * 2, y1, x2 * 2, y2, projection, symbol)

        for top, bottom in zip(rotated_top, rotated_bottom):
            x1, y1, z1 = top
            x2, y2, z2 = bottom
            x1 += self.size
            y1 += self.size
            x2 += self.size
            y2 += self.size
            symbol = "." if z1 > 0 and z2 > 0 else "#"
            self.draw_line(x1 * 2, y1, x2 * 2, y2, projection, symbol)

        return projection
