from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.WuAlgorithm import WuAlgorithm
from model.DDAAlgorithm import DDAAlgorithm
from model.BresenhamAlgorithm import BresenhamAlgorithm


class LineController:
    def __init__(self, algorithm):
        self.output_window = None
        self.algorithm = algorithm

    def run_output_window(self, start, end, debug_mode):
        if self.algorithm == 'WuAlgorithm':
            self.algorithm = WuAlgorithm()
            self.output_window = ShapeDrawWindow(self.algorithm.compute_points(
                Dot(start[0], start[1]), Dot(end[0], end[1])), debug_mode
            )
            self.output_window.show_shape()
        elif self.algorithm == 'DDAAlgorithm':
            self.algorithm = DDAAlgorithm()
            self.output_window = ShapeDrawWindow(self.algorithm.compute_points(
                Dot(start[0], start[1]), Dot(end[0], end[1])), debug_mode
            )
            self.output_window.show_shape()
        else:
            self.algorithm = BresenhamAlgorithm()
            self.output_window = ShapeDrawWindow(self.algorithm.compute_points(
                Dot(start[0], start[1]), Dot(end[0], end[1])), debug_mode
            )
            self.output_window.show_shape()


