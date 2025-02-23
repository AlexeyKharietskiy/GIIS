from controller.Controller import Controller
from view.CanvasWindow import CanvasWindow
from controller.Curve.DataCurveController import DataCurveController


class CanvasController(Controller):
    def __init__(self, daddy_window, algorithm):
        super().__init__()
        self.daddy_window = daddy_window
        self.input_controller = None
        self.join_mode = False
        self.algorithm = algorithm

    def clear_canvas(self):
        self.input_controller.clear_all()

    def toggle_seamless_mode(self, event=None):
        self.join_mode = not self.join_mode
        self.window.seamless_var.set(self.join_mode)

    def change_point(self, x, y):
        dot = (x, y)
        self.input_controller.change_dot(dot)

    def get_model_info(self):
        unprocess_reference_dot_list, unprocess_dot_list = self.input_controller.get_result()
        dot_list = [(dot[0], dot[1]) for dot in unprocess_dot_list]
        reference_dot_list = [(dot[0], dot[1]) for dot in unprocess_reference_dot_list]
        return reference_dot_list, dot_list

    def set_model_info(self, x, y):
        dot = (x, y)
        self.input_controller.add_dot(dot, self.join_mode)
        return self.input_controller.check_existence(dot)

    def run_window(self):
        self.window = CanvasWindow(self.daddy_window, self)
        self.input_controller = DataCurveController(self, self.algorithm)
        self.window.run()

    def update(self):
        self.window.draw_curve()