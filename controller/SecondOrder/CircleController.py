from view.ShapeDrawWindow import ShapeDrawWindow
from model.Dot import Dot
from model.Shapes.Circle import Circle
from controller.InputController import InputController
from view.InputWindows.SecondOrder.CircleInputWindow import CircleInputWindow



class CircleController(InputController):
    def __init__(self, algorithm):
        super().__init__(algorithm)

    def run_output_window(self, center, radius, debug_mode):
        self.shape = Circle(Dot(center[0], center[1]), radius)
        self.shape.draw_dots(self.algorithm)
        self.output_window = ShapeDrawWindow(self.shape, debug_mode, size=50)
        self.output_window.show_shape()

    def run_input_window(self):
        self.check_input_window()
        self.input_window = CircleInputWindow(self)
        self.input_window.run()