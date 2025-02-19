from model.InterpolationDot import InterpolationDot
from model.Shapes.Сurve import Curve


class CurveController:
    def __init__(self, algorithm):
        self.output_window = None
        self.algorithm = algorithm
        self.shape_list = []

    def get_curve_point_list(self, reference_dot_list, join_mode, adjust_mode=False):
        dot_list = []
        pair_list = []
        for point in reference_dot_list:
            dot_list.append(InterpolationDot(point[0], point[1], point[2], point[3]))
            pair_list = list(zip(dot_list,dot_list[1:]))
        if adjust_mode:
            for pair in pair_list:
                shape = Curve(pair[0], pair[1])
                self.__check_existence(shape)
                dot_list = [(dot.x, dot.y) for shape in self.shape_list for dot in shape.dot_list]
            return dot_list

        if join_mode:
            for pair in pair_list:
                shape = Curve(pair[0], pair[1])
                self.__check_existence(shape)
        else:
            for i in range(0, len(pair_list), 2):
                shape = Curve(pair_list[i][0], pair_list[i][1])
                self.__check_existence(shape)
        dot_list = [(dot.x, dot.y) for shape in self.shape_list for dot in shape.dot_list ]
        return dot_list


    def __check_existence(self, shape):
        found = False
        for i, existed_shape in enumerate(self.shape_list):
            if shape.start.x == existed_shape.start.x and shape.end.x == existed_shape.end.x \
                    and shape.start.y == existed_shape.start.y and shape.end.y == existed_shape.end.y:
                self.shape_list[i] = shape
                found = True
                break
        if not found:
            self.shape_list.append(shape)

        shape.draw_dots(self.algorithm)



