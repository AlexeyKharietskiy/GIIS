import tkinter as tk
from tkinter import ttk
from view.InputWindows.InputWindow import InputWindow
from view.InputWindows.Curve.InputDerivativeWindow import InputDerivativeWindow
from controller.Curve.CurveController import CurveController


class CurveInputWindow(InputWindow):
    def __init__(self, algorithm):
        super().__init__()
        self.root.focus_set()
        self.root.title("Создание кривых")
        self.root.bind("<Return>", lambda event: self.show_points())
        self.pack_buttons()
        self.canvas = tk.Canvas(self.root, width=1900, height=1000, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.draw_point)
        self.root.grab_set()

        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, relief="flat", background="#4CAF50", foreground="white",
                             font=("Arial", 10))
        self.style.map("TButton", background=[("active", "#45a049")])

        self.algorithm = algorithm
        self.controller = CurveController(algorithm)
        self.reference_dot_list = []
        self.join_mode = False

        self.center_window()

    def draw_point(self, event):
        x, y = event.x, event.y
        dialog = InputDerivativeWindow(self.root)
        self.root.wait_window(dialog)
        if dialog.dx is not None and dialog.dy is not None:
            self.canvas.create_oval(x-4, y-4, x+4, y+4, fill="black")
            self.controller.add_reference_dot((x, y, dialog.dx, dialog.dy), self.join_mode)

    def show_points(self):
        point_list = self.controller.get_curve_point_list()
        for point in point_list:
            self.canvas.create_rectangle(point[0] - 1, point[1] - 1, point[0] + 1, point[1] + 1, fill="black")


    def adjust_points(self):
        adjust_window = tk.Toplevel(self.root)
        adjust_window.title("Корректировка точек")

        self.listbox = tk.Listbox(adjust_window, width=50, height=20)
        self.listbox.pack(padx=10, pady=10)

        for idx, dot in enumerate(self.controller.get_reference_dot_list()):
            x, y, dx, dy = dot
            self.listbox.insert(tk.END, f"Точка {idx}: ({x}, {y}), производные ({dx}, {dy})")

        def on_select(event):
            selected = self.listbox.curselection()
            if selected:
                index = selected[0]
                dot_list = self.controller.get_reference_dot_list()
                x, y, dx, dy = dot_list[index]
                dialog = InputDerivativeWindow(adjust_window)
                adjust_window.wait_window(dialog)

                if dialog.dx is not None and dialog.dy is not None:
                    self.controller.change_reference_dot((x, y, dialog.dx, dialog.dy))
                    self.redraw_curve()

        self.listbox.bind('<<ListboxSelect>>', on_select)

    def redraw_curve(self):
        self.canvas.delete("all")
        dot_list =  self.controller.get_reference_dot_list()
        for dot in dot_list:
            x, y, dx, dy = dot
            self.canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black")

        self.listbox.delete(0, len(dot_list))
        for idx, dot in enumerate(dot_list):
            x, y, dx, dy = dot
            self.listbox.insert(tk.END, f"Точка {idx}: ({x}, {y}), производные ({dx}, {dy})")

        self.show_points()

    def pack_buttons(self):
        toolbar = ttk.Frame(self.root, style="TFrame")
        toolbar.pack(side=tk.TOP, fill=tk.X, pady=5)
        ok_button = ttk.Button(toolbar, text="Построить кривую", command=self.show_points, style="TButton")
        ok_button.pack(side=tk.RIGHT, padx=10)
        adjust_button = ttk.Button(toolbar, text="Корректировка", command=self.adjust_points, style="TButton")
        adjust_button.pack(side=tk.LEFT, padx=10)
        clear_button = ttk.Button(toolbar, text="Очистить холст", command=self.clear_canvas, style="TButton")
        clear_button.pack(side=tk.LEFT, padx=10)
        join_mode_check = tk.Checkbutton(
            toolbar,
            text="Режим состыковки сегментов",
            command=self.on_join_mode_toggle
        )
        join_mode_check.pack(side=tk.RIGHT)

    def on_join_mode_toggle(self):
        self.join_mode = not self.join_mode

    def clear_canvas(self):
        self.canvas.delete('all')
        self.controller.clear_all()

