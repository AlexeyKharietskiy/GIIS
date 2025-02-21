from view.ShapeDrawWindow import ShapeDrawWindow
from view.InputWindows.Line.LineInputWindow import LineInputWindow
from model.Dot import Dot
from model.Shapes.Line import Line
from controller.InputController import InputController


class LineController(InputController):
    def __init__(self, algorithm):
        super().__init__(algorithm)

    def run_output_window(self, start, end, debug_mode):
        self.shape = Line(Dot(start[0], start[1]), Dot(end[0], end[1]))
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode)
        self.output_window.show_shape()
        self.shape.clear_dot_list()

    def run_input_window(self):
        self.check_input_window()
        self.input_window = LineInputWindow(self)
        self.input_window.run()
