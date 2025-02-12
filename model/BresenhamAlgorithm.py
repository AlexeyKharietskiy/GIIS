from model.Algorithm import Algorithm
from model.Dot import Dot

class BresenhamAlgorithm(Algorithm):
    def compute_points(self, start: Dot, end: Dot):
        dot_list = []
        x = start.x
        y = start.y
        dx = end.x - start.x
        dy = end.y - start.y
        e = 2 * dy - dx
        dot_list.append(Dot(x,y))
        i = 1
        while i <= dx :
            if e >= 0:
                y += 1
                e -= 2 * dx
            x += 1
            e += 2 * dy
            i += 1
            dot_list.append(Dot(x,y))
        return dot_list
