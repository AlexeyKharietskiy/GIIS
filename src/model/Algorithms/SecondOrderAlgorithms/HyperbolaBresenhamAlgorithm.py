from src.model.Algorithms.Algorithm import Algorithm
from src.model.Shapes.Dot.dot import Dot


class HyperbolaBresenhamAlgorithm(Algorithm):
    def compute_points(self, center: Dot, a: int, b: int):
        x0, y0 = center.x, center.y
        points = []

        # Инициализация начальных значений
        x = a
        y = 0
        d = b ** 2 * (2 * x + 1) - 2 * a ** 2 * (y + 1) + a ** 2

        # Построение в первом квадранте (x >= a, y >= 0)
        if a >= b:
            # Горизонтальная гипербола
            x = a
            y = 0
            d = b**2 * (2 * x + 1) - 2 * a**2 * (y + 1) + a**2

            while x <= 100:  # Ограничение для предотвращения бесконечного цикла
                points.extend(self.get_symmetric_points(center, Dot(x, y)))

                if d < 0:
                    d += b**2 * (2 * x + 3)
                else:
                    d += b**2 * (2 * x + 3) - 4 * a**2 * (y + 1)
                    y += 1
                x += 1
        else:
            # Вертикальная гипербола
            x = 0
            y = b
            d = a**2 * (2 * y + 1) - 2 * b**2 * (x + 1) + b**2

            while y <= 100:  # Ограничение для предотвращения бесконечного цикла
                points.extend(self.get_symmetric_points(center, Dot(x, y)))

                if d < 0:
                    d += a**2 * (2 * y + 3)
                else:
                    d += a**2 * (2 * y + 3) - 4 * b**2 * (x + 1)
                    x += 1
                y += 1

        return points


    @staticmethod
    def get_symmetric_points(center: Dot, dot: Dot):
        """Генерирует симметричные точки для всех квадрантов"""
        x0, y0 = center.x, center.y
        return [
            Dot(x0 + dot.x, y0 + dot.y),  # Первый квадрант
            Dot(x0 - dot.x, y0 + dot.y),  # Второй квадрант
            Dot(x0 - dot.x, y0 - dot.y),  # Третий квадрант
            Dot(x0 + dot.x, y0 - dot.y)  # Четвертый квадрант
        ]