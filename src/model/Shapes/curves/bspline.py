from src.model.algorithms.curve.bsplain import BSplainAlgorithm
from src.model.shapes.curves.curve_segment import CurveSegment
from src.model.shapes.dots.interpolation_dot import InterpolationDot
from src.model.shapes.dots.dot import Dot
from  logger import logger
from src.model.shapes.curves.curve import Curve

class BSplineCurve(Curve):
    def add_dot(self, dot, join_mod):
        ref_dot = Dot(*dot)
        if None in self.reference_dot_list:
            index = self.reference_dot_list.index(None)
            self.reference_dot_list[index] = ref_dot
        else:
            self.reference_dot_list.append(ref_dot)
        logger.info(f'add dot {dot[0], dot[1]}')

    def change_dot(self, dot):
        dot = Dot(*dot)
        for i in range(len(self.reference_dot_list)):
            if dot == self.reference_dot_list[i]:
                self.reference_dot_list[i] = None
                break

    def calculate_dot_list(self, algorithm):
        dot_list = BSplainAlgorithm().compute_points(self.reference_dot_list)
        return dot_list