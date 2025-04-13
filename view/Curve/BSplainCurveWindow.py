from tkinter import ttk

from  view.Curve.CurveWindow import CurveWindow
import tkinter as tk


class BSplainCurveWindow(CurveWindow):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)
        self.input_window = None
        self.line_list = []
        self.bind("<Escape>", self.clear_canvas)
        self.bind("<KeyPress-space>", self.controller.toggle_seamless_mode)
        self.bind("<Return>", self.draw_curve)
        self.btn_draw = ttk.Button(
            self.control_frame,
            text="Построить сплайн",
            command=self.draw_curve
        )
        self.btn_draw.pack(side=tk.LEFT, padx=5)
        self.canvas.bind("<Button-1>", self.add_dot)
        self.canvas.tag_bind("dot", "<Enter>", self.on_enter_dot)
        self.canvas.tag_bind("dot", "<Leave>", self.on_exit_dot)
        self.canvas.tag_bind("dot", "<Button-3>", self.adjust_dot)

    def adjust_dot(self, event):
        dot_id = self.canvas.find_withtag(tk.CURRENT)[0]
        dot_coord = self.canvas.coords(dot_id)
        x, y = dot_coord[0] + 5, dot_coord[1] + 5
        self.controller.toggle_adjust_mode()
        self.controller.set_model_info((x,y))
        self.canvas.delete(dot_id)
        self.controller.toggle_adjust_mode()
        
    def draw_curve(self, event=None):
        self.canvas.delete("curve")
        reference_dot_list, dot_list = self.controller.get_model_info()
        if dot_list:
            for dot in dot_list:
                self.canvas.create_oval(dot[0] + 2, dot[1] + 2, dot[0] - 2, dot[1] - 2, fill='black', width=3, tags='curve')
        self.canvas.tag_raise("dot")
            
    def add_dot(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x + 5, y + 5, x - 5, y - 5, fill='#4682B4', tags='dot')
        self.controller.set_model_info((x,y))

    def on_enter_dot(self, event):
        item_id = self.canvas.find_withtag(tk.CURRENT)[0]
        self.canvas.itemconfig(item_id, fill="#90EE90")

    def on_exit_dot(self, event):
        item_id = self.canvas.find_withtag(tk.CURRENT)[0]
        self.canvas.itemconfig(item_id, fill="#4682B4")
