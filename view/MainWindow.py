import tkinter as tk
from tkinter import Menu
from controller.MainController import MainController


class MainWindow:
    def __init__(self):
        self.controller = MainController()
        self.root = tk.Tk()
        self.root.resizable(False,False)
        self.root.title("Графический редактор")
        self.root.geometry("800x600")
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Меню для отрезков
        self.segments_menu = Menu(self.menu_bar, tearoff=0)
        self.segments_menu.add_command(label="Алгоритм ЦДА", command=self.draw_with_dda)
        self.segments_menu.add_command(label="Алгоритм Брезенхема", command=self.draw_with_bresenham)
        self.segments_menu.add_command(label="Алгоритм Ву", command=self.draw_with_wu)
        self.menu_bar.add_cascade(label="Отрезки", menu=self.segments_menu)

        # Холст для рисования
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Приветственное сообщение
        self.canvas.create_text(
            400,
            300,
            text="Добро пожаловать в графический редактор!\nВыберите тип фигуры и алгоритм для построения.",
            fill="black",
            font=("Arial", 14),
            justify="center"
        )

    def run(self):
        self.root.lift()  # Поднимает окно на передний план
        self.root.attributes('-topmost', True)  # Делает окно всегда поверх других
        self.root.after_idle(self.root.attributes, '-topmost', False)  # Сбрасывает после отображения
        self.root.mainloop()

    def draw_with_dda(self):
        self.controller.run_line_input_window('DDAAlgorithm')

    def draw_with_bresenham(self):
        self.controller.run_line_input_window('BresenhamAlgorithm')

    def draw_with_wu(self):
        self.controller.run_line_input_window('WuAlgorithm')
