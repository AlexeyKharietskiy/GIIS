from model.Shapes.Shape import Shape
from model.Algorithms.SecondOrderAlgorithms.CircleBresenhamAlgorithm import CircleBresenhamAlgorithm


class Circle(Shape):
    def __init__(self, center_dot, radius):
        super().__init__()
        self.center = center_dot
        self.radius = radius
        self.algorithm_dict = {
            'Окружность': CircleBresenhamAlgorithm(),
        }

    def compute_points(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.center, self.radius)
        self.unique_dot_list()
