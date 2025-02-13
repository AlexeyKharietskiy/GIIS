from view.InputWindows.LineInputWindow import LineInputWindow
from view.InputWindows.CircleInputWindow import CircleInputWindow
from view.InputWindows.EllipseInputWindow import EllipseInputWindow
from model.Algorithms.WuAlgorithm import WuAlgorithm
from model.Algorithms.DDAAlgorithm import DDAAlgorithm
from model.Algorithms.BresenhamAlgorithm import BresenhamAlgorithm
from model.Algorithms.CircleBresenhamAlgorithm import CircleBresenhamAlgorithm
from model.Algorithms.EllipseBresenhamAlgorithm import BresenhamEllipseAlgorithm
import tkinter


class MainController:
    def __init__(self):
        self.input_data_window = None
        self.algorithm_dict = {
            'Алгоритм Ву': WuAlgorithm(),
            'Алгоритм ЦДА': DDAAlgorithm(),
            'Алгоритм Брезенхема': BresenhamAlgorithm(),
            'Окружность': CircleBresenhamAlgorithm(),
            'Эллипс': BresenhamEllipseAlgorithm()
        }

    def run_line_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = LineInputWindow(self.algorithm_dict[algorithm])
        self.input_data_window.run()

    def run_circle_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = CircleInputWindow(self.algorithm_dict[algorithm])
        self.input_data_window.run()

    def run_ellipse_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = EllipseInputWindow(self.algorithm_dict[algorithm])
        self.input_data_window.run()

    def check_window(self):
        if self.input_data_window is not None:
            try:
                if self.input_data_window.exist():
                    self.input_data_window.destroy()
            except tkinter.TclError:
                pass
