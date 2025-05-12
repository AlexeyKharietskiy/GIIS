from typing import List, Tuple

from src.model.algorithms.filling_polygons.filling_algorithm import FillingAlgorithm
from src.model.shapes.dots.dot import Dot


class ScanlineActiveEdgeList(FillingAlgorithm):
    requires_seed = False

    def fill(self, vertices: List[Dot], width: int, height: int, seed: Dot = None) -> List[Tuple]:
        if len(vertices) < 3:
            return []
        
        y_min = min(v.y for v in vertices)
        y_max = max(v.y for v in vertices)
        
        class Edge:
            def __init__(self, y_min, y_max, x_start, m):
                self.y_min = y_min
                self.y_max = y_max
                self.x = x_start
                self.m = m
        
        edges = []
        for i in range(len(vertices)):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % len(vertices)]
            if p1.y != p2.y:
                y1, y2 = (p1.y, p2.y) if p1.y < p2.y else (p2.y, p1.y)
                x_start = p1.x if p1.y < p2.y else p2.x
                m = (p2.x - p1.x) / (p2.y - p1.y)
                edges.append(Edge(y1, y2, x_start, m))
        
        edges.sort(key=lambda e: e.y_min)
        active_edges = []
        operations = []
        for y in range(y_min, y_max + 1):
            if 0 <= y < height:
                active_edges.extend(e for e in edges if e.y_min == y)
                active_edges = [e for e in active_edges if e.y_max > y]
                for e in active_edges:
                    e.x += e.m
                x_list = sorted(e.x for e in active_edges)
                for i in range(0, len(x_list), 2):
                    if i + 1 < len(x_list):
                        x1, x2 = x_list[i], x_list[i + 1]
                        left = max(0, int(round(x1)))
                        right = min(width - 1, int(round(x2)))
                        if left <= right:
                            operations.append(('line', y, left, right))
        return operations