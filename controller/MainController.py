from view.LineInputDataWindow import LineInputDataWindow
import tkinter

class MainController:
    def __init__(self):
        self.line_input_window = None

    def run_line_input_window(self, algorithm):
        if self.line_input_window is not None:
            try:
                if self.line_input_window.exist():
                    self.line_input_window.destroy()
            except tkinter.TclError:
                pass
        self.line_input_window = LineInputDataWindow(algorithm)
        self.line_input_window.run()
