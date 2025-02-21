from controller.Curve.CurveController import CurveController
from controller.Line.LineController import LineController
from controller.SecondOrder.ParabolaController import ParabolaController
from controller.SecondOrder.EllipseController import EllipseController
from controller.SecondOrder.HyperbolaController import HyperbolaController
from controller.SecondOrder.CircleController import CircleController
from view.MainWindow import MainWindow


class MainController:
    def __init__(self):
        self.input_data_window = None
        self.main_window = MainWindow(self)
        self.controller = None

    def run_line_input_window(self, algorithm):
        if not isinstance(self.controller, LineController):
            self.controller = LineController(algorithm)
        self.controller.run_input_window()

    def run_circle_input_window(self, algorithm):
        if not isinstance(self.controller, LineController):
            self.controller = CircleController(algorithm)
        self.controller.run_input_window()

    def run_ellipse_input_window(self, algorithm):
        if not isinstance(self.controller, LineController):
            self.controller = EllipseController(algorithm)
        self.controller.run_input_window()

    def run_hyperbola_input_window(self, algorithm):
        if not isinstance(self.controller, LineController):
            self.controller = HyperbolaController(algorithm)
        self.controller.run_input_window()

    def run_parabola_input_window(self, algorithm):
        if not isinstance(self.controller, LineController):
            self.controller = ParabolaController(algorithm)
        self.controller.run_input_window()

    def run_curve_input_window(self, algorithm):
        if not isinstance(self.controller, LineController):
            self.controller = CurveController(algorithm)
        self.controller.run_input_window()

    def run_app(self):
        self.main_window.run()