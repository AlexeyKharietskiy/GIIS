from model.Shapes.Shape import Shape
from model.Algorithms.LineAlgorithms.LineBresenhamAlgorithm import BresenhamAlgorithm
from model.Algorithms.LineAlgorithms.DDAAlgorithm import DDAAlgorithm
from model.Algorithms.LineAlgorithms.WuAlgorithm import WuAlgorithm

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

    def draw_dots(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.start, self.end)
