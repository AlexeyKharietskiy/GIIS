from src.model.shapes.shape import Shape
from src.model.algorithms.second_order.hyperbola import HyperbolaBresenhamAlgorithm
from src.model.shapes.dots.intensity_dot import IntensityDot


class Hyperbola(Shape):
    def __init__(self, center_dot, a, b):
        super().__init__()
        self.center = IntensityDot(center_dot[0], center_dot[1])
        self.a = a
        self.b = b
        self.algorithm_dict = {
            'Гипербола': HyperbolaBresenhamAlgorithm()
        }

    def compute_points(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.center, self.a, self.b)
        self.unique_dot_list()
