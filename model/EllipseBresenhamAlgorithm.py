from model.Algorithm import Algorithm
from model.Dot import Dot

class BresenhamEllipseAlgorithm(Algorithm):
    def compute_points(self, center, a, b):
        dot_list = []
        x = 0
        y = b
        a_squared = a * a
        b_squared = b * b
        two_a_squared = 2 * a_squared
        two_b_squared = 2 * b_squared
        four_a_squared = 4 * a_squared
        four_b_squared = 4 * b_squared

        # Initial decision parameter for region 1
        d1 = b_squared - a_squared * b + 0.25 * a_squared
        dx = two_b_squared * x
        dy = two_a_squared * y

        # Region 1
        while dx < dy:
            dot_list.extend(self.get_ellipse_points(center, Dot(x, y)))
            x += 1
            dx += two_b_squared
            if d1 < 0:
                d1 += dx + b_squared
            else:
                y -= 1
                dy -= two_a_squared
                d1 += dx - dy + b_squared

        # Decision parameter for region 2
        d2 = b_squared * (x + 0.5) * (x + 0.5) + a_squared * (y - 1) * (y - 1) - a_squared * b_squared

        # Region 2
        while y >= 0:
            dot_list.extend(self.get_ellipse_points(center, Dot(x, y)))
            y -= 1
            dy -= two_a_squared
            if d2 > 0:
                d2 += a_squared - dy
            else:
                x += 1
                dx += two_b_squared
                d2 += dx - dy + a_squared

        return dot_list

    @staticmethod
    def get_ellipse_points(center: Dot, dot: Dot):
        # Get all four symmetric points
        points = [
            Dot(center.x + dot.x, center.y + dot.y),
            Dot(center.x - dot.x, center.y + dot.y),
            Dot(center.x + dot.x, center.y - dot.y),
            Dot(center.x - dot.x, center.y - dot.y),
        ]
        return points