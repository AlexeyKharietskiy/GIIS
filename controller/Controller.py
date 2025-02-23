from abc import ABC, abstractmethod
import tkinter as tk


class Controller(ABC):
    def __init__(self):
        self.window = None
        self.shape = None

    @abstractmethod
    def get_model_info(self):
        pass

    @abstractmethod
    def set_model_info(self, *args):
        pass

    @abstractmethod
    def run_window(self):
        pass

    def check_window(self):
        if self.window is not None:
            try:
                if self.window.exist():
                    self.window.destroy()
            except tk.TclError:
                pass
