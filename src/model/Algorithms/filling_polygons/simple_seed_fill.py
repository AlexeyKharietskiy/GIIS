from typing import List, Tuple
from src.model.algorithms.filling_polygons.filling_algorithm import FillingAlgorithm
from src.model.shapes.dots.dot import Dot


class SimpleSeedFill(FillingAlgorithm):
    requires_seed = True

    def __init__(self):
        self.boundary = set()

    def bresenham_line(self, p1: Dot, p2: Dot) -> List[Tuple[int, int]]:
        x1, y1 = p1.x, p1.y
        x2, y2 = p2.x, p2.y
        points = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        while True:
            points.append((x1, y1))
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
        return points

    def compute_boundary(self, vertices: List[Dot]):
        self.boundary.clear()
        for i in range(len(vertices)):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % len(vertices)]
            for px in self.bresenham_line(p1, p2):
                self.boundary.add(px)

    def fill(self, vertices: List[Dot], width: int, height: int, seed: Dot = None) -> List[Tuple]:
        if not seed or len(vertices) < 3:
            return []
        
        self.compute_boundary(vertices)
        stack = [seed.get_coordinate()]
        filled = set()
        operations = []
        while stack:
            pixel = stack.pop()
            x, y = pixel
            if not (0 <= x < width and 0 <= y < height):
                continue
            if pixel in self.boundary or pixel in filled:
                continue
            filled.add(pixel)
            operations.append(('pixel', x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in self.boundary and (nx, ny) not in filled:
                    stack.append((nx, ny))
        return operations