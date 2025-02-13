from model.Shapes.Shape import Shape


class Circle(Shape):
    def __init__(self, center_dot, a, b):
        super().__init__()
        self.center = center_dot
        self.a = a
        self.b = b

    def draw_dots(self, algorithm):
        self.dot_list = algorithm.compute_points(self.center, self.a, self.b)