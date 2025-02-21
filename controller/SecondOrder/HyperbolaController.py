from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.Hyperbola import Hyperbola
from view.InputWindows.SecondOrder.HyperbolaInputWindow import HyperbolaInputWindow
from controller.InputController import InputController


class HyperbolaController(InputController):
    def __init__(self, algorithm):
        super().__init__(algorithm)

    def run_output_window(self, center, a, b, debug_mode):
        self.shape = Hyperbola(Dot(center[0], center[1]), a, b)
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode, size=70)
        self.output_window.show_shape()

    def run_input_window(self):
        self.check_input_window()
        self.input_window = HyperbolaInputWindow(self)
        self.input_window.run()