from model.Dot import Dot


class InterpolationDot(Dot):
    def __init__(self, x, y, derivative_x, derivative_y, intensity=1):
        super().__init__(x, y, intensity)
        self.dx = derivative_x
        self.dy = derivative_y

    def __iter__(self):
        return iter((self.x, self.y, self.dx, self.dy))
