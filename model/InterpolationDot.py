from model.Dot import Dot


class InterpolationDot(Dot):
    def __init__(self, x, y, derivative_x, derivative_y, intensity=1):
        super().__init__(x, y, intensity)
        self.derivative_x = derivative_x
        self.derivative_y = derivative_y