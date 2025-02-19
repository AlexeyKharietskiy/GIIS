from model.Algorithms.Algorithm import Algorithm
from model.Dot import Dot


class HyperbolaBresenhamAlgorithm(Algorithm):
    def compute_points(self, center: Dot, a: int, b: int):
        dot_list = []
        x = abs(a)  # Начинаем с вершины гиперболы (a, 0)
        y = 0
        a = a * a
        b = b * b

        # Начальное значение ошибки
        error = b * (2 * x + 1) - a
        bx = x
        dx = 5

        # Построение точек в первом квадранте
        while x- bx <= dx:  # Ограничиваем область построения
            dot_list.extend(self.get_hyperbola_points(center, Dot(x, y)))

            f1 =  (error <= 0 or 2 * error - b * (2 * x + 1) <= 0)
            f2 = (error <= 0 or 2 * error - a * (2 * y + 1) > 0)
            if f1:
                x= x + 1
                error += b * (2 * x + 1)

            if f2:
                y=y+1
                error -= a * (2 * y - 1)

        return dot_list

    @staticmethod
    def get_hyperbola_points(center: Dot, dot: Dot):
        # Получаем четыре симметричные точки
        points = [
            Dot(center.x + dot.x, center.y + dot.y),  # Первый квадрант
            Dot(center.x - dot.x, center.y + dot.y),  # Второй квадрант
            Dot(center.x + dot.x, center.y - dot.y),  # Четвертый квадрант
            Dot(center.x - dot.x, center.y - dot.y),  # Третий квадрант
        ]
        return points