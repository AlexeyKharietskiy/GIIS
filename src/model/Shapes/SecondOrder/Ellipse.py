from src.model.Shapes.Shape import Shape
from src.model.Algorithms.SecondOrderAlgorithms.EllipseBresenhamAlgorithm import EllipseBresenhamAlgorithm
from src.model.Dot import Dot


class Ellipse(Shape):
    def __init__(self, center_dot, a, b):
        super().__init__()
        self.center = Dot(center_dot[0], center_dot[1])
        self.a = a
        self.b = b
        self.algorithm_dict = {
            'Эллипс': EllipseBresenhamAlgorithm()
        }

    def compute_points(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.center, self.a, self.b)
        self.unique_dot_list()



