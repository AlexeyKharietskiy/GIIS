from src.model.Shapes.Curve.СurveSegment import CurveSegment
from src.model.Shapes.Dot.InterpolationDot import InterpolationDot
from  logger import logger
from src.model.Shapes.Curve.Curve import Curve


class HermiteCurve(Curve):

    def add_dot(self, dot, join_mod):
        interpolation_dot = InterpolationDot(dot[0], dot[1], dot[2], dot[3])
        if self.reference_dot_list:
            self._add_dot_in_segment(interpolation_dot, join_mod)
        self.reference_dot_list.append(interpolation_dot)
        logger.info(f'add dot {dot[0], dot[1], dot[2], dot[3]}')
        self._notify_observers()

    def change_dot(self, dot):
        interpolation_dot = InterpolationDot(dot[0], dot[1], dot[2], dot[3])
        for i in range(len(self.reference_dot_list)):
            if interpolation_dot == self.reference_dot_list[i]:
                self.reference_dot_list[i] = interpolation_dot
                self._change_dot_in_segment(interpolation_dot)
                break

    def _change_dot_in_segment(self, changed_dot):
        for i, segment in enumerate(self.segment_list):
            if segment.start == changed_dot:
                logger.info(f'change dot ({segment.start.x}, {segment.start.y}, '
                            f'{segment.start.x_ref_coord}, {segment.start.y_ref_coord}) to '
                            f'dot ({changed_dot.x}, {changed_dot.y}, '
                            f'{changed_dot.x_ref_coord}, {changed_dot.y_ref_coord})')
                segment.start = changed_dot
                break
            elif segment.end == changed_dot:
                logger.info(f'change dot ({segment.end.x}, {segment.end.y}, '
                            f'{segment.end.x_ref_coord}, {segment.end.y_ref_coord}) to '
                            f'dot ({changed_dot.x}, {changed_dot.y}, '
                            f'{changed_dot.x_ref_coord}, {changed_dot.y_ref_coord})')
                segment.end = changed_dot

        self._notify_observers()

    def _add_dot_in_segment(self, dot, join_mode):
        if not self.segment_list:
            self.segment_list.append(CurveSegment(self.reference_dot_list[0], dot))
            return
        if join_mode:
            self.segment_list.append(CurveSegment(self.reference_dot_list[-1], dot))
        else:
            if self.reference_dot_list[-1] != self.segment_list[-1].end:
                self.segment_list.append(CurveSegment(self.reference_dot_list[-1], dot))