import tkinter as tk
from tkinter import messagebox
from controller.SecondOrder.ParabolaController import ParabolaController


class ParabolaInputWindow:
    def __init__(self, algorithm):
        super().__init__()
        self.root.title("Ввод нужных данных")
        self.controller = ParabolaController(algorithm)
        self.debug_mode = False
        self.entry_x = None
        self.entry_a = None
        self.entry_y = None
        self.create_widgets()

    def create_widgets(self):

        frame_point1 = tk.LabelFrame(self.root, text="Вершина", padx=10, pady=10)
        frame_point1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point1, text="X:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_x = tk.Entry(frame_point1)
        self.entry_x.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point1, text="Y:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_y = tk.Entry(frame_point1)
        self.entry_y.grid(row=1, column=1, padx=5, pady=5)

        frame_point2 = tk.LabelFrame(self.root, text="Высота параболы", padx=10, pady=10)
        frame_point2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point2, text="A:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_a = tk.Entry(frame_point2)
        self.entry_a.grid(row=0, column=1, padx=5, pady=5)

        frame_options = tk.LabelFrame(self.root, text="Настройки", padx=10, pady=10)
        frame_options.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        tk.Checkbutton(frame_options, text="Режим отладки", command=self.reverse_debug).grid(row=0, column=0, padx=5,
                                                                                           pady=5)

        tk.Button(self.root, text="Построить отрезок", command=self.show_line).grid(row=2, column=0,
                                                                                                 columnspan=2, padx=10,
                                                                                                 pady=10, sticky="ew")

    def reverse_debug(self):
        self.debug_mode = not self.debug_mode

    def show_line(self):
        try:
            x = int(self.entry_x.get())
            y = int(self.entry_y.get())
            a = int(self.entry_a.get())
            self.controller.run_output_window((x,y), a, self.debug_mode)
            self.root.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения.")

    def run(self):
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()

    def exist(self):
        return self.root.winfo_exists()