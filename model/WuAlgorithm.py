from Algorithm import Algorithm
from Dot import Dot

class WuAlgorithm(Algorithm):
    def compute_points(self, start: Dot, end: Dot):
        dot_list = []
        steep = abs(end.y - start.y) > abs(end.x - start.x)
        if steep:
            start.x, start.y = self.swap(start.x, start.y)
            end.x, end.y = self.swap(end.x, end.y)

        if start.x > end.x:
            start.x, end.x = self.swap(start.x, end.x)
            start.y, end.y = self.swap(start.y, end.y)
        dot_list.append(self.check_dot(steep, Dot(start.x, start.y, 1)))
        dot_list.append(self.check_dot(steep, Dot(end.x, end.y, 1)))

        dx = float(end.x - start.x)
        dy = float(end.y - start.y)
        gradient = dy / dx if dx != 0 else 0

        y = start.y + gradient
        for x in range(start.x + 1, end.x):
            dot_list.append(self.check_dot(steep, Dot(x, int(y), 1 - (y - int(y)))))
            dot_list.append(self.check_dot(steep, Dot(x, int(y) + 1, y - int(y))))
            y += gradient

        return dot_list

    @staticmethod
    def swap(a, b):
        return b, a

    @staticmethod
    def check_dot(steep, dot: Dot):
        if steep:
            dot.x, dot.y = dot.y, dot.x
        return dot


a = WuAlgorithm()
b = a.compute_points(Dot(0,0), Dot(9,4))
for i in b :
    print(f"{i.x} {i.y} {i.intensity}")