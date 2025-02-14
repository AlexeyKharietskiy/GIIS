from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.Hyperbola import Hyperbola


class HyperbolaController:
    def __init__(self, algorithm):
        self.output_window = None
        self.algorithm = algorithm
        self.shape = None

    def run_output_window(self, center, a, b, debug_mode):
        self.shape = Hyperbola(Dot(center[0], center[1]), a, b)
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode)
        self.output_window.show_shape()