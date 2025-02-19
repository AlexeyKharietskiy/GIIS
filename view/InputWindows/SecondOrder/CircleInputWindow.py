import tkinter as tk
from tkinter import messagebox
from controller.SecondOrder.CircleController import CircleController
from view.InputWindows.InputWindow import InputWindow

class CircleInputWindow(InputWindow):
    def __init__(self, algorithm):
        super().__init__()
        self.root.title("Ввод нужных данных")
        self.controller = CircleController(algorithm)
        self.debug_mode = False
        self.entry_xc = None
        self.entry_yc = None
        self.entry_radius = None
        self.create_widgets_circle()


    def create_widgets_circle(self):
        frame_point1 = tk.LabelFrame(self.root, text="Центр окружности", padx=10, pady=10)
        frame_point1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point1, text="Xc:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_xc = tk.Entry(frame_point1)
        self.entry_xc.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point1, text="Yc:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_yc = tk.Entry(frame_point1)
        self.entry_yc.grid(row=1, column=1, padx=5, pady=5)

        frame_radius = tk.LabelFrame(self.root, text="Радиус", padx=10, pady=10)
        frame_radius.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_radius, text="R:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_radius = tk.Entry(frame_radius)
        self.entry_radius.grid(row=0, column=1, padx=5, pady=5)

        frame_options = tk.LabelFrame(self.root, text="Настройки", padx=10, pady=10)
        frame_options.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        tk.Checkbutton(frame_options, text="Режим отладки", command=self.reverse_debug).grid(row=0, column=0, padx=5,
                                                                                             pady=5)

        tk.Button(self.root, text="Построить окружность", command=self.show_circle).grid(row=2, column=0,
                                                                                    columnspan=2, padx=10,
                                                                                    pady=10, sticky="ew")

    def reverse_debug(self):
        self.debug_mode = not self.debug_mode

    def show_circle(self):
        try:
            xc = int(self.entry_xc.get())
            yc = int(self.entry_yc.get())
            r = int(self.entry_radius.get())
            self.controller.run_output_window((xc,yc), r, self.debug_mode)
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