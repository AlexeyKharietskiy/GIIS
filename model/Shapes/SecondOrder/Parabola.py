from model.Shapes.Shape import Shape
from model.Algorithms.SecondOrderAlgorithms.ParabolaBresenhamAlgorithm import ParabolaBresenhamAlgorithm

class Parabola(Shape):
    def __init__(self, center_dot, h):
        super().__init__()
        self.center = center_dot
        self.h = h
        self.algorithm_dict={
            'Парабола': ParabolaBresenhamAlgorithm()
        }


    def compute_points(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.center, self.h)
        self.unique_dot_list()