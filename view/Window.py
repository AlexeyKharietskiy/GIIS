import tkinter
from tkinter.font import Font


class Window(tkinter.Toplevel):
    def __init__(self, daddy_window, controller, *args):
        super().__init__(daddy_window)
        self.controller = controller
        self.configure(bg="#f5f5f5")
        self.font = Font(family="Arial", size=10)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"+{x}+{y}")

    def exist(self):
        return self.winfo_exists()

    def return_data(self):
        pass

    def pack_all(self):
        pass

    def run(self):
        self.pack_all()
        self.center_window()
        self.lift()
        self.mainloop()