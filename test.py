import numpy as np
import matplotlib.pyplot as plt


class BSpline:
    def __init__(self, control_points, closed=False):
        """
        Инициализация B-сплайна
        :param control_points: список контрольных точек в формате [(x1, y1), (x2, y2), ...]
        :param closed: флаг, указывающий, должен ли сплайн быть замкнутым
        """
        self.control_points = np.array(control_points)
        self.closed = closed
        self.M = np.array([
            [-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 0, 3, 0],
            [1, 4, 1, 0]
        ]) / 6.0

        if closed:
            # Для замкнутого сплайна добавляем дополнительные точки
            self.control_points = np.vstack([
                self.control_points[-3:],
                self.control_points,
                self.control_points[:3]
            ])

    def evaluate_segment(self, i, t):
        """
        Вычисляет точку на сегменте сплайна между контрольными точками i и i+1
        :param i: индекс первой контрольной точки сегмента
        :param t: параметр t в диапазоне [0, 1)
        :return: координаты точки (x, y)
        """
        # Получаем 4 контрольные точки для текущего сегмента
        points = self.control_points[i - 1:i + 3]

        # Вектор параметра t
        T = np.array([t ** 3, t ** 2, t, 1])

        # Вычисляем координаты точки
        x = T @ self.M @ points[:, 0]
        y = T @ self.M @ points[:, 1]

        return x, y

    def evaluate(self, num_points=100):
        """
        Вычисляет точки на всем сплайне
        :param num_points: количество точек на каждом сегменте
        :return: массивы x и y координат точек сплайна
        """
        x_vals = []
        y_vals = []

        # Определяем количество сегментов
        n = len(self.control_points)
        if self.closed:
            segments = n - 3
        else:
            segments = n - 3

        for i in range(1, segments + 1):
            for t in np.linspace(0, 1, num_points, endpoint=False):
                x, y = self.evaluate_segment(i, t)
                x_vals.append(x)
                y_vals.append(y)

        # Добавляем последнюю точку
        if not self.closed:
            x, y = self.evaluate_segment(segments, 1.0)
            x_vals.append(x)
            y_vals.append(y)
        return np.array(x_vals), np.array(y_vals)

    def plot(self, num_points=100, show_control_points=True):
        """
        Визуализация B-сплайна
        :param num_points: количество точек на каждом сегменте
        :param show_control_points: показывать ли контрольные точки
        """
        x_vals, y_vals = self.evaluate(num_points)

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, 'b-', label='B-сплайн')

        if show_control_points:
            # Для замкнутого сплайна показываем только исходные точки
            if self.closed:
                n = len(self.control_points) - 6
                points = self.control_points[3:3 + n]
            else:
                points = self.control_points

            plt.plot(points[:, 0], points[:, 1], 'ro--', label='Контрольные точки')
            for i, (x, y) in enumerate(points):
                plt.text(x, y, f'P{i + 1}', fontsize=12)

        plt.title('B-сплайн')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.legend()
        plt.axis('equal')
        plt.show()


# Пример использования для незамкнутого сплайна
control_points = [(0, 0), (5, 5), (2, 1), (3, 7)]
spline = BSpline(control_points, closed=False)
spline.plot()

# Пример использования для замкнутого сплайна (как в учебном пособии)
control_points_closed = [(2, 0), (4, 0), (4, 2), (4, 4), (2, 4), (0, 4), (0, 2), (0, 0)]
spline_closed = BSpline(control_points_closed, closed=True)
spline_closed.plot()