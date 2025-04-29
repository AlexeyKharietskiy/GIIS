from view.Window import Window
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GeomRefactorView(Window):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.title("Визуализация куба")
        self.geometry("1900x1000")
        
        self.fig = None
        self.ax = None
        self.canvas = None
        self.grid_limits = None
        
        self.plot_frame = tk.Frame(self)
        self.plot_frame.pack(fill=tk.BOTH, expand=True)
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть файл", command=self.open_file)
        
        self.bind("<KeyPress>", self.handle_keypress)
        
        
    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Выберите файл TXT",
            filetypes=[
                ("Текстовые файлы", "*.txt"),
                ],
            parent=self,
        )
        if file_path:
            self.controller.set_model_info(file_path=file_path)
        else:
            messagebox.showinfo("Информация", "Файл не выбран")
        self.visualize()
        
    def calculate_grid_limits(self):
        """
        Вычисляет пределы осей для сетки, которая в 3 раза больше размеров куба.
        """
        edges = self.controller.get_model_info()[1]
        if not edges:
            return [-10, 10], [-10, 10], [-10, 10]  # Значения по умолчанию, если куб пустой

        # Собираем все координаты точек
        x_coords, y_coords, z_coords = [], [], []
        for edge in edges:
            point1, point2 = edge
            x1, y1, z1 = [*point1]
            x2, y2, z2 = [*point2]
            x_coords.extend([x1, x2])
            y_coords.extend([y1, y2])
            z_coords.extend([z1, z2])

        # Находим минимальные и максимальные значения
        x_min, x_max = min(x_coords), max(x_coords)
        y_min, y_max = min(y_coords), max(y_coords)
        z_min, z_max = min(z_coords), max(z_coords)

        # Вычисляем размеры куба
        x_range = x_max - x_min
        y_range = y_max - y_min
        z_range = z_max - z_min

        # Увеличиваем размеры в 3 раза
        grid_factor = 3
        x_range *= grid_factor
        y_range *= grid_factor
        z_range *= grid_factor

        # Центрируем сетку вокруг центра куба
        x_center = (x_max + x_min) / 2
        y_center = (y_max + y_min) / 2
        z_center = (z_max + z_min) / 2

        x_limits = [x_center - x_range / 2, x_center + x_range / 2]
        y_limits = [y_center - y_range / 2, y_center + y_range / 2]
        z_limits = [z_center - z_range / 2, z_center + z_range / 2]

        return x_limits, y_limits, z_limits
    def visualize(self):

        if self.fig is None:
            self.fig = plt.Figure(figsize=(100, 100))
            self.ax = self.fig.add_subplot(111, projection='3d')
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            self.grid_limits =  self.calculate_grid_limits()
        self.update()
        
    def update(self):
        self.plot_cube(self.ax, color='black', label='Куб')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.legend()
        self.ax.set_title('Фигура')
        self.ax.set_box_aspect([1, 1, 1])
        
        x_limits, y_limits, z_limits = self.grid_limits
        self.ax.set_xlim(x_limits)
        self.ax.set_ylim(y_limits)
        self.ax.set_zlim(z_limits)
        
        self.ax.set_axis_off()
        
        self.canvas.draw()

    def handle_keypress(self, event):
        self.controller.set_model_info(event=event.keysym)
        
    def plot_cube(self, ax, color='b', label=None):
        ax.clear()
        edges = self.controller.get_model_info()[1]
        for i, edge in enumerate(edges):
            point1, point2 = edge
            x1, y1, z1 = [*point1]
            x2, y2, z2 = [*point2]
            ax.plot([x1, x2], [y1, y2], [z1, z2], color=color, label=label if i == 0 else None)
