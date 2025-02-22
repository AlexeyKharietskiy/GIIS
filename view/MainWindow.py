import tkinter as tk
from tkinter import Menu
from tkinter.font import Font


class MainWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.configure(bg="#f5f5f5")
        self.font = Font(family="Arial", size=10)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.algorithm = tk.StringVar()
        self.title("Графический редактор")
        self.geometry("800x600")
        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)

        self.line_menu = Menu(self.menu_bar, tearoff=0)
        self.second_order_line_menu = Menu(self.menu_bar, tearoff=0)
        self.curve_menu = Menu(self.menu_bar, tearoff=0)
        self.__paste_line_menu()
        self.__paste_second_order_line_menu()
        self.__paste_curve_menu()

        self.label = tk.Label(self, text="Добро пожаловать в графический редактор!"
                                         "\nВыберите тип фигуры и алгоритм для построения.",
                              justify='center',
                              font=("Arial", 20),
                              bg="#f5f5f5"
                              )
        self.label.pack(pady=220)

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"+{x}+{y}")

    def exist(self):
        return self.winfo_exists()

    def run(self):
        self.center_window()
        self.mainloop()

    def __paste_curve_menu(self):
        self.curve_menu.add_radiobutton(label="Формы Эрмита",variable=self.algorithm,
                                        command=lambda:self.controller.run_curve_input_window(self.algorithm.get()))
        self.curve_menu.add_radiobutton(label="Формы Безье", variable=self.algorithm,
                                        command=lambda:self.controller.run_curve_input_window(self.algorithm.get()))
        self.curve_menu.add_radiobutton(label="В-сплайн", variable=self.algorithm,
                                        command=lambda:self.controller.run_curve_input_window(self.algorithm.get()))
        self.menu_bar.add_cascade(label="Кривые", menu=self.curve_menu)

    def __paste_line_menu(self):
        self.line_menu.add_radiobutton(label="Алгоритм ЦДА", variable=self.algorithm,
                                       command=lambda:self.controller.run_line_input_window(self.algorithm.get()))
        self.line_menu.add_radiobutton(label="Алгоритм Брезенхема", variable=self.algorithm,
                                       command=lambda:self.controller.run_line_input_window(self.algorithm.get()))
        self.line_menu.add_radiobutton(label="Алгоритм Ву", variable=self.algorithm,
                                       command=lambda:self.controller.run_line_input_window(self.algorithm.get()))
        self.menu_bar.add_cascade(label="Отрезки", menu=self.line_menu)

    def __paste_second_order_line_menu(self):
        self.second_order_line_menu.add_radiobutton(label="Окружность", variable=self.algorithm,
                                                    command=lambda:self.controller.run_circle_input_window(self.algorithm.get()))
        self.second_order_line_menu.add_radiobutton(label="Эллипс", variable=self.algorithm,
                                                    command=lambda:self.controller.run_ellipse_input_window(self.algorithm.get()))
        self.second_order_line_menu.add_radiobutton(label="Гипербола", variable=self.algorithm,
                                                    command=lambda:self.controller.run_hyperbola_input_window(self.algorithm.get()))
        self.second_order_line_menu.add_radiobutton(label="Парабола", variable=self.algorithm,
                                                    command=lambda:self.controller.run_parabola_input_window(self.algorithm.get()))
        self.menu_bar.add_cascade(label="Линии второго порядка", menu=self.second_order_line_menu)

    def input_line_data(self):
        self.controller.run_line_input_window(self.algorithm.get())

    def input_circle_data(self):
        self.controller.run_circle_input_window(self.algorithm.get())

    def input_ellipse_data(self):
        self.controller.run_ellipse_input_window(self.algorithm.get())

    def input_hyperbola_data(self):
        self.controller.run_hyperbola_input_window(self.algorithm.get())

    def input_parabola_data(self):
        self.controller.run_parabola_input_window(self.algorithm.get())

    def input_curve_data(self):
        self.controller.run_curve_input_window(self.algorithm.get())
