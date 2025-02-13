from model.Shapes.Shape import Shape


class Circle(Shape):
    def __init__(self, center_dot, radius):
        super().__init__()
        self.center = center_dot
        self.radius = radius

    def draw_dots(self, algorithm):
        self.dot_list = algorithm.compute_points(self.center, self.radius)