import tkinter as tk
from tkinter import ttk, messagebox


class InputDerivativeWindow(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.dx = None
        self.dy = None

        self.geometry("300x150")
        self.resizable(False, False)
        self.center_window()
        self.configure(bg="#f5f5f5")

        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, relief="flat", background="#4CAF50", foreground="white", font=("Arial", 10))
        self.style.map("TButton", background=[("active", "#45a049")])

        self.style.configure("TLabel", background="#f5f5f5", font=("Arial", 10))
        self.style.configure("TEntry", font=("Arial", 10))

        tk.Label(self, text="Введите производную по x:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.dx_entry = ttk.Entry(self)
        self.dx_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Введите производную по y:", bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.dy_entry = ttk.Entry(self)
        self.dy_entry.grid(row=1, column=1, padx=10, pady=5)

        ok_button = ttk.Button(self, text="OK", command=self.on_ok, style="TButton")
        ok_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        cancel_button = ttk.Button(self, text="Cancel", command=self.on_cancel, style="TButton")
        cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.dx_entry.focus_set()
        self.bind("<Return>", lambda event: self.on_ok())
        self.bind("<Escape>", lambda event: self.on_cancel())

        self.protocol("WM_DELETE_WINDOW", self.on_cancel)

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"+{x}+{y}")

    def on_ok(self):
        try:
            self.dx = float(self.dx_entry.get())
            self.dy = float(self.dy_entry.get())
            self.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения для производных")

    def on_cancel(self):
        self.destroy()