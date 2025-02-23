from view.ShapeDrawWindow import ShapeDrawWindow
from view.InputWindows.Line.LineInputWindow import LineInputWindow
from model.Dot import Dot
from model.Shapes.Line.Line import Line
from controller.InputController import InputController


class LineController(InputController):
    def __init__(self, daddy_window, algorithm):
        super().__init__(daddy_window, algorithm)

    def get_result(self, start, end, debug_mode):
        self.shape = Line(Dot(start[0], start[1]), Dot(end[0], end[1]))
        self.shape.compute_points(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode)
        self.output_window.show_shape()
        self.shape.clear_dot_list()

    def run_window(self):
        self.check_window()
        self.window = LineInputWindow(self.daddy_window, self)
        self.window.run()
