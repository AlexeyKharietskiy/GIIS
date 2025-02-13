from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.dot_list = []
        self.algorithm_dict = {}

    @abstractmethod
    def draw_dots(self, algorithm):
        pass
