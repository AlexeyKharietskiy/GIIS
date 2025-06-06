from src.model.shapes.shape import Shape
from src.model.shapes.dots.dot import Dot
from src.model.algorithms.line.bresenham import BresenhamAlgorithm
from src.model.algorithms.line.dda import DDAAlgorithm
from src.model.algorithms.line.wu import WuAlgorithm

class Line(Shape):
    def __init__(self, start_dot, end_dot):
        super().__init__()
        self.start = Dot(start_dot[0], start_dot[1])
        self.end = Dot(end_dot[0], end_dot[1])
        self.algorithm_dict = {
            'Алгоритм Ву': WuAlgorithm(),
            'Алгоритм ЦДА': DDAAlgorithm(),
            'Алгоритм Брезенхема': BresenhamAlgorithm()
        }

    def compute_points(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.start, self.end)
        self.unique_dot_list()

