from abc import ABC, abstractmethod

from src.model.shapes.dots.dot import Dot
from src.model.shapes.polygons.polygon import Polygon


class PolygonBuild(ABC):
    @staticmethod
    def cross_product(p1: Dot, p2: Dot, p3: Dot):
        v1 = p2 - p1
        v2 = p3 - p2
        return v1.x * v2.y - v1.y * v2.x
    
    @abstractmethod
    def build():
        ...