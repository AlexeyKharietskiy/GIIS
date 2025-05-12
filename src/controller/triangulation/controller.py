

from src.controller.triangulation.factory import TriangulationFactory

class TriangulationController:
    def __init__(self, daddy_window, algorithm):
        self.daddy_window = daddy_window
        self.algorithm = algorithm
        self.window = TriangulationFactory().create_window(daddy_window, self, algorithm)
        
    def change_algorithm(self, algorithm):
        if not self.check_window(self.window):
            self.algorithm = algorithm
            self.window = TriangulationFactory().create_window(self.daddy_window, self, algorithm)

    @staticmethod        
    def check_window(window):
        if window is not None:
            try:
                if window.exist():
                    window.destroy()
            except Exception:
                pass
        

    