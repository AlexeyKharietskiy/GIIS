from src.controller.factory import Factory
from view.curve.hermite import HermiteCurveWindow
from view.curve.bezier import BezierCurveWindow
from view.curve.bsplain import BSplainCurveWindow
from view.curve.curve_canvas import CurveWindow
from src.model.shapes.curves.hermite import HermiteCurve
from src.model.shapes.curves.bspline import BSplineCurve
from src.model.shapes.curves.bezier import BezierCurve

class CurveFactory(Factory):
    def __init__(self):
        self._algorithm_dict = {
            "Формы Эрмита": (HermiteCurveWindow, HermiteCurve),
            "Формы Безье": (BezierCurveWindow, BezierCurve),
            "В-сплайн": (BSplainCurveWindow, BSplineCurve)
        }

    def create_window(self, daddy_window, controller, algorithm) -> CurveWindow:
        return self._algorithm_dict[algorithm][0](daddy_window, controller)

    def create_shape(self, algorithm, *args):
        return self._algorithm_dict[algorithm][1](*args)