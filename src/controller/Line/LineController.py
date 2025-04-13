from view.ShapeDrawWindow import ShapeDrawWindow
from view.Line.LineInputWindow import LineInputWindow
from src.model.Shapes.Line.Line import Line
from src.controller.Controller import Controller


class LineController(Controller):
    def __init__(self, daddy_window, algorithm):
        super().__init__()
        self.daddy_window = daddy_window
        self.algorithm = algorithm
        self.window = LineInputWindow(daddy_window, self)

    def get_model_info(self):
        dot_list = [(dot.x, dot.y, dot.intensity) for dot in self.shape.dot_list]
        return dot_list

    def set_model_info(self, *args):
        debug_mode = args[-1]
        self.shape = Line(*args[0:-1])
        self.shape.compute_points(self.algorithm)
        ShapeDrawWindow(self, debug_mode, size=50).show_shape()
        self.shape.clear_dot_list()

    def change_algorithm(self, algorithm):
        if not self.check_window():
            self.window = LineInputWindow(self.daddy_window, self)
            self.algorithm = algorithm


