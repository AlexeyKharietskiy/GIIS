from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Algorithm import Algorithm
from model.Shapes.Circle import Circle


class CircleController:
    def __init__(self, algorithm: Algorithm):
        self.output_window = None
        self.algorithm = algorithm
        self.line = None

    def run_output_window(self, center, radius, debug_mode):
        self.line = Circle(Dot(center[0], center[1]), radius)
        dot_list = self.line.run_algorithm(self.algorithm)
        self.output_window = ShapeDrawWindow(dot_list, debug_mode)
        self.output_window.show_shape()