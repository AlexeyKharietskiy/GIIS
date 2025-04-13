from  src.factories.Factory import Factory
from  view.Curve.HermiteCurveWindow import HermiteCurveWindow
from  view.Curve.BezierCurveWindow import BezierCurveWindow
from  view.Curve.BSplainCurveWindow import BSplainCurveWindow
from  view.Curve.CurveWindow import CurveWindow
from src.model.Shapes.Curve.HermiteCurve import HermiteCurve
from src.model.Shapes.Curve.BsplineCurve import BSplineCurve
from src.model.Shapes.Curve.BezierCurve import BezierCurve

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