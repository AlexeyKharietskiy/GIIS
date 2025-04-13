from src.factories.Factory import Factory
from view.SecondOrder.CircleInputWindow import CircleInputWindow
from view.SecondOrder.EllipseInputWindow import EllipseInputWindow
from view.SecondOrder.HyperbolaInputWindow import HyperbolaInputWindow
from view.SecondOrder.ParabolaInputWindow import ParabolaInputWindow
from view.Curve.CurveWindow import CurveWindow
from src.model.Shapes.SecondOrder.Circle import Circle
from src.model.Shapes.SecondOrder.Ellipse import Ellipse
from src.model.Shapes.SecondOrder.Hyperbola import Hyperbola
from src.model.Shapes.SecondOrder.Parabola import Parabola
from src.model.Shapes.Shape import Shape


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
