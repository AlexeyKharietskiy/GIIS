from typing import List
from src.model.algorithms.filling_polygons.scanline_active_edge import ScanlineActiveEdgeList
from src.model.algorithms.filling_polygons.scanline_seed_fill import ScanlineSeedFill
from src.model.algorithms.filling_polygons.scanline_sorted_edge import ScanlineSortedEdgeList
from src.model.algorithms.filling_polygons.simple_seed_fill import SimpleSeedFill
from src.model.shapes.dots.dot import Dot
from src.model.shapes.polygons.polygon import Polygon


class PolygonModel:
    def __init__(self):
        self.polygons = []
        self.algorithms = {
            "ScanlineSortedEdgeList": ScanlineSortedEdgeList(),
            "ScanlineActiveEdgeList": ScanlineActiveEdgeList(),
            "SimpleSeedFill": SimpleSeedFill(),
            "ScanlineSeedFill": ScanlineSeedFill()
        }

    def add_polygon(self, points: List[Dot]):
        polygon = Polygon(points)
        self.polygons.append(polygon)
        return polygon

    def get_operations(self, algorithm_name: str, polygon: Polygon, width: int, height: int):
        algorithm = self.algorithms[algorithm_name]
        seed = polygon.seed if algorithm.requires_seed else None
        return algorithm.fill(polygon.points, width, height, seed)