from model.Algorithms.Algorithm import Algorithm
from model.Dot import Dot

class CircleBresenhamAlgorithm(Algorithm):
    def compute_points(self, center: Dot, radius):
        dot_list = []
        disp_x = center.x
        disp_y = center.y
        x = 0
        y = radius
        delta = (1 - 2 * radius)
        error = 0
        while y >= 0:
            dot_list.append(Dot(disp_x + x, disp_y + y))
            dot_list.append(Dot(disp_x + x, disp_y - y))
            dot_list.append(Dot(disp_x - x, disp_y + y))
            dot_list.append(Dot(disp_x - x, disp_y - y))

            error = 2 * (delta + y) - 1
            if delta < 0 and error <= 0:
                x += 1
                delta = delta + (2 * x + 1)
                continue
            error = 2 * (delta - x) - 1
            if delta > 0 and error > 0:
                y -= 1
                delta = delta + (1 - 2 * y)
                continue
            x += 1
            delta = delta + (2 * (x - y))
            y -= 1
        return dot_list
