from model.Shapes.Shape import Shape


class Circle(Shape):
    def __init__(self, center_dot, radius):
        super().__init__()
        self.center = center_dot
        self.radius = radius

    def run_algorithm(self, algorithm):
        self.dot_list = algorithm.compute_points(self.center, self.radius)
        return self.dot_list
