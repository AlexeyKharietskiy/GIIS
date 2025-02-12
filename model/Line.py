from Shape import Shape
from DDAAlgorithm import DDAAlgorithm
from BresenhamAlgorithm import BresenhamAlgorithm
from WuAlgorithm import WuAlgorithm
from Dot import Dot


class Line(Shape):
    def __init__(self, start_dot, end_dot):
        super().__init__()
        self.start = start_dot
        self.end = end_dot

    def draw(self, algorithm):
        self.dot_list = algorithm.compute_points(self.start, self.end)
