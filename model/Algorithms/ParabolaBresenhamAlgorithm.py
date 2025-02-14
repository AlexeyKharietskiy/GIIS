from model.Algorithms.Algorithm import Algorithm
from model.Dot import Dot

class BresenhamParabolaAlgorithm(Algorithm):
    def compute_points(self, vertex: Dot, a: int):
        dot_list = []
        x = 0
        y = 0
        error = 0

        # Построение точек в первом квадранте
        while x <= vertex.x + 100:  # Ограничиваем область построения
            dot_list.extend(self.get_parabola_points(vertex, Dot(x, y)))

            # Обновляем ошибку и координаты
            if error >= 0:
                y += 1
                error -= 4 * a
            x += 1
            error += 2 * y + 1

        return dot_list

    @staticmethod
    def get_parabola_points(vertex: Dot, dot: Dot):
        # Получаем две симметричные точки (для горизонтальной параболы)
        points = [
            Dot(vertex.x + dot.x, vertex.y + dot.y),  # Верхняя ветвь
            Dot(vertex.x + dot.x, vertex.y - dot.y),  # Нижняя ветвь
        ]
        return points