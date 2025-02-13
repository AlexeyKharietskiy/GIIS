from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Algorithm import Algorithm
from model.Shapes.Line import Line


class LineController:
    def __init__(self, algorithm:Algorithm):
        self.output_window = None
        self.algorithm = algorithm
        self.line = None

    def run_output_window(self, start, end, debug_mode):
        self.line = Line(Dot(start[0], start[1]), Dot(end[0], end[1]))
        dot_list = self.line.run_algorithm(self.algorithm)
        self.output_window = ShapeDrawWindow(dot_list, debug_mode)
        self.output_window.show_shape()



