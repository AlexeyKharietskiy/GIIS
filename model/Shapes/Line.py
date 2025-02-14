from model.Shapes.Shape import Shape
from model.Algorithms.BresenhamAlgorithm import BresenhamAlgorithm
from model.Algorithms.DDAAlgorithm import DDAAlgorithm
from model.Algorithms.WuAlgorithm import WuAlgorithm

class Line(Shape):
    def __init__(self, start_dot, end_dot):
        super().__init__()
        self.start = start_dot
        self.end = end_dot
        self.algorithm_dict = {
            'Алгоритм Ву': WuAlgorithm(),
            'Алгоритм ЦДА': DDAAlgorithm(),
            'Алгоритм Брезенхема': BresenhamAlgorithm()
        }
        self.algorithm = None

    def draw_dots(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.start, self.end)
