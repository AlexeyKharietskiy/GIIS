from src.model.Dot import Dot
from src.model.Algorithms.Algorithm import Algorithm
import numpy as np


class BSplainAlgorithm(Algorithm):
    def __init__(self):
        super().__init__()
        """
        Инициализация B-сплайна
        :param control_points: список контрольных точек в формате [(x1, y1), (x2, y2), ...]
        :param closed: флаг, указывающий, должен ли сплайн быть замкнутым
        """
        self.M = np.array([
            [-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 0, 3, 0],
            [1, 4, 1, 0]
        ]) / 6.0

    def _get_control_points_array(self, control_dots):
        """Конвертирует список Dot в массив numpy для вычислений"""
        return np.array([(dot.x, dot.y) for dot in control_dots])

    def evaluate_segment(self, i, t, control_dots):
        """
        Вычисляет точку на сегменте сплайна между контрольными точками i и i+1
        :param i: индекс первой контрольной точки сегмента
        :param t: параметр t в диапазоне [0, 1)
        :return: объект Dot с координатами точки
        """
        # Получаем массив контрольных точек
        points = self._get_control_points_array(control_dots)

        # Получаем 4 контрольные точки для текущего сегмента
        segment_points = points[i - 1:i + 3]

        # Вектор параметра t
        T = np.array([t ** 3, t ** 2, t, 1])

        # Вычисляем координаты точки
        x = T @ self.M @ segment_points[:, 0]
        y = T @ self.M @ segment_points[:, 1]

        # Возвращаем объект Dot
        return int(x), int(y)

    def compute_points(self, dot_list, points_per_segment=500):
        """
        Вычисляет точки на всем сплайне
        :param points_per_segment: количество точек на каждом сегменте
        :return: список объектов Dot, представляющих точки сплайна
        """
        control_dots=dot_list
        control_dots = (
                control_dots[-3:] +
                control_dots +
                control_dots[:3]
        )
        spline_dots = []

        # Определяем количество сегментов
        n = len(control_dots)
        segments = n - 3

        for i in range(1, segments + 1):
            for t in np.linspace(0, 1, points_per_segment, endpoint=False):
                spline_dots.append(self.evaluate_segment(i, t, control_dots))


        return spline_dots