from model.Shapes.Line.Line import Line
from model.Algorithms.CurveAlgorithms.BezierAlgorithm import BezierAlgorithm
from model.Algorithms.CurveAlgorithms.BSplainAlgorithm import BSplainAlgorithm
from model.Algorithms.CurveAlgorithms.HermiteAlgorithm import HermiteAlgorithm
from model.InterpolationDot import InterpolationDot

class CurveSegment(Line):
    def __init__(self, start_dot:InterpolationDot, end_dot:InterpolationDot):
        super().__init__(start_dot, end_dot)
        self.algorithm_dict = {
            "Формы Эрмита": HermiteAlgorithm(),
            "Формы Безье": BezierAlgorithm(),
            "В-сплайн": BSplainAlgorithm()
        }

    def change_dot(self, dot):
        if dot == self.start:
            self.start = dot
        elif dot == self.end:
            self.end = dot
