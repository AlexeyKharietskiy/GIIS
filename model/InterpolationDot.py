from model.Dot import Dot


class InterpolationDot(Dot):
    def __init__(self, x, y, derivative_x, derivative_y, intensity=1):
        super().__init__(x, y, intensity)
        self.dx = derivative_x
        self.dy = derivative_y

    def __eq__(self, other):
        if isinstance(other, InterpolationDot):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        return iter((self.x, self.y, self.dx, self.dy))
