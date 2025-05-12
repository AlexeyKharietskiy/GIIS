from typing import List, Tuple

from src.model.shapes.dots.dot import Dot


class FillingAlgorithm:
    requires_seed = False

    def fill(self, vertices: List[Dot], width: int, height: int, seed: Dot = None) -> List[Tuple]:
        pass