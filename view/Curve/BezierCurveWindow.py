from  view.Curve.CurveWindow import CurveWindow
import tkinter as tk


class BezierCurveWindow(CurveWindow):
    def __init__(self, daddy_window, controller):
        super().__init__(daddy_window, controller)

        self.last_start_dline_id = None
        self.start_dline_dot = None
        self.end_dline_dot = None
        self.dline_dict = {}
        self.temp_line = None
        self.adjust_mode = False

        self.pack_all()
        self.bind("<Escape>", self._cancel_dline)
        self.canvas.bind("<Motion>", self._on_mouse_move)
        self.bind("<KeyPress-space>", self.controller.toggle_seamless_mode)

        self.canvas.bind("<Button-1>", self.add_dot)
        self.canvas.tag_bind("dot", "<Enter>", self.on_enter_dot)
        self.canvas.tag_bind("dot", "<Leave>", self.on_exit_dot)
        self.canvas.tag_bind("dot", "<Button-3>", self.adjust_dot)


    def adjust_dot(self, event):
        self.adjust_mode = True
        self.controller.toggle_adjust_mode(self.adjust_mode)
        dot_id = self.canvas.find_withtag(tk.CURRENT)[0]
        dot_coord = self.canvas.coords(dot_id)
        x, y = dot_coord[0] + 5, dot_coord[1] + 5
        self.start_dline_dot = (x, y)
        for line_key in self.dline_dict:
            if self.dline_dict[line_key][0] == (x, y):
                del self.dline_dict[line_key]
                self.canvas.delete(line_key)
                break

    def add_dot(self, event):
        x, y = event.x, event.y
        if self.start_dline_dot is None:
            self.start_dline_dot = (x, y)
            self.adjust_mode = False
            self.controller.toggle_adjust_mode(self.adjust_mode)
            self.last_start_dline_id = self.canvas.create_oval(x + 5, y + 5, x - 5, y - 5,
                                                               fill='#4682B4', tags='dot')
        else:
            self.end_dline_dot = (x, y)
            self.dline_dict[self.temp_line] = ((self.start_dline_dot[0], self.start_dline_dot[1]),
                                               (self.end_dline_dot[0], self.end_dline_dot[1]))
            self.canvas.tag_raise("dot")
            self.controller.set_model_info((*self.start_dline_dot, *self.end_dline_dot))
            self.start_dline_dot = None
            self.end_dline_dot = None
            self.temp_line = None

    def _cancel_dline(self, event=None):
        if not self.adjust_mode:
            if self.start_dline_dot is not None:
                self.start_dline_dot = None
                self.canvas.delete(self.last_start_dline_id)
                if self.temp_line:
                    self.canvas.delete(self.temp_line)
                    self.temp_line = None


    def _on_mouse_move(self, event):
        if self.start_dline_dot is not None:
            x, y = event.x, event.y
            if self.temp_line:
                self.canvas.coords(self.temp_line, self.start_dline_dot[0], self.start_dline_dot[1], x, y)
            else:
                self.temp_line = self.canvas.create_line(
                    self.start_dline_dot[0], self.start_dline_dot[1],
                    x, y,
                    dash=(4, 2), fill="black", arrow=tk.LAST
                )

    def on_enter_dot(self, event):
        item_id = self.canvas.find_withtag(tk.CURRENT)[0]
        self.canvas.itemconfig(item_id, fill="#90EE90")

    def on_exit_dot(self, event):
        item_id = self.canvas.find_withtag(tk.CURRENT)[0]
        self.canvas.itemconfig(item_id, fill="#4682B4")


