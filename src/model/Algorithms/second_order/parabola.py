from src.model.algorithms.Algorithm import Algorithm
from src.model.shapes.dots.intensity_dot import IntensityDot


class ParabolaBresenhamAlgorithm(Algorithm):
    def compute_points(self, vertex: IntensityDot, p: int):
        dot_list = []
        x0 = vertex.x
        y0 = vertex.y
        x = 0
        y = 0
        Sd = (x + 1) ** 2 - 2 * p * (y + 1)
        Sv = (x + 1) ** 2 - 2 * p * y
        Sh = x ** 2 - 2 * p * (y + 1)
        dot_list.extend(self.get_parabola_points(vertex, IntensityDot(x0 + x, y0 + y)))

        while y + y0 < 50:
            if abs(Sh) - abs(Sv) <= 0:
                if abs(Sd) - abs(Sh) < 0:
                    x += 1
                y += 1
            else:
                if abs(Sv) - abs(Sd) > 0:
                    y += 1
                x += 1

            dot_list.extend(self.get_parabola_points(vertex, IntensityDot(x+x0, y+y0)))
            Sd = (x + 1) ** 2 - 2 * p * (y + 1)
            Sv = (x + 1) ** 2 - 2 * p * y
            Sh = x ** 2 - 2 * p * (y + 1)

        return dot_list

    @staticmethod
    def get_parabola_points(vertex, dot: IntensityDot):
        points = [
            dot,
            IntensityDot(2 * vertex.x - dot.x, dot.y)
        ]
        return points