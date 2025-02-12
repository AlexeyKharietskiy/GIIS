from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, algorithm):
        pass
