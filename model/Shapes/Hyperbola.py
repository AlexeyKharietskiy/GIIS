from model.Shapes.Shape import Shape
from model.Algorithms.HyperbolaBresenhamAlgorithm import HyperbolaBresenhamAlgorithm

class Hyperbola(Shape):
    def __init__(self, center_dot, a, b):
        super().__init__()
        self.center = center_dot
        self.a = a
        self.b = b
        self.algorithm_dict = {
            'Гипербола': HyperbolaBresenhamAlgorithm()
        }

    def draw_dots(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.center, self.a, self.b)