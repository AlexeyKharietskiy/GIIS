from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Algorithm import Algorithm


class LineController:
    def __init__(self, algorithm:Algorithm):
        self.output_window = None
        self.algorithm = algorithm

    def run_output_window(self, start, end, debug_mode):
            self.output_window = ShapeDrawWindow(self.algorithm.compute_points(
                Dot(start[0], start[1]), Dot(end[0], end[1])), debug_mode
            )
            self.output_window.show_shape()


