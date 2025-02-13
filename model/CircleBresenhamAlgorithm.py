from model.Algorithm import Algorithm
from model.Dot import Dot

class CircleBresenhamAlgorithm(Algorithm):
    def compute_points(self, center: Dot, radius):
        dot_list = []
        x = 0
        y = radius
        d = 3 - 2 * radius
        dot_list.append(Dot(x + center.x, y + center.y))
        while y >= x:
            x += 1
            if d > 0:
                y -= 1
                d = d + 4 * (x - y) + 10
            else:
                d = d + 4 * x + 6
            dot_list.append(Dot(x + center.x, y + center.y))
