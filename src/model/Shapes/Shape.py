from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.dot_list = []
        self.algorithm_dict = {}
        self.algorithm = None

    @abstractmethod
    def compute_points(self, algorithm):
        pass

    def clear_dot_list(self):
        self.dot_list = []

    def unique_dot_list(self):
        unique_list = []
        for dot in self.dot_list:
            if dot not in unique_list:
                unique_list.append(dot)
        self.dot_list = unique_list