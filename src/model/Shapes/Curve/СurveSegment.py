from src.model.Shapes.Shape import Shape
from src.model.Algorithms.CurveAlgorithms.BezierAlgorithm import BezierAlgorithm
from src.model.Algorithms.CurveAlgorithms.BSplainAlgorithm import BSplainAlgorithm
from src.model.Algorithms.CurveAlgorithms.HermiteAlgorithm import HermiteAlgorithm
from src.model.Shapes.Dot.dot import Dot

class CurveSegment(Shape):
    def __init__(self, start_dot: Dot, end_dot: Dot):
        super().__init__()
        self.start = start_dot
        self.end = end_dot
        self.algorithm_dict = {
            "Формы Эрмита": HermiteAlgorithm,
            "Формы Безье": BezierAlgorithm,
            "В-сплайн": BSplainAlgorithm
        }

    def change_dot(self, dot):
        if dot == self.start:
            self.start = dot
        elif dot == self.end:
            self.end = dot

    def compute_points(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]()
        self.dot_list = self.algorithm.compute_points(self.start, self.end)
        self.unique_dot_list()
