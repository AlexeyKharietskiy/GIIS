from abc import ABC, abstractmethod

class Algorithm(ABC):
    @abstractmethod
    def compute_points(self, *kwargs):
        pass
