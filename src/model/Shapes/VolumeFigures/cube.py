import numpy as np
from src.model.Shapes.Shape import Shape
from src.model.Shapes.Dot.dot_3d import Dot3D


class Cube(Shape):
    def __init__(self, points: list[tuple]):
        self.points = [Dot3D(*point) for point in points ]
        self.edges:list[tuple[Dot3D, Dot3D]] = []
        self._observers = []
        
    def compute_points(self, matrix: tuple):
        np_matrix = np.array(matrix)
        self.points = self._apply_transformation(self.points, np_matrix)
        self._notify_observers()
        
    @staticmethod
    def _apply_transformation(dots: list[Dot3D], refactor_matrix: np.array):
        points = np.array([[*dot] for dot in dots])
        homogeneous_points = np.hstack((points, np.ones((points.shape[0], 1))))
        transformed = np.dot(homogeneous_points, refactor_matrix.T)
        return [Dot3D(*row) for row in transformed[:, :3]]
    
    def get_edges(self) -> tuple[list, list]:
        edge_indices = [
        (0, 1), (1, 3), (3, 2), (2, 0),
        (4, 5), (5, 7), (7, 6), (6, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
        ]
    
        edges = [([*self.points[i]], [*self.points[j]]) for i, j in edge_indices]
        return edges
    
    def get_points(self):
        points = [[*point] for point in self.points]
        return points
        
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def _notify_observers(self):
        for observer in self._observers:
            observer.update()