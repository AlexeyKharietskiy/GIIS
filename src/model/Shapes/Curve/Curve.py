from src.model.Dot import Dot
from abc import ABC, abstractmethod


class Curve(ABC):
    def __init__(self):
        self.segment_list = []
        self.reference_dot_list = []
        self._observer_list = []

    def add_observer(self, observer):
        self._observer_list.append(observer)

    def _notify_observers(self):
        for observer in self._observer_list:
            observer.update()

    def calculate_dot_list(self, algorithm):
        dot_list = []

        for segment in self.segment_list:
            segment.compute_points(algorithm)
            curve = []
            for dot in segment.dot_list:
                curve.append((dot.x, dot.y))

                # dot_list.append()
            dot_list.append(curve)
            segment.clear_dot_list()

        return dot_list

    def clear_all(self):
        self.segment_list = []
        self.reference_dot_list = []
        self._notify_observers()

    def check_existence(self, dot):
        int_dot = Dot(*dot)
        if self.reference_dot_list:
            return int_dot == self.reference_dot_list[-1]
        else:
            return False

    def get_reference_dot_list(self):
        dot_list = []
        for dot in self.reference_dot_list:
            dot_list.append((dot.x, dot.y))
        return dot_list

    @abstractmethod
    def add_dot(self, dot, join_mod):
        pass

    @abstractmethod
    def change_dot(self, dot):
        pass

