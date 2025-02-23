from controller.Curve.CanvasController import CanvasController
from controller.Line.LineController import LineController
from controller.SecondOrder.ParabolaController import ParabolaController
from controller.SecondOrder.EllipseController import EllipseController
from controller.SecondOrder.HyperbolaController import HyperbolaController
from controller.SecondOrder.CircleController import CircleController
from view.MainWindow import MainWindow


class MainController:
    def __init__(self):
        self.window = MainWindow(self)
        self.controller = None

    def run_line_input_window(self, algorithm, event=None):
        if not isinstance(self.controller, LineController):
            self.controller = LineController(self.window, algorithm)
        self.controller.run_window()

    def run_circle_input_window(self, algorithm, event=None):
        if not isinstance(self.controller, LineController):
            self.controller = CircleController(self.window, algorithm)
        self.controller.run_window()

    def run_ellipse_input_window(self, algorithm, event=None):
        if not isinstance(self.controller, LineController):
            self.controller = EllipseController(self.window, algorithm)
        self.controller.run_window()

    def run_hyperbola_input_window(self, algorithm, event=None):
        if not isinstance(self.controller, LineController):
            self.controller = HyperbolaController(self.window, algorithm)
        self.controller.run_window()

    def run_parabola_input_window(self, algorithm, event=None):
        if not isinstance(self.controller, LineController):
            self.controller = ParabolaController(self.window, algorithm)
        self.controller.run_window()

    def run_curve_input_window(self, algorithm, event=None):
        if not isinstance(self.controller, LineController):
            self.controller = CanvasController(self.window, algorithm)
        self.controller.run_window()

    def run_app(self):
        self.window.run()