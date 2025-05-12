import time
import tkinter as tk
from tkinter import ttk
from typing import List, Tuple

from src.model.shapes.dots.dot import Dot
from view.window import Window


class PolygonFiller(Window):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.title("Polygon Filler")
        self.geometry("800x600")

        self.control_frame = ttk.Frame(self)
        self.control_frame.pack(fill=tk.X, padx=10, pady=5)

        build_frame = ttk.Frame(self.control_frame)
        build_frame.pack(side=tk.LEFT, padx=5)
        ttk.Button(build_frame, text="Build Polygon", command=self.controller.on_build_polygon).pack(side=tk.LEFT)
        self.select_seed_button = ttk.Button(build_frame, text="Select Seed", command=self.controller.on_select_seed)
        self.select_seed_button.pack(side=tk.LEFT, padx=5)

        algorithm_frame = ttk.Frame(self.control_frame)
        algorithm_frame.pack(side=tk.LEFT, padx=10)
        ttk.Label(algorithm_frame, text="Algorithm:").pack(anchor=tk.W)
        self.algorithm_var = tk.StringVar(value="ScanlineSortedEdgeList")
        algorithms = [
            ("ScanlineSortedEdgeList", "Scanline (Sorted Edge List)"),
            ("ScanlineActiveEdgeList", "Scanline (Active Edge List)"),
            ("SimpleSeedFill", "Simple Seed Fill"),
            ("ScanlineSeedFill", "Scanline Seed Fill")
        ]
        for value, text in algorithms:
            ttk.Radiobutton(algorithm_frame, text=text, value=value, variable=self.algorithm_var,
                            command=lambda: self.controller.set_algorithm(self.algorithm_var.get())).pack(anchor=tk.W)

        fill_frame = ttk.Frame(self.control_frame)
        fill_frame.pack(side=tk.LEFT, padx=5)
        ttk.Button(fill_frame, text="Fill Polygons", command=self.controller.on_fill_polygons).pack(side=tk.LEFT)
        self.debug_var = tk.BooleanVar()
        ttk.Checkbutton(fill_frame, text="Debug Mode", variable=self.debug_var).pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", lambda event: self.controller.on_canvas_click(event.x, event.y))

    def draw_polygon(self, points: List[Dot]):
        coords = [p.get_coordinate() for p in points]
        coords.append(coords[0])
        self.canvas.create_line(coords, fill="black")

    def draw_seed(self, seed: Dot):
        x, y = seed.get_coordinate()
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="blue")

    def perform_operations(self, operations: List[Tuple], debug: bool):
        if not operations:
            return
        if not debug:
            for op in operations:
                if op[0] == 'line':
                    y, x1, x2 = op[1], op[2], op[3]
                    self.canvas.create_line(x1, y, x2, y, fill="red")
                elif op[0] == 'pixel':
                    x, y = op[1], op[2]
                    self.canvas.create_rectangle(x, y, x, y, outline="", fill="red")
        else:
            total_operations = len(operations)
            start_time = time.time()
            for i, op in enumerate(operations):
                if op[0] == 'line':
                    y, x1, x2 = op[1], op[2], op[3]
                    self.canvas.create_line(x1, y, x2, y, fill="red")
                elif op[0] == 'pixel':
                    x, y = op[1], op[2]
                    self.canvas.create_rectangle(x, y, x, y, outline="", fill="red")
                expected_time = start_time + (i + 1) / total_operations * 5
                current_time = time.time()
                if current_time < expected_time:
                    time.sleep(expected_time - current_time)
                self.canvas.update()