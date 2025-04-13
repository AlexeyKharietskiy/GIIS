from src.model.InterpolationDot import InterpolationDot, Dot
from src.model.Algorithms.Algorithm import Algorithm


class HermiteAlgorithm(Algorithm):
    def __init__(self):
        self.dot_list = []
        self._hermite_matrix = [
            [2, -2, 1, 1],
            [-3, 3, -2, -1],
            [0, 0, 1, 0],
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
        step = 0.001
        dx = end_dot.x - start_dot.x
        dy = end_dot.y - start_dot.y
        scale_factor = (dx ** 2 + dy ** 2) ** 0.5
        reference_matrix = [
            [start_dot.x, start_dot.y],
            [end_dot.x, end_dot.y],
            [start_dot.x_ref_coord * scale_factor, start_dot.y_ref_coord * scale_factor],
            [end_dot.x_ref_coord * scale_factor, end_dot.y_ref_coord * scale_factor]
            ]
        cx_matrix = self.multiply_matrix(self._hermite_matrix, reference_matrix)
        t = 0
        while t <= 1:
            t_matrix = [[t ** 3, t ** 2, t, 1]]
            result = self.multiply_matrix(t_matrix, cx_matrix)
            x, y = result[0]
            dot_list.append(Dot(
                round(x) if abs(x) > 1e-5 else 0,
                round(y) if abs(y) > 1e-5 else 0
            ))
            t += step

        return dot_list