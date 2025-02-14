from model.Shapes.Shape import Shape


class Parabola(Shape):
    def __init__(self, center_dot, h):
        super().__init__()
        self.center = center_dot
        self.h = h

    def draw_dots(self, algorithm):
        self.dot_list = algorithm.compute_points(self.center, self.a, self.b)