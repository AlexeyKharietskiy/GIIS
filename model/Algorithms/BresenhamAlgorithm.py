from model.Algorithms.Algorithm import Algorithm
from model.Dot import Dot

class BresenhamAlgorithm(Algorithm):
    def compute_points(self, start: Dot, end: Dot):
        dot_list = []
        steep = abs(end.y - start.y) > abs(end.x - start.x)
        if steep:
            start.x, start.y = self.swap(start.x, start.y)
            end.x, end.y = self.swap(end.x, end.y)

        if start.x > end.x:
            start.x, end.x = self.swap(start.x, end.x)
            start.y, end.y = self.swap(start.y, end.y)
        x = start.x
        y = start.y
        dx = end.x - start.x
        dy = end.y - start.y
        e = 2 * dy - dx
        dot_list.append(self.check_dot(steep, Dot(x,y)))
        i = 1
        while i <= dx :
            if e >= 0:
                y += 1
                e -= 2 * dx
            x += 1
            e += 2 * dy
            i += 1
            dot_list.append(self.check_dot(steep, Dot(x,y)))
        return dot_list

    @staticmethod
    def swap(a, b):
        return b, a

    @staticmethod
    def check_dot(steep, dot: Dot):
        if steep:
            dot.x, dot.y = dot.y, dot.x
        return dot