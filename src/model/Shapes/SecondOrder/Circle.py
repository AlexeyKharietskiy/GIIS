from src.model.Shapes.Shape import Shape
from src.model.Algorithms.SecondOrderAlgorithms.CircleBresenhamAlgorithm import CircleBresenhamAlgorithm
from src.model.Shapes.Dot.dot import Dot

class Circle(Shape):
    def __init__(self, center_dot, radius):
        super().__init__()
        self.center = Dot(center_dot[0], center_dot[1])
        self.radius = radius
        self.algorithm_dict = {
            'Окружность': CircleBresenhamAlgorithm(),
        }

    def compute_points(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.center, self.radius)
        self.unique_dot_list()
