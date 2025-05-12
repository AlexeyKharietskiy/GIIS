from typing import List, Tuple
from src.model.algorithms.filling_polygons.filling_algorithm import FillingAlgorithm
from src.model.shapes.dots.dot import Dot


class ScanlineSortedEdgeList(FillingAlgorithm):
    requires_seed = False

    def fill(self, vertices: List[Dot], width: int, height: int, seed: Dot = None) -> List[Tuple]:
        if len(vertices) < 3:
            return []
        
        y_min = min(v.y for v in vertices)
        y_max = max(v.y for v in vertices)
        
        edges = []
        for i in range(len(vertices)):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % len(vertices)]
            if p1.y != p2.y:
                y1, y2 = (p1.y, p2.y) if p1.y < p2.y else (p2.y, p1.y)
                x_start = p1.x if p1.y < p2.y else p2.x
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                m = dx / dy if dy != 0 else 0
                edges.append((y1, y2, x_start, m))
        
        edges.sort(key=lambda e: e[0])
        operations = []
        for y in range(y_min, y_max + 1):
            if 0 <= y < height:
                active_edges = [e for e in edges if e[0] <= y < e[1]]
                if active_edges:
                    x_intersections = []
                    for e in active_edges:
                        y1, y2, x_start, m = e
                        x_inter = x_start + m * (y - y1)
                        x_intersections.append(x_inter)
                    x_intersections.sort()
                    for i in range(0, len(x_intersections), 2):
                        if i + 1 < len(x_intersections):
                            x1, x2 = x_intersections[i], x_intersections[i + 1]
                            left = max(0, int(round(x1)))
                            right = min(width - 1, int(round(x2)))
                            if left <= right:
                                operations.append(('line', y, left, right))
        return operations
