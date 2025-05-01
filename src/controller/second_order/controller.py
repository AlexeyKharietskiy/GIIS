from src.controller.abstract_controller import Controller
from src.controller.second_order.factory import SecondOrderFactory
from view.line_drawer import ShapeDrawWindow


class SecondOrderLineController(Controller):
    def __init__(self, daddy_window, algorithm):
        super().__init__()
        self.daddy_window = daddy_window
        self.algorithm = algorithm
        self.window = SecondOrderFactory().create_window(self.daddy_window, self, self.algorithm)

    def get_model_info(self):
        dot_list = [(dot.x, dot.y, dot.intensity) for dot in self.shape.dot_list]
        return dot_list

    def set_model_info(self, *args):
        debug_mode = args[-1]
        self.shape = SecondOrderFactory().create_shape(self.algorithm, *args[0:-1])
        self.shape.compute_points(self.algorithm)
        ShapeDrawWindow(self, debug_mode, size=50).show_shape()
        self.shape.clear_dot_list()

    def change_algorithm(self, algorithm):
        if not self.check_window(self.window):
            self.algorithm = algorithm
            self.window = SecondOrderFactory().create_window(self.daddy_window, self, algorithm)
