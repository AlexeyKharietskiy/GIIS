from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.Line import Line


class LineController:
    def __init__(self, algorithm):
        self.output_window = None
        self.algorithm = algorithm
        self.shape = None

    def run_output_window(self, start, end, debug_mode):
        self.shape = Line(Dot(start[0], start[1]), Dot(end[0], end[1]))
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode)
        self.output_window.show_shape()



