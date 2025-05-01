import tkinter as tk
from tkinter import messagebox
from view.window import Window

class CircleInputWindow(Window):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.debug_mode = False
        self.entry_xc = None
        self.entry_yc = None
        self.entry_radius = None
        self.create_widgets_circle()
        self.center_window()

    def create_widgets_circle(self):
        frame_point1 = tk.LabelFrame(self, text="Центр окружности", padx=10, pady=10)
        frame_point1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point1, text="Xc:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_xc = tk.Entry(frame_point1)
        self.entry_xc.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point1, text="Yc:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_yc = tk.Entry(frame_point1)
        self.entry_yc.grid(row=1, column=1, padx=5, pady=5)

        frame_radius = tk.LabelFrame(self, text="Радиус", padx=10, pady=10)
        frame_radius.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_radius, text="R:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_radius = tk.Entry(frame_radius)
        self.entry_radius.grid(row=0, column=1, padx=5, pady=5)

        frame_options = tk.LabelFrame(self, text="Настройки", padx=10, pady=10)
        frame_options.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        tk.Checkbutton(frame_options, text="Режим отладки", command=self.reverse_debug).grid(row=0, column=0, padx=5,
                                                                                             pady=5)

        tk.Button(self, text="Построить окружность", command=self.return_data).grid(row=2, column=0,
                                                                                    columnspan=2, padx=10,
                                                                                    pady=10, sticky="ew")

    def reverse_debug(self):
        self.debug_mode = not self.debug_mode

    def return_data(self):
        try:
            xc = int(self.entry_xc.get())
            yc = int(self.entry_yc.get())
            r = int(self.entry_radius.get())
            self.destroy()
            self.controller.set_model_info((xc, yc), r, self.debug_mode)
        except ValueError:
            self.destroy()
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения.")