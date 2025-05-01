from src.model.shapes.shape import Shape
from src.model.algorithms.curve.bezier import BezierAlgorithm
from src.model.algorithms.curve.bsplain import BSplainAlgorithm
from src.model.algorithms.curve.hermite import HermiteAlgorithm
from src.model.shapes.dots.dot import Dot

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
