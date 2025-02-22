from model.Shapes.СurveSegment import CurveSegment
from model.InterpolationDot import InterpolationDot

class Curve:
    def __init__(self):
        self.segment_list = []
        self.reference_dot_list = []

    def get_curve_point_list(self, algorithm):
        dot_list = []
        for shape in self.segment_list:
            shape.draw_dots(algorithm)
            for dot in shape.dot_list:
                dot_list.append((dot.x, dot.y))
            shape.clear_dot_list()
        return dot_list

    def add_reference_dot(self, dot, join_mod):
        interpolation_dot = InterpolationDot(dot[0], dot[1], dot[2], dot[3])
        if self.reference_dot_list:
            self.add_dot_in_segment_list(interpolation_dot, join_mod)
        self.reference_dot_list.append(interpolation_dot)

    def change_reference_dot(self, dot):
        interpolation_dot = InterpolationDot(dot[0], dot[1], dot[2], dot[3])
        for i in range(len(self.reference_dot_list)):
            if interpolation_dot == self.reference_dot_list[i]:
                self.reference_dot_list[i] = interpolation_dot
                self.change_dot_in_segment(interpolation_dot)
                break

    def change_dot_in_segment(self, changed_dot):
        for i, segment in enumerate(self.segment_list):
            if segment.start == changed_dot:
                segment.start = changed_dot
            elif segment.end == changed_dot:
                segment.end = changed_dot
                break

    def add_dot_in_segment_list(self, dot, join_mode):
        if not self.segment_list:
            self.segment_list.append(CurveSegment(self.reference_dot_list[0], dot))
            return
        if join_mode:
            self.segment_list.append(CurveSegment(self.reference_dot_list[-1], dot))
        else:
            if self.reference_dot_list[-1] != self.segment_list[-1].end:
                self.segment_list.append(CurveSegment(self.reference_dot_list[-1], dot))


    def get_reference_dot_list(self):
        dot_list = []
        for dot in self.reference_dot_list:
            dot_list.append((dot.x, dot.y, dot.dx, dot.dy))
        return dot_list

    def clear_all(self):
        self.segment_list = []
        self.reference_dot_list = []

    def check_existence(self, dot):
        dot = InterpolationDot(dot[0], dot[1], 0, 0)
        if self.reference_dot_list:
            return dot == self.reference_dot_list[-1]
        else:
            return False
