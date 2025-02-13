from view.InputWindows.LineInputDataWindow import LineInputDataWindow
from model.Algorithms.WuAlgorithm import WuAlgorithm
from model.Algorithms.DDAAlgorithm import DDAAlgorithm
from model.Algorithms.BresenhamAlgorithm import BresenhamAlgorithm
from model.Algorithms.CircleBresenhamAlgorithm import CircleBresenhamAlgorithm
from view.InputWindows.CircleInputWindow import CircleInputWindow
import tkinter


class MainController:
    def __init__(self):
        self.input_data_window = None
        self.algorithm_dict = {
            'Алгоритм Ву': WuAlgorithm(),
            'Алгоритм ЦДА': DDAAlgorithm(),
            'Алгоритм Брезенхема': BresenhamAlgorithm(),
            'Окружность': CircleBresenhamAlgorithm()
        }

    def run_line_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = LineInputDataWindow(self.algorithm_dict[algorithm])
        self.input_data_window.run()

    def run_circle_input_window(self, algorithm):
        self.check_window()
        self.input_data_window = CircleInputWindow(self.algorithm_dict[algorithm])
        self.input_data_window.run()

    def check_window(self):
        if self.input_data_window is not None:
            try:
                if self.input_data_window.exist():
                    self.input_data_window.destroy()
            except tkinter.TclError:
                pass
