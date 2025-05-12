import tkinter as tk

from src.model.algorithms.triangulation.DelaunayAlgorithm import DelaunayAlgorithm
from view.window import Window


class DelaunayApp(Window):
    def __init__(self, root, cont):
        super().__init__(root, cont)
        self.title("Delaunay Triangulation")
        self.geometry("820x700")

        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.points = []
        self.mode = None
        self.sweep_y = 300

        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Button-3>", self.clear_points)

        self.button_frame = tk.Frame(self)
        self.calc_button = tk.Button(self.button_frame, text="Calculate", command=self.set_delaunay_mode)
        self.run()
        self.draw()

    def pack_all(self):
        self.canvas.pack(padx=10, pady=10)
        self.button_frame.pack(fill=tk.X, padx=10, pady=5)
        self.calc_button.pack(side=tk.LEFT, padx=5)

    def set_delaunay_mode(self):
        self.mode = "delaunay"
        self.draw()

    def add_point(self, event):
        self.points.append((event.x, event.y))
        self.draw()

    def clear_points(self, event):
        self.points = []
        self.mode = None
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for x, y in self.points:
            self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")

        if self.mode == "delaunay" and len(self.points) >= 3:
            try:
                delaunay = DelaunayAlgorithm(self.points)
                delaunay_edges = delaunay.run()
                for (p1, p2) in delaunay_edges:
                    self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], width=2, fill="green")
            except Exception as e:
                print(f"Error in Delaunay triangulation: {e}")