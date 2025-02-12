from view.InputDataWindow import InputDataWindow
import tkinter as tk
from tkinter import messagebox
from controller.LineController import LineController

class LineInputDataWindow(InputDataWindow):
    def __init__(self, algorithm):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Ввод нужных данных")
        self.controller = LineController(algorithm)
        self.debug_mode = False

        self.create_widgets()

    def create_widgets(self):

        frame_point1 = tk.LabelFrame(self.root, text="Точка 1", padx=10, pady=10)
        frame_point1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point1, text="X1:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_x1 = tk.Entry(frame_point1)
        self.entry_x1.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point1, text="Y1:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_y1 = tk.Entry(frame_point1)
        self.entry_y1.grid(row=1, column=1, padx=5, pady=5)

        frame_point2 = tk.LabelFrame(self.root, text="Точка 2", padx=10, pady=10)
        frame_point2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_point2, text="X2:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_x2 = tk.Entry(frame_point2)
        self.entry_x2.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_point2, text="Y2:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_y2 = tk.Entry(frame_point2)
        self.entry_y2.grid(row=1, column=1, padx=5, pady=5)

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
            x1 = int(self.entry_x1.get())
            y1 = int(self.entry_y1.get())
            x2 = int(self.entry_x2.get())
            y2 = int(self.entry_y2.get())
            self.controller.run_output_window((x1,y1), (x2,y2), self.debug_mode)
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