from model.Algorithms.Algorithm import Algorithm
from model.Dot import Dot

class HyperbolaBresenhamAlgorithm(Algorithm):
    def compute_points(self, center: Dot, a: int, b: int):
        dot_list = []
        x = a  # Начинаем с вершины гиперболы (a, 0)
        y = 0
        a_squared = a * a
        b_squared = b * b
        two_a_squared = 2 * a_squared
        two_b_squared = 2 * b_squared

        # Начальное значение ошибки
        error = b_squared * (2 * x + 1) - a_squared

        # Построение точек в первом квадранте
        while x <= center.x + a * 2:  # Ограничиваем область построения
            dot_list.extend(self.get_hyperbola_points(center, Dot(x, y)))

            if error >= 0:
                y += 1
                error -= two_a_squared * y
            x += 1
            error += b_squared * (2 * x + 1)

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