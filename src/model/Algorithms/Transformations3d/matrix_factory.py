import numpy as np
from src.model.Algorithms.Transformations3d.matrixes import (
    move_matrix,
    rotation_matrix_x,
    rotation_matrix_y,
    rotation_matrix_z,
    scaling_matrix, 
    translation_matrix,
    )

def matrix_values(event: str) -> tuple:
    events = {
        
    }
    return events[event]

class MatrixFactory:
    def __init__(self):
        self._matrix_dict = {
            'Up': translation_matrix(0, 1, 0),
            'Down': translation_matrix(0, -1, 0),
            'Left': translation_matrix(-1, 0, 0),
            'Right': translation_matrix(1, 0, 0),
            'z': translation_matrix(0, 0, 1),
            'x': translation_matrix(0, 0, -1),
            'r': rotation_matrix_x(np.deg2rad(10)),
            't': rotation_matrix_y(np.deg2rad(10)),
            'y': rotation_matrix_z(np.deg2rad(10)),
            's': scaling_matrix(2, 2, 2),
            'd': scaling_matrix(0.5, 0.5, 0.5),
        }
        
    def get_matrix(self, event: str):
        if event in self._matrix_dict:
            return self._matrix_dict[event]
        else:
            return translation_matrix(0, 0, 0)
    
    