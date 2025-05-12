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
        self.volume_refactoring_menu = Menu(self.menu_bar, tearoff=0)
        self.polygon_menu = Menu(self.menu_bar, tearoff=0)
        
        self._paste_line_menu()
        self._paste_second_order_line_menu()
        self._paste_curve_menu()
        self._paste_volume_refactoring_menu()
        self._paste_polygon_menu()

        self.label = tk.Label(
            self, 
            text="Добро пожаловать в графический редактор!"
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

    def _paste_curve_menu(self):
        self.curve_menu.add_command(
            label="Формы Эрмита",
            command=lambda:self.controller.run_shape_window(
                "Кривые",
                "Формы Эрмита"
                )
            )
        self.curve_menu.add_command(
            label="Формы Безье",
            command=lambda:self.controller.run_shape_window(
                "Кривые", 
                "Формы Безье"
                )
            )
        self.curve_menu.add_command(
            label="В-сплайн",
            command=lambda:self.controller.run_shape_window(
                "Кривые",
                "В-сплайн"
                )
            )
        self.menu_bar.add_cascade(label="Кривые", menu=self.curve_menu)

    def _paste_line_menu(self):
        self.line_menu.add_command(
            label="Алгоритм ЦДА",
            command=lambda:self.controller.run_shape_window(
                "Отрезки", 
                "Алгоритм ЦДА"
                )
            )
        self.line_menu.add_command(
            label="Алгоритм Брезенхема",
            command=lambda:self.controller.run_shape_window(
                "Отрезки", 
                "Алгоритм Брезенхема"
                )
            )
        self.line_menu.add_command(
            label="Алгоритм Ву",
            command=lambda:self.controller.run_shape_window(
                "Отрезки", 
                "Алгоритм Ву"
                )
            )
        self.menu_bar.add_cascade(label="Отрезки", menu=self.line_menu)

    def _paste_second_order_line_menu(self):
        self.second_order_line_menu.add_command(
            label="Окружность",
            command=lambda:self.controller.run_shape_window(
                "Линии второго порядка", 
                "Окружность"
                )
            )
        self.second_order_line_menu.add_command(
            label="Эллипс",
            command=lambda:self.controller.run_shape_window(
                "Линии второго порядка", 
                "Эллипс"
                )
            )
        self.second_order_line_menu.add_command(
            label="Гипербола",
            command=lambda:self.controller.run_shape_window(
                "Линии второго порядка", 
                "Гипербола"
                )
            )
        self.second_order_line_menu.add_command(
            label="Парабола",
            command=lambda:self.controller.run_shape_window(
                "Линии второго порядка",
                "Парабола"
                )
            )
        self.menu_bar.add_cascade(label="Линии второго порядка", menu=self.second_order_line_menu)
        
    def _paste_volume_refactoring_menu(self):
        self.volume_refactoring_menu.add_command(
            label='Файл с точками',
            command=lambda:self.controller.run_shape_window(
                'Геометрические преобразования',
                'Куб'
            )
        )
        self.menu_bar.add_cascade(
            label='Геометрические преобразования', 
            menu=self.volume_refactoring_menu,
        )
        
    def _paste_polygon_menu(self):
        self.polygon_menu.add_command(
            label='Холст',
            command=lambda:self.controller.run_shape_window(
                'Полигон',
                'Построение'
            )
        )
        self.polygon_menu.add_command(
            label='Заполнение',
            command=lambda:self.controller.run_shape_window(
                'Полигон',
                'Заполнение'
            )
        )
        self.menu_bar.add_cascade(
            label='Полигон', 
            menu=self.polygon_menu,
        )


