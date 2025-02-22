import tkinter as tk
from view.InputWindows.InputWindow import InputWindow
from tkinter import messagebox

class HyperbolaInputWindow(InputWindow):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.debug_mode = False
        self.entry_xc = None
        self.entry_a = None
        self.entry_b = None
        self.entry_yc = None
        self.entry_radius = None
        self.create_widgets()

    def create_widgets(self):

        frame_point1 = tk.LabelFrame(self, text="Центр", padx=10, pady=10)
        frame_point1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point1, text="Xc:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_xc = tk.Entry(frame_point1)
        self.entry_xc.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point1, text="Yc:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_yc = tk.Entry(frame_point1)
        self.entry_yc.grid(row=1, column=1, padx=5, pady=5)

        frame_point2 = tk.LabelFrame(self, text="Характеристики гиперболы", padx=10, pady=10)
        frame_point2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point2, text="A:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_a = tk.Entry(frame_point2)
        self.entry_a.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point2, text="B:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_b = tk.Entry(frame_point2)
        self.entry_b.grid(row=1, column=1, padx=5, pady=5)

        frame_options = tk.LabelFrame(self, text="Настройки", padx=10, pady=10)
        frame_options.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        tk.Checkbutton(frame_options, text="Режим отладки", command=self.reverse_debug).grid(row=0, column=0, padx=5,
                                                                                           pady=5)

        tk.Button(self, text="Построить отрезок", command=self.return_data).grid(row=2, column=0,
                                                                                 columnspan=2, padx=10,
                                                                                 pady=10, sticky="ew")

    def reverse_debug(self):
        self.debug_mode = not self.debug_mode

    def return_data(self):
        try:
            xc = int(self.entry_xc.get())
            yc = int(self.entry_yc.get())
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            self.controller.get_result((xc, yc), a, b, self.debug_mode)
            self.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения.")
