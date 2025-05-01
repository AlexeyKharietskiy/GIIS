from src.controller.polygon.controller import PolygonController
from src.controller.geom_refactoring.controller import GeomRefactorController
from src.controller.curve.controller import CurveController
from src.controller.line.controller import LineController
from src.controller.second_order.controller import SecondOrderLineController
from view.app_window import MainWindow


class MainController:
    def __init__(self):
        self.window = MainWindow(self)
        self._shape_dict = {
            "Кривые": CurveController,
            "Отрезки": LineController,
            "Линии второго порядка": SecondOrderLineController,
            "Геометрические преобразования": GeomRefactorController,
            "Полигон": PolygonController,
            }
        self.controller = None

    def run_shape_window(self, shape, algorithm, event=None):
        if not isinstance(self.controller, self._shape_dict[shape]):
            self.controller = self._shape_dict[shape](self.window, algorithm)
        else:
            self.controller.change_algorithm(algorithm)

    def run_app(self):
        self.window.run()

