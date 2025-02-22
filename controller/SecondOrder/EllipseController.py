from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.Ellipse import Ellipse
from controller.InputController import InputController
from view.InputWindows.SecondOrder.EllipseInputWindow import EllipseInputWindow


class EllipseController(InputController):
    def __init__(self, daddy_window, algorithm):
        super().__init__(daddy_window, algorithm)

    def get_result(self, center, a, b, debug_mode):
        self.shape = Ellipse(Dot(center[0], center[1]), a, b)
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode, size=50)
        self.output_window.show_shape()

    def run_input_window(self):
        self.check_window()
        self.window = EllipseInputWindow(self.daddy_window, self)
        self.window.run()