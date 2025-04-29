import numpy as np
from src.model.Algorithms.Transformations3d.matrix_factory import MatrixFactory
from src.factories.volume_refactoring import VolumeRefactoringFactory
from src.controller.Controller import Controller


class GeomRefactorController(Controller):
    def __init__(self, daddy_window, algorithm):
        super().__init__()
        self.daddy_window = daddy_window
        self.algorithm = algorithm
        self.window = VolumeRefactoringFactory().create_window(self.daddy_window, self, self.algorithm)

    def get_model_info(self):
        edges = self.shape.get_edges()
        points = self.shape.get_points()
        return points, edges

    def set_model_info(self, **kwargs):
        if 'file_path' in kwargs:
            points = self._load_object(kwargs['file_path'])
            self.shape = VolumeRefactoringFactory().create_shape(self.algorithm, points)
            self.shape.add_observer(self)
        if 'event' in kwargs:
            factory = MatrixFactory()
            matrix = factory.get_matrix(kwargs['event'])
            self.shape.compute_points(matrix)

    @staticmethod
    def _load_object(file_path: str) -> list[tuple]:
        points = np.loadtxt(file_path, dtype=float)
        return [tuple(point) for point in points]
    
    def update(self):
        self.window.update()