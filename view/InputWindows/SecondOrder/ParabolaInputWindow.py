import tkinter as tk
from tkinter import messagebox
from view.InputWindows.InputWindow import InputWindow


class ParabolaInputWindow(InputWindow):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.debug_mode = False
        self.entry_x = None
        self.entry_a = None
        self.entry_y = None
        self.create_widgets()

    def create_widgets(self):

        frame_point1 = tk.LabelFrame(self, text="Вершина", padx=10, pady=10)
        frame_point1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point1, text="X:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_x = tk.Entry(frame_point1)
        self.entry_x.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point1, text="Y:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_y = tk.Entry(frame_point1)
        self.entry_y.grid(row=1, column=1, padx=5, pady=5)

        frame_point2 = tk.LabelFrame(self, text="Высота параболы", padx=10, pady=10)
        frame_point2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point2, text="A:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_a = tk.Entry(frame_point2)
        self.entry_a.grid(row=0, column=1, padx=5, pady=5)

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
            x = int(self.entry_x.get())
            y = int(self.entry_y.get())
            a = int(self.entry_a.get())
            self.controller.get_result((x, y), a, self.debug_mode)
            self.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения.")
