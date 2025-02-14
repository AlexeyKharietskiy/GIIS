from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.Parabola import Parabola


class ParabolaController:
    def __init__(self, algorithm):
        self.output_window = None
        self.algorithm = algorithm
        self.shape = None

    def run_output_window(self, center, high, debug_mode):
        self.shape = Parabola(Dot(center[0], center[1]), high)
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode, size = 70)
        self.output_window.show_shape()



