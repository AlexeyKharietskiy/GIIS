from view.LineInputDataWindow import LineInputDataWindow
from model.WuAlgorithm import WuAlgorithm
from model.DDAAlgorithm import DDAAlgorithm
from model.BresenhamAlgorithm import BresenhamAlgorithm
import tkinter


class MainController:
    def __init__(self):
        self.line_input_window = None
        self.algorithm_dict = {
            'WuAlgorithm': WuAlgorithm(),
            'DDAAlgorithm': DDAAlgorithm(),
            'BresenhamAlgorithm': BresenhamAlgorithm()
        }

    def run_line_input_window(self, algorithm):
        if self.line_input_window is not None:
            try:
                if self.line_input_window.exist():
                    self.line_input_window.destroy()
            except tkinter.TclError:
                pass
        self.line_input_window = LineInputDataWindow(self.algorithm_dict[algorithm])
        self.line_input_window.run()
