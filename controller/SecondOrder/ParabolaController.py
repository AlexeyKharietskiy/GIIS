from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.SecondOrder.Parabola import Parabola
from controller.InputController import InputController
from view.InputWindows.SecondOrder.ParabolaInputWindow import ParabolaInputWindow


class ParabolaController(InputController):
    def __init__(self, daddy_window, algorithm):
        super().__init__(daddy_window, algorithm)

    def get_result(self, center, high, debug_mode):
        self.shape = Parabola(Dot(center[0], center[1]), high)
        self.shape.compute_points(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode, size = 70)
        self.output_window.show_shape()

    def run_window(self):
        self.check_window()
        self.window = ParabolaInputWindow(self.daddy_window, self)
        self.window.run()