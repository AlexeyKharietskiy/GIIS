from src.controller.factory import Factory
from view.second_order.circle import CircleInputWindow
from view.second_order.ellipse import EllipseInputWindow
from view.second_order.hyperbola import HyperbolaInputWindow
from view.second_order.parabola import ParabolaInputWindow
from view.curve.curve_canvas import CurveWindow
from src.model.shapes.second_order.circle import Circle
from src.model.shapes.second_order.ellipse import Ellipse
from src.model.shapes.second_order.hyperbola import Hyperbola
from src.model.shapes.second_order.parabola import Parabola
from src.model.shapes.shape import Shape


class SecondOrderFactory(Factory):
    def __init__(self):
        self._algorithm_shape_dict = {
            'Окружность': (CircleInputWindow, Circle),
            'Эллипс': (EllipseInputWindow, Ellipse),
            'Гипербола': (HyperbolaInputWindow, Hyperbola),
            'Парабола': (ParabolaInputWindow, Parabola)
        }

    def create_window(self, daddy_window, controller, algorithm) -> CurveWindow:
        return self._algorithm_shape_dict[algorithm][0](daddy_window, controller)

    def create_shape(self, algorithm, *args)->Shape:
        return self._algorithm_shape_dict[algorithm][1](*args)
