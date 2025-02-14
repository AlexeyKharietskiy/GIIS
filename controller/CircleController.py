from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.Circle import Circle


class CircleController:
    def __init__(self, algorithm):
        self.output_window = None
        self.algorithm = algorithm
        self.shape = None

    def run_output_window(self, center, radius, debug_mode):
        self.shape = Circle(Dot(center[0], center[1]), radius)
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode, size=50)
        self.output_window.show_shape()