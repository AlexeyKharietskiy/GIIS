import tkinter as tk
from tkinter import ttk, messagebox
from view.InputWindows.InputWindow import InputWindow


class InputHermiteWindow(InputWindow):
    def __init__(self, daddy_window, controller, dot):
        super().__init__(daddy_window, controller)
        self.dx = None
        self.dy = None
        self.x = dot[0]
        self.y = dot[1]
        self.bind("<Return>", lambda event: self.return_data)
        self.bind("<Escape>", lambda event: self.destroy)
        self.geometry("320x100")
        self.center_window()

        tk.Label(self, text="Введите производную по x:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.dx_entry = ttk.Entry(self)
        self.dx_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self, text="Введите производную по y:", bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.dy_entry = ttk.Entry(self)
        self.dy_entry.grid(row=1, column=1, padx=10, pady=5)

        ok_button = ttk.Button(self, text="OK", command=self.return_data, style="TButton")
        ok_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        cancel_button = ttk.Button(self, text="Cancel", command=self.destroy, style="TButton")
        cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.bind('<Return>', self.return_data)
        self.bind('<Escape>', self.del_window)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def return_data(self, event=None):
        try:
            self.dx = float(self.dx_entry.get())
            self.dy = float(self.dy_entry.get())
            self.destroy()
            self.controller.get_dot_info((self.x, self.y, self.dx, self.dy))
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения для производных")

    def del_window(self, event=None):
        self.destroy()

    def run(self):
        self.wait_window()
