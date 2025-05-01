from src.model.shapes.dots.dot import Dot


class IntensityDot(Dot):
    def __init__(self, x, y, intensity=1):
        super().__init__(x, y)
        self.intensity = intensity