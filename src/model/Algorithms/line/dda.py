from src.model.algorithms.Algorithm import Algorithm
from src.model.shapes.dots.intensity_dot import IntensityDot

class DDAAlgorithm(Algorithm):
    def compute_points(self, start: IntensityDot, end: IntensityDot):
        dot_list = []
        steep = abs(end.y - start.y) > abs(end.x - start.x)
        if steep:
            start.x, start.y = self.swap(start.x, start.y)
            end.x, end.y = self.swap(end.x, end.y)

        if start.x > end.x:
            start.x, end.x = self.swap(start.x, end.x)
            start.y, end.y = self.swap(start.y, end.y)

        length = max(abs(start.x - end.x), abs(start.y - end.y))
        if length == 0:
            return[start]
        dx = (end.x - start.x)/ length
        dy = (end.y - start.y)/ length
        x = start.x + 0.5 * self.sign(dx)
        y = start.y + 0.5 * self.sign(dy)
        dot_list.append(self.check_dot(steep, IntensityDot(int(x),int(y))))
        for i in range(length):
            x = x + dx
            y = y + dy
            dot_list.append(self.check_dot(steep, IntensityDot(int(x),int(y))))

        return dot_list


    @staticmethod
    def sign(x):
        return -1 if x < 0 else (1 if x > 0 else 0)


    @staticmethod
    def swap(a, b):
        return b, a

    @staticmethod
    def check_dot(steep, dot: IntensityDot):
        if steep:
            dot.x, dot.y = dot.y, dot.x
        return dot

