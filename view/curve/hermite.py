from view.curve.curve_canvas import CurveWindow
from view.curve.hermite_input import InputHermiteWindow
import tkinter as tk
from tkinter import ttk
class HermiteCurveWindow(CurveWindow):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.input_window = None
        self.line_list = []
        self.seamless_var = tk.BooleanVar()
        self.seamless_check = ttk.Checkbutton(
            self.control_frame,
            text="Режим состыковки",
            variable=self.seamless_var,
            command=self.controller.toggle_seamless_mode
        )
        self.seamless_check.pack(side=tk.RIGHT, padx=5)
        self.bind("<Escape>", self.clear_canvas)
        self.bind("<KeyPress-space>", self.controller.toggle_seamless_mode)

        self.canvas.bind("<Button-1>", self.add_dot)
        self.canvas.tag_bind("dot", "<Enter>", self.on_enter_dot)
        self.canvas.tag_bind("dot", "<Leave>", self.on_exit_dot)
        self.canvas.tag_bind("dot", "<Button-3>", self.adjust_dot)
        
        

    def adjust_dot(self, event):
        dot_id = self.canvas.find_withtag(tk.CURRENT)[0]
        dot_coord = self.canvas.coords(dot_id)
        x, y = dot_coord[0] + 5, dot_coord[1] + 5
        self.controller.toggle_adjust_mode()
        self.open_input_window((x,y))
        self.controller.toggle_adjust_mode()

    def open_input_window(self, dot):
        self.controller.check_window(self.input_window)
        self.input_window = InputHermiteWindow(self, self.controller, dot)
        self.input_window.run()

    def add_dot(self, event):
        x, y = event.x, event.y
        self.open_input_window((x, y))
        if self.controller.check_existence((x,y)):
            self.canvas.create_oval(x + 5, y + 5, x - 5, y - 5, fill='#4682B4', tags='dot')


    def on_enter_dot(self, event):
        item_id = self.canvas.find_withtag(tk.CURRENT)[0]
        self.canvas.itemconfig(item_id, fill="#90EE90")

    def on_exit_dot(self, event):
        item_id = self.canvas.find_withtag(tk.CURRENT)[0]
        self.canvas.itemconfig(item_id, fill="#4682B4")
