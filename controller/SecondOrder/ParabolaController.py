from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.Parabola import Parabola
from controller.InputController import InputController
from view.InputWindows.SecondOrder.ParabolaInputWindow import ParabolaInputWindow

class ParabolaController(InputController):
    def __init__(self, algorithm):
        super().__init__(algorithm)

    def run_output_window(self, center, high, debug_mode):
        self.shape = Parabola(Dot(center[0], center[1]), high)
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode, size = 70)
        self.output_window.show_shape()

    def run_input_window(self):
        self.check_input_window()
        self.input_window = ParabolaInputWindow(self)
        self.input_window.run()