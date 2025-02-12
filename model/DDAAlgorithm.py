from Algorithm import Algorithm
from Dot import Dot

class DDAAlgorithm(Algorithm):
    def compute_points(self, start: Dot, end: Dot):
        dot_list = []
        length = max(abs(start.x - end.x), abs(start.y - end.y))
        dx = (end.x - start.x)/ length
        dy = (end.y - start.y)/ length
        x = start.x + 0.5 * self.sign(dx)
        y = start.y + 0.5 * self.sign(dy)
        dot_list.append(Dot(int(x),int(y)))
        for i in range(length):
            x = x + dx
            y = y + dy
            dot_list.append(Dot(int(x),int(y)))

        return dot_list


    @staticmethod
    def sign(x):
        return -1 if x < 0 else (1 if x > 0 else 0)

