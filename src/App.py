from src.controller.app_controller import MainController

class App:
    def __init__(self):
        app = MainController()
        app.run_app()