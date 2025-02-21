import tkinter


class InputController:
    def __init__(self, algorithm):
        self.output_window = None
        self.input_window = None
        self.algorithm = algorithm
        self.shape = None

    def run_output_window(self, *kwargs):
        pass

    def check_input_window(self):
        if self.input_window is not None:
            try:
                if self.input_window.exist():
                    self.input_window.destroy()
            except tkinter.TclError:
                pass

    def run_input_window(self):
        pass
