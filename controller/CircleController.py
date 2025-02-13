from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Algorithms.Algorithm import Algorithm
from model.Shapes.Circle import Circle


class CircleController:
    def __init__(self, algorithm: Algorithm):
        self.output_window = None
        self.algorithm = algorithm
        self.shape = None

    def run_output_window(self, center, radius, debug_mode):
        self.shape = Circle(Dot(center[0], center[1]), radius)
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode)
        self.output_window.show_shape()