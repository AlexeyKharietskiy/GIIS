from model.Dot import Dot
from model.Algorithms.Algorithm import Algorithm


class BezierAlgorithm(Algorithm):
    def __init__(self):
        self._bezier_matrix = [
            [-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 3, 0, 0],
            [1, 0, 0, 0]
        ]

    @staticmethod
    def multiply_matrix(a, b):
        if len(a[0]) != len(b):
            raise ValueError("Matrix size mismatch")
        return [
            [
                sum(a_row[k] * b[k][j] for k in range(len(b)))
                for j in range(len(b[0]))
            ]
            for a_row in a
        ]

    def compute_points(self, start_dot, end_dot):
        dot_list = []
        step = 0.0005
        dx = end_dot.x - start_dot.x
        dy = end_dot.y - start_dot.y
        scale_factor = (dx ** 2 + dy ** 2) ** 0.5
        reference_matrix = [
            [start_dot.x, start_dot.y],
            [end_dot.x, end_dot.y],
            [start_dot.dx, start_dot.dy],
            [end_dot.dx, end_dot.dy]
        ]
        cx_matrix = self.multiply_matrix(self._bezier_matrix, reference_matrix)
        t = 0
        while t <= 1:
            t_matrix = [[t ** 3, t ** 2, t, 1]]
            result = self.multiply_matrix(t_matrix, cx_matrix)
            x, y = result[0]
            dot_list.append(Dot(
                round(x, 5) if abs(x) > 1e-5 else 0.0,
                round(y, 5) if abs(y) > 1e-5 else 0.0
            ))
            t += step

        return dot_list