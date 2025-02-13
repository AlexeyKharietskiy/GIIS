from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.dot_list = []
        self.algorithm_dict = {}

    @abstractmethod
    def run_algorithm(self, algorithm):
        pass
