from abc import ABC, abstractmethod
from view.window import Window
import tkinter as tk
from tkinter import ttk

class CurveWindow(ABC, Window):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.title("Построение кривых")
        self.state("zoomed")
        self.main_frame = ttk.Frame(self)
        self.control_frame = ttk.Frame(self.main_frame)
        self.btn_clear = ttk.Button(
            self.control_frame,
            text="Очистить",
            command=self.clear_canvas
        )

        self.canvas = tk.Canvas(
            self.main_frame,
            bg="white",
        )
        self.pack_all()


    def pack_all(self):
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.control_frame.pack(fill=tk.X)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        self.canvas.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

    @abstractmethod
    def adjust_dot(self, event):
        pass

    @abstractmethod
    def add_dot(self, event):
        pass

    def draw_curve(self, event=None):
        self.canvas.delete("curve")
        reference_dot_list, dot_list = self.controller.get_model_info()
        if dot_list:
            for curve in dot_list:
                self.canvas.create_line(curve, fill='black', width=3, tags='curve')
        self.canvas.tag_raise("dot")

    def clear_canvas(self, event=None):
        self.canvas.delete('all')
        self.controller.clear_canvas()

    @abstractmethod
    def on_enter_dot(self, event):
        pass

    @abstractmethod
    def on_exit_dot(self, event):
        pass
