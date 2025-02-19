from view.InputWindows.LineInputWindow import LineInputWindow
from view.InputWindows.CircleInputWindow import CircleInputWindow
from view.InputWindows.EllipseInputWindow import EllipseInputWindow
from view.InputWindows.HyperbolaInputWindow import HyperbolaInputWindow
from view.InputWindows.ParabolaInputWindow import ParabolaInputWindow
from view.InputWindows.CurveInputWindow import CurveInputWindow
import tkinter


class MainController:
    def __init__(self):
        self.input_data_window = None

    def check_window(self):
        if self.input_data_window is not None:
            try:
                if self.input_data_window.exist():
                    self.input_data_window.destroy()
            except tkinter.TclError:
                pass

    def run_line_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = LineInputWindow(algorithm)
        self.input_data_window.run()

    def run_circle_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = CircleInputWindow(algorithm)
        self.input_data_window.run()

    def run_ellipse_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = EllipseInputWindow(algorithm)
        self.input_data_window.run()

    def run_hyperbola_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = HyperbolaInputWindow(algorithm)
        self.input_data_window.run()

    def run_parabola_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = ParabolaInputWindow(algorithm)
        self.input_data_window.run()

    def run_curve_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = CurveInputWindow(algorithm)
        self.input_data_window.run()


