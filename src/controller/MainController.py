from src.controller.Curve.CurveController import CurveController
from src.controller.Line.LineController import LineController
from src.controller.SecondOrder.SecondOrderLineController import SecondOrderLineController
from  view.MainWindow import MainWindow


class MainController:
    def __init__(self):
        self.window = MainWindow(self)
        self._shape_dict = {
            "Кривые": CurveController,
            "Отрезки": LineController,
            "Линии второго порядка": SecondOrderLineController
            }
        self.controller = None

    def run_shape_window(self, shape, algorithm, event=None):
        if not isinstance(self.controller, self._shape_dict[shape]):
            self.controller = self._shape_dict[shape](self.window, algorithm)
        else:
            self.controller.change_algorithm(algorithm)

    def run_app(self):
        self.window.run()

