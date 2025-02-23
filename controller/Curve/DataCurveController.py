from model.Shapes.Curve.Curve import Curve
from controller.InputController import InputController
from view.InputWindows.Curve.InputHermiteWindow import InputHermiteWindow


class DataCurveController(InputController):
    def __init__(self, daddy_controller, algorithm):
        super().__init__(daddy_controller.window, algorithm)
        self.shape = Curve()
        self.daddy_controller = daddy_controller
        self.shape.add_observer(self)
        self.adjust_mode = False
        self.join_mode = False

    def check_existence(self, dot):
        return self.shape.check_existence(dot)

    def get_result(self):
        return self.get_reference_dot_list(), self.shape.get_result_dot_list(self.algorithm)

    def get_dot_info(self, dot):
        if self.adjust_mode:
            self.shape.change_dot(dot)
        else:
            self.shape.add_dot(dot, self.join_mode)

    def add_dot(self, dot, join_mod):
        self.adjust_mode = False
        self.join_mode = join_mod
        self.run_window(dot)

    def change_dot(self, dot):
        self.adjust_mode = True
        self.run_window(dot)

    def get_reference_dot_list(self):
        return self.shape.get_reference_dot_list()

    def clear_all(self):
        self.shape.clear_all()

    def run_window(self, dot):
        self.check_window()
        self.window = InputHermiteWindow(self.daddy_window, self, dot)
        self.window.run()

    def update(self):
        self.daddy_controller.update()