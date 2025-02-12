from abc import ABC, abstractmethod


class InputDataWindow(ABC):
    @abstractmethod
    def run(self):
        pass