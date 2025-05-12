from src.controller.factory import Factory
from view.polygon.filling import PolygonFiller
from view.polygon.polygon_drawer import DrawingInterface

class PolygonWinFactory:
    def __init__(self):
        self._algorithm_shape_dict = {
            'Построение': DrawingInterface,
            'Заполнение': PolygonFiller,
        }

    def create_window(self, daddy_window, controller, algorithm):
        return self._algorithm_shape_dict[algorithm](daddy_window, controller)
    
