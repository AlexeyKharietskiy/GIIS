from model.Shapes.Shape import Shape
from model.Algorithms.LineAlgorithms.LineBresenhamAlgorithm import BresenhamAlgorithm
from model.Algorithms.LineAlgorithms.DDAAlgorithm import DDAAlgorithm
from model.Algorithms.CurveAlgorithms.HermiteFormsAlgorithm import HermiteAlgorithm

class Curve(Shape):
    def __init__(self, reference_dot_list):
        super().__init__()
        self.reference_dot_list = reference_dot_list
        self.algorithm_dict = {
            "Формы Эрмита": HermiteAlgorithm(),
            "Формы Безье": DDAAlgorithm(),
            "В-сплайн": BresenhamAlgorithm()
        }

    def draw_dots(self, algorithm):
        self.algorithm = self.algorithm_dict[algorithm]
        self.dot_list = self.algorithm.compute_points(self.reference_dot_list)
