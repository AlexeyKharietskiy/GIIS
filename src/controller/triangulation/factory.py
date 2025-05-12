from view.triangulation.DelaunayView import DelaunayApp
from view.triangulation.VoronoiView import VoronoiApp


class TriangulationFactory:
    def __init__(self):
        self._algorithm_shape_dict = {
            "Делоне": DelaunayApp, 
            "Вороной": VoronoiApp
        }
        
    def create_window(self, daddy_window, controller, algorithm):
        return self._algorithm_shape_dict[algorithm](daddy_window, controller)