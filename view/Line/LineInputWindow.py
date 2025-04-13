import tkinter as tk
from tkinter import messagebox
from view.Window import Window


class LineInputWindow(Window):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.title('Входные данные')
        self.debug_mode = False
        self.entry_x1 = None
        self.entry_y1 = None
        self.entry_x2 = None
        self.entry_y2 = None
        self.create_widgets_line()
        self.center_window()

    def create_widgets_line(self):
        frame_point1 = tk.LabelFrame(self, text="Точка 1", padx=10, pady=10)
        frame_point1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point1, text="X1:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_x1 = tk.Entry(frame_point1)
        self.entry_x1.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point1, text="Y1:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_y1 = tk.Entry(frame_point1)
        self.entry_y1.grid(row=1, column=1, padx=5, pady=5)

        frame_point2 = tk.LabelFrame(self, text="Точка 2", padx=10, pady=10)
        frame_point2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point2, text="X2:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_x2 = tk.Entry(frame_point2)
        self.entry_x2.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point2, text="Y2:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_y2 = tk.Entry(frame_point2)
        self.entry_y2.grid(row=1, column=1, padx=5, pady=5)

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
            x1 = int(self.entry_x1.get())
            y1 = int(self.entry_y1.get())
            x2 = int(self.entry_x2.get())
            y2 = int(self.entry_y2.get())
            self.destroy()
            self.controller.set_model_info((x1, y1), (x2, y2), self.debug_mode)
        except ValueError:
            self.destroy()
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения.")
