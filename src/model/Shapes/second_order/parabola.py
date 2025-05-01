from src.model.shapes.shape import Shape
from src.model.algorithms.second_order.parabola import ParabolaBresenhamAlgorithm
from src.model.shapes.dots.intensity_dot import IntensityDot


class Parabola(Shape):
    def __init__(self, center_dot, p):
        super().__init__()
        self.center = IntensityDot(center_dot[0], center_dot[1])
        self.p = p
        self.algorithm_dict={
            'Парабола': ParabolaBresenhamAlgorithm()
        }


    def compute_points(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.center, self.p)
        self.unique_dot_list()