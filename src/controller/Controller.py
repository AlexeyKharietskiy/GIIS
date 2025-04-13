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

    @staticmethod
    def check_window(window):
        if window is not None:
            try:
                if window.exist():
                    window.destroy()
            except tk.TclError:
                pass
