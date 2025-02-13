import tkinter as tk
from tkinter import Menu
from controller.MainController import MainController


class MainWindow:
    def __init__(self):
        self.controller = MainController()
        self.root = tk.Tk()
        self.algorithm = tk.StringVar()
        self.root.resizable(False,False)
        self.root.title("Графический редактор")
        self.root.geometry("800x600")
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Меню для отрезков
        self.line_menu = Menu(self.menu_bar, tearoff=0)
        self.line_menu.add_radiobutton(label="Алгоритм ЦДА", variable=self.algorithm, command=self.input_line_data)
        self.line_menu.add_radiobutton(label="Алгоритм Брезенхема", variable=self.algorithm, command=self.input_line_data)
        self.line_menu.add_radiobutton(label="Алгоритм Ву", variable=self.algorithm, command=self.input_line_data)
        self.menu_bar.add_cascade(label="Отрезки", menu=self.line_menu, command=self.pr_men)

        # Меню для линий второго порядка
        self.second_order_line_menu = Menu(self.menu_bar, tearoff=0)
        self.second_order_line_menu.add_radiobutton(label="Окружность",variable=self.algorithm, command=self.input_circle_data)
        self.second_order_line_menu.add_radiobutton(label="Эллипс", variable=self.algorithm,command=self.input_line_data)
        self.second_order_line_menu.add_radiobutton(label="Гипербола", variable=self.algorithm,command=self.input_line_data)
        self.second_order_line_menu.add_radiobutton(label="Парабола", variable=self.algorithm ,command=self.input_line_data)
        self.menu_bar.add_cascade(label="Линии второго порядка", menu=self.second_order_line_menu)

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

    def input_line_data(self):
        self.controller.run_line_input_window(self.algorithm.get())

    def input_circle_data(self):
        self.controller.run_circle_input_window(self.algorithm.get())

    def input_ellipse_data(self):
        self.controller.run_line_input_window(self.algorithm.get())

    def input_hyperbola_data(self):
        self.controller.run_line_input_window(self.algorithm.get())

    def input_parabola_data(self):
        self.controller.run_line_input_window(self.algorithm.get())

    def pr_men(self):
        print('aa')