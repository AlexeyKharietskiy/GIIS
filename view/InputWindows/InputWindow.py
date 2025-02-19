import tkinter as tk
from tkinter.font import Font

class InputWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="#f5f5f5")
        self.font = Font(family="Arial", size=10)
        self.root.resizable(False, False)
        self.controller = None

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"+{x}+{y}")

    def run(self):
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()

    def exist(self):
        return self.root.winfo_exists()