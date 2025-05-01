import tkinter as tk
from tkinter import ttk

from view.window import Window

class DrawingInterface(Window):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.title("Polygon Drawing Interface")
        self.geometry("1000x700")
        
        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.control_frame = ttk.Frame(self)
        self.control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
        
        self.draw_mode = tk.StringVar(value="point")
        ttk.Label(self.control_frame, text="Режим рисования:").pack(anchor="w")
        ttk.Radiobutton(
            self.control_frame, 
            text="Точка", 
            value="point", 
            variable=self.draw_mode, 
            command=self.on_mode_change
            ).pack(anchor="w")
        ttk.Radiobutton(
            self.control_frame, 
            text="Отрезок", 
            value="segment", 
            variable=self.draw_mode, 
            command=self.on_mode_change
            ).pack(anchor="w")
        ttk.Radiobutton(
            self.control_frame, 
            text="Полигон", 
            value="polygon", 
            variable=self.draw_mode, 
            command=self.on_mode_change
            ).pack(anchor="w")
        
        self.algorithm_label = ttk.Label(self.control_frame, text="Алгоритм полигона:")
        self.algorithm_label.pack(anchor="w", pady=(10, 0))
        self.algorithm = tk.StringVar(value="Graham")
        self.algorithm_menu = ttk.Combobox(
            self.control_frame, 
            textvariable=self.algorithm, 
            values=["Graham", "Jarvis"], 
            state="disabled"
            )
        self.algorithm_menu.pack(anchor="w")
        
        self.build_polygon_button = ttk.Button(
            self.control_frame, 
            text="Построить полигон", 
            command=self.on_build_polygon_button,
            state="disabled"
            )
        self.build_polygon_button.pack(anchor="w", pady=(10, 0))
        
        self.points = []
        self.segments = []
        self.polygons = []
        self.intersections = []
        self.current_shape = []
        self.selected_shape = None
        
        self.tooltip = None
        
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<Motion>", self.on_canvas_motion)
        
    def on_mode_change(self):
        """Вызывается при смене режима рисования."""
        if self.draw_mode.get() == "polygon":
            self.algorithm_menu["state"] = "normal"
            self.build_polygon_button["state"] = "normal"
        else:
            self.algorithm_menu["state"] = "disabled"
            self.build_polygon_button["state"] = "disabled"
        self.current_shape = []
        self.redraw()
    
    def on_canvas_click(self, event):
        """Вызывается при клике на канвас."""
        x, y = event.x, event.y
        self.add_shape(x, y)
    
    def on_canvas_motion(self, event):
        """Вызывается при движении мыши."""
        x, y = event.x, event.y
        self.update_tooltip(x, y)
    
    def on_build_polygon_button(self):
        """Вызывается при нажатии на кнопку построения полигона."""
        if self.draw_mode.get() == "polygon" and len(self.current_shape) >= 3:
            polygon = self.controller.add_polygon(self.current_shape[:], self.algorithm.get())
            self.polygons.append([(p.x, p.y) for p in polygon.points])
            self.current_shape = []
            self.redraw()
    
    def add_shape(self, x, y):
        """Добавляет новую фигуру в зависимости от режима."""
        mode = self.draw_mode.get()
        if mode == "point":
            self.points.append((x, y))
            self.controller.add_dot(x, y)
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="blue", tags="point")
        elif mode == "segment":
            self.current_shape.append((x, y))
            if len(self.current_shape) == 2:
                self.segments.append(self.current_shape[:])
                intersections = self.controller.add_line(*self.current_shape[:])
                for p in intersections:
                    self.intersections.append((p.x, p.y))
                self.canvas.create_line(
                    self.current_shape[0][0], 
                    self.current_shape[0][1],
                    self.current_shape[1][0],
                    self.current_shape[1][1],
                    fill="red", 
                    tags="segment",
                    width=2
                    )
                self.current_shape = []
                self.redraw()
        elif mode == "polygon":
            self.current_shape.append((x, y))
            # self.canvas.create_line(
            #     self.current_shape[-2][0], 
            #     self.current_shape[-2][1],
            #     self.current_shape[-1][0], 
            #     self.current_shape[-1][1],
            #     fill="black", 
            #     tags="temp_line"
            #     )
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="black", tags="point")

    def update_tooltip(self, x, y):
        """Обновляет подсказку при наведении на точку."""
        if self.tooltip:
            self.canvas.delete(self.tooltip)
            self.tooltip = None
        for point in self.points:
            if ((point[0] - x) ** 2 + (point[1] - y) ** 2) ** 0.5 < 5:
                is_inside, polygon = self.controller.is_point_inside(point)
                text = f"({point[0]:.0f}, {point[1]:.0f})"
                if is_inside:
                    text += f"\nВнутри полигона"
                else:
                    text += f"\nСнаружи"
                self.tooltip = self.canvas.create_text(
                    x+15, 
                    y-10,
                    text=text, 
                    anchor="nw", 
                    tags="tooltip", 
                    fill="black"
                    )
                break
    
    def redraw(self):
        """Перерисовывает все фигуры, выделяя выбранную."""
        self.canvas.delete("point", "segment", "polygon", "temp_line", "intersection")
        # Точки
        for point in self.points:
            color = "yellow" if self.selected_shape == ("point", point) else "blue"
            self.canvas.create_oval(
                point[0] - 3, 
                point[1] - 3, 
                point[0] + 3, 
                point[1] + 3, 
                fill=color, 
                tags="point"
                )
        # Отрезки
        for seg in self.segments:
            color = "orange" if self.selected_shape == ("segment", seg) else "red"
            self.canvas.create_line(
                seg[0][0], 
                seg[0][1], 
                seg[1][0], 
                seg[1][1], 
                fill=color, 
                tags="segment",
                width=2
                )
        # Полигоны
        for poly in self.polygons:
            color = "green" if self.selected_shape == ("polygon", poly) else "black"
            for i in range(len(poly)):
                p1, p2 = poly[i], poly[(i + 1) % len(poly)]
                self.canvas.create_line(
                    p1[0],
                    p1[1], 
                    p2[0], 
                    p2[1], 
                    fill=color, 
                    tags="polygon",
                    width=2
                    )
        # Точки пересечения
        for point in self.intersections:
            self.canvas.create_oval(
                point[0] - 3, 
                point[1] - 3, 
                point[0] + 3, 
                point[1] + 3, 
                fill="yellow", 
                tags="intersection"
                )