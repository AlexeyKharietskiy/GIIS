from view.Window import Window
import tkinter as tk
from tkinter import ttk
from logger import logger


class CanvasWindow(Window):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.title("Построение кривых")
        self.state("zoomed")
        self.main_frame = ttk.Frame(self)
        self.control_frame = ttk.Frame(self.main_frame)

        self.btn_clear = ttk.Button(
            self.control_frame,
            text="Очистить",
            command=self.clear_canvas
        )
        self.seamless_var = tk.BooleanVar()
        self.seamless_check = ttk.Checkbutton(
            self.control_frame,
            text="Режим состыковки",
            variable=self.seamless_var,
            command=self.controller.toggle_seamless_mode
        )
        self.canvas = tk.Canvas(
            self.main_frame,
            bg="white",
        )
        self.bind("<Escape>", self.clear_canvas)
        self.bind("<Return>", self.draw_curve)
        self.bind("<KeyPress-space>", self.controller.toggle_seamless_mode)

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.tag_bind("dot", "<Enter>", self.on_enter_dot)
        self.canvas.tag_bind("dot", "<Leave>", self.on_exit_dot)
        self.canvas.tag_bind("dot", "<Button-3>", self.on_dot_click)

    def on_dot_click(self, event):
        dot_id = self.canvas.find_withtag(tk.CURRENT)[0]
        dot_coord = self.canvas.coords(dot_id)
        x, y = dot_coord[0]+5, dot_coord[1]+5
        self.controller.change_point(x, y)

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        self.controller.set_model_info(x, y)

    def draw_curve(self, event=None):
        self.canvas.delete("curve")
        reference_dot_list, dot_list = self.controller.get_model_info()

        for dot in reference_dot_list:
            x, y = dot[0], dot[1]
            self.canvas.create_oval(x+5, y+5, x-5, y-5, fill='#4682B4', tags='dot')

        for dot in dot_list:
            x, y = dot[0], dot[1]
            self.canvas.create_rectangle(x+1, y+1, x-1, y-1, tags="curve", fill="black", width=2)

        self.canvas.tag_raise("dot")

    def clear_canvas(self, event=None):
        self.controller.clear_canvas()
        self.canvas.delete("all")

    def on_enter_dot(self, event):
        item_id = self.canvas.find_withtag(tk.CURRENT)[0]
        self.canvas.itemconfig(item_id, fill="#90EE90")

    def on_exit_dot(self, event):
        item_id = self.canvas.find_withtag(tk.CURRENT)[0]
        self.canvas.itemconfig(item_id, fill="#4682B4")

    def pack_all(self):
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.control_frame.pack(fill=tk.X)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        self.seamless_check.pack(side=tk.RIGHT, padx=5)
        self.canvas.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
