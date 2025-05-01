from src.controller.abstract_controller import Controller
from src.controller.curve.factory import CurveFactory

class CurveController(Controller):
    def __init__(self, daddy_window, algorithm):
        super().__init__()
        self.daddy_window = daddy_window
        self.join_mode = False
        self.adjust_mode = False
        self.algorithm = algorithm
        self.shape = CurveFactory().create_shape(algorithm)
        self.shape.add_observer(self)
        self.window = CurveFactory().create_window(self.daddy_window, self, self.algorithm)
        self.input_window = None

    def clear_canvas(self):
        self.shape.clear_all()

    def set_model_info(self, data):
        if self.adjust_mode:
            self.shape.change_dot(data)
        else:
            self.shape.add_dot(data, self.join_mode)

    def toggle_seamless_mode(self, event=None):
        self.join_mode = not self.join_mode
        self.window.seamless_var.set(self.join_mode)

    def toggle_adjust_mode(self, value=None):
        if value is not None:
            self.adjust_mode = value
        else:
            self.adjust_mode = not self.adjust_mode

    def get_model_info(self):
        reference_dot_list = self.shape.get_reference_dot_list()
        dot_list = self.shape.calculate_dot_list(self.algorithm)
        return reference_dot_list, dot_list

    def update(self):
        self.window.draw_curve()

    def change_algorithm(self, algorithm):
        if not self.check_window(self.window):
            self.algorithm = algorithm
            self.shape = CurveFactory().create_shape(algorithm)
            self.shape.add_observer(self)
            self.window = CurveFactory().create_window(self.daddy_window, self, algorithm)

    def check_existence(self, dot):
        return self.shape.check_existence(dot)