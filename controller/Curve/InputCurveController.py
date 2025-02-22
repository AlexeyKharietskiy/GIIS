from model.Shapes.Curve import Curve
from controller.InputController import InputController
from view.InputWindows.Curve.InputHermiteWindow import InputHermiteWindow


class InputCurveController(InputController):
    def __init__(self, daddy_window, algorithm):
        super().__init__(daddy_window, algorithm)
        self.curve = Curve()
        self.adjust_mode = False
        self.join_mode = False

    def check_existence(self, dot):
        return self.curve.check_existence(dot)

    def get_result(self):
        return self.curve.get_curve_point_list(self.algorithm)

    def get_dot_info(self, dot):
        if self.adjust_mode:
            self.curve.change_reference_dot(dot)
        else:
            self.curve.add_reference_dot(dot, self.join_mode)

    def add_dot(self, dot, join_mod):
        self.adjust_mode = False
        self.join_mode = join_mod
        self.run_window(dot)

    def change_dot(self, dot):
        self.adjust_mode = True
        self.run_window(dot)

    def get_reference_dot_list(self):
        return self.curve.get_reference_dot_list()

    def clear_all(self):
        self.curve.clear_all()

    def run_window(self, dot):
        self.check_window()
        self.window = InputHermiteWindow(self.daddy_window, self, dot)
        self.window.run()