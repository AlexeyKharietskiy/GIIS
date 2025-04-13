from src.model.Algorithms.Algorithm import Algorithm
from src.model.Dot import Dot


class ParabolaBresenhamAlgorithm(Algorithm):
    def compute_points(self, vertex: Dot, p: int):
        dot_list = []
        x0 = vertex.x
        y0 = vertex.y
        x = 0
        y = 0
        Sd = (x + 1) ** 2 - 2 * p * (y + 1)
        Sv = (x + 1) ** 2 - 2 * p * y
        Sh = x ** 2 - 2 * p * (y + 1)
        dot_list.extend(self.get_parabola_points(vertex, Dot(x0 + x, y0 + y)))

        while y + y0 < 50:
            if abs(Sh) - abs(Sv) <= 0:
                if abs(Sd) - abs(Sh) < 0:
                    x += 1
                y += 1
            else:
                if abs(Sv) - abs(Sd) > 0:
                    y += 1
                x += 1

            dot_list.extend(self.get_parabola_points(vertex, Dot(x+x0, y+y0)))
            Sd = (x + 1) ** 2 - 2 * p * (y + 1)
            Sv = (x + 1) ** 2 - 2 * p * y
            Sh = x ** 2 - 2 * p * (y + 1)

        return dot_list

    @staticmethod
    def get_parabola_points(vertex, dot: Dot):
        points = [
            dot,
            Dot(2 * vertex.x - dot.x, dot.y)
        ]
        return points