from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.dot_list = []
        self.algorithm_dict = {}
        self.algorithm = None

    @abstractmethod
    def draw_dots(self, algorithm):
        pass
