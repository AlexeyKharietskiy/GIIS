import tkinter as tk
from tkinter import ttk, messagebox
from view.InputWindows.InputWindow import InputWindow


class InputDerivativeWindow(InputWindow):
    def __init__(self, controller):
        super().__init__(controller)
        self.dx = None
        self.dy = None

        self.root.geometry("300x100")
        self.center_window()

        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, relief="flat", background="#4CAF50", foreground="white", font=("Arial", 10))
        self.style.map("TButton", background=[("active", "#45a049")])

        self.style.configure("TLabel", background="#f5f5f5", font=("Arial", 10))
        self.style.configure("TEntry", font=("Arial", 10))

        tk.Label(self.root, text="Введите производную по x:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.dx_entry = ttk.Entry(self.root)
        self.dx_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Введите производную по y:", bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.dy_entry = ttk.Entry(self.root)
        self.dy_entry.grid(row=1, column=1, padx=10, pady=5)

        ok_button = ttk.Button(self.root, text="OK", command=self.on_ok, style="TButton")
        ok_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        cancel_button = ttk.Button(self.root, text="Cancel", command=self.on_cancel, style="TButton")
        cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.dx_entry.focus_set()
        self.root.bind("<Return>", lambda event: self.on_ok())
        self.root.bind("<Escape>", lambda event: self.on_cancel())

        self.root.protocol("WM_DELETE_WINDOW", self.on_cancel)

    def on_ok(self):
        try:
            self.dx = float(self.dx_entry.get())
            self.dy = float(self.dy_entry.get())
            self.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения для производных")

    def on_cancel(self):
        self.destroy()