from abc import ABC, abstractmethod
from view.window import Window

class Factory(ABC):

    @abstractmethod
    def create_window(self, daddy_window, controller, algorithm) -> Window:
        pass

    @abstractmethod
    def create_shape(self, *args):
        pass
