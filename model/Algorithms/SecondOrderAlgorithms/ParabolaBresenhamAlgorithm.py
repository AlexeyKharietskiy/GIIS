from model.Algorithms.Algorithm import Algorithm
from model.Dot import Dot


class ParabolaBresenhamAlgorithm(Algorithm):
    def compute_points(self, vertex: Dot, h: int):
        dot_list = []
        x = 0
        y = 0
        error = 0
        h += y

        # Построение точек в первом квадранте
        while y < h:  # Ограничиваем область построения
            dot_list.extend(self.get_parabola_points(vertex, Dot(x + vertex.x, y + vertex.y)))
            f1 = (error <= 0 or 2 * (error - x) - 1 <= 0)
            f2 = (error >= 0 or 2 * error + 1 > 0)
            if f1:
                x += 1
                error += 2*x + 1

            if f2:
                y += 1
                error -= 1

        return dot_list

    @staticmethod
    def get_parabola_points(vertex, dot: Dot):
        # Получаем две симметричные точки (для горизонтальной параболы)
        points = [
            dot,  # Верхняя ветвь
            Dot(2 * vertex.x - dot.x, dot.y)  # Нижняя ветвь
        ]
        return points