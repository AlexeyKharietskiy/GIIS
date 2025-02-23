from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.SecondOrder.Circle import Circle
from controller.InputController import InputController
from view.InputWindows.SecondOrder.CircleInputWindow import CircleInputWindow


class CircleController(InputController):
    def __init__(self, daddy_window, algorithm):
        super().__init__(daddy_window, algorithm)

    def get_result(self, center, radius, debug_mode):
        self.shape = Circle(Dot(center[0], center[1]), radius)
        self.shape.compute_points(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode, size=50)
        self.output_window.show_shape()

    def run_window(self):
        self.check_window()
        self.window = CircleInputWindow(self.daddy_window, self)
        self.window.run()