from model.InterpolationDot import InterpolationDot
from model.Shapes.Сurve import Curve


class CurveController:
    def __init__(self, algorithm):
        self.output_window = None
        self.algorithm = algorithm
        self.shape = None

    def get_curve_point_list(self, reference_dot_list):
        dot_list = []
        for point in reference_dot_list:
            dot_list.append(InterpolationDot(point[0], point[1], point[2], point[3]))
        self.shape = Curve(dot_list)
        dot_list = []
        self.shape.draw_dots(self.algorithm)
        for point in self.shape.dot_list:
            dot_list.append((point.x, point.y))
        return dot_list



