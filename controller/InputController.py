from controller.Controller import Controller

class InputController(Controller):
    def __init__(self, daddy_window, algorithm):
        super().__init__()
        self.daddy_window = daddy_window
        self.output_window = None
        self.window = None
        self.algorithm = algorithm
        self.shape = None

    def run_window(self, *args):
        pass

    def get_model_info(self):
        pass

    def set_model_info(self, *args):
        pass

