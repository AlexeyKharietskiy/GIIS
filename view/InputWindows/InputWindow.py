from view.Window import Window

class InputWindow(Window):
    def __init__(self, daddy_window, controller, *kwargs):
        super().__init__(daddy_window, controller)
        self.title("Ввод нужных данных")

    def return_data(self):
        pass
