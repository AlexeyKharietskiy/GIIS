from src.model.Shapes.VolumeFigures.cube import Cube
from src.factories.Factory import Factory
from src.model.Shapes.Shape import Shape
from view.geom_refactor.view import GeomRefactorView


class VolumeRefactoringFactory(Factory):
    def __init__(self):
        self._algorithm_shape_dict = {
            'Куб': (GeomRefactorView, Cube),
        }

    def create_shape(self, algorithm, *args)->Shape:
        return self._algorithm_shape_dict[algorithm][1](*args)
    
    def create_window(self, daddy_window, controller, algorithm):
         return self._algorithm_shape_dict[algorithm][0](daddy_window, controller)
