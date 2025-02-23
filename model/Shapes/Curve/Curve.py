from model.Shapes.Curve.СurveSegment import CurveSegment
from model.InterpolationDot import InterpolationDot
from logger import logger


class Curve:
    def __init__(self):
        self.segment_list = []
        self.reference_dot_list = []
        self._observer_list = []

    def check_existence(self, dot):
        dot = InterpolationDot(dot[0], dot[1], 0, 0)
        if self.reference_dot_list:
            return dot == self.reference_dot_list[-1]
        else:
            return False

    def get_reference_dot_list(self):
        dot_list = []
        for dot in self.reference_dot_list:
            dot_list.append((dot.x, dot.y))
        return dot_list

    def get_result_dot_list(self, algorithm):
        dot_list = []
        for shape in self.segment_list:
            shape.compute_points(algorithm)
            for dot in shape.dot_list:
                dot_list.append((dot.x, dot.y))
            shape.clear_dot_list()
        return dot_list

    def add_dot(self, dot, join_mod):
        interpolation_dot = InterpolationDot(dot[0], dot[1], dot[2], dot[3])
        if self.reference_dot_list:
            self._add_dot_in_segment(interpolation_dot, join_mod)
        self.reference_dot_list.append(interpolation_dot)
        logger.info(f'add dot ({dot[0]}, {dot[1]})')
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
                            f'{segment.start.dx}, {segment.start.dy}) to '
                            f'dot ({changed_dot.x}, {changed_dot.y}, '
                            f'{changed_dot.dx}, {changed_dot.dy})')
                segment.start = changed_dot
                break

            elif segment.end == changed_dot:
                logger.info(f'change dot ({segment.end.x}, {segment.end.y}, '
                            f'{segment.end.dx}, {segment.end.dy}) to '
                            f'dot ({changed_dot.x}, {changed_dot.y}, '
                            f'{changed_dot.dx}, {changed_dot.dy})')
                segment.end = changed_dot
                break
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

    def clear_all(self):
        self.segment_list = []
        self.reference_dot_list = []

    def add_observer(self, observer):
        self._observer_list.append(observer)

    def _notify_observers(self):
        for observer in self._observer_list:
            observer.update()
