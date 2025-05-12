from typing import List, Tuple

from src.model.algorithms.filling_polygons.filling_algorithm import FillingAlgorithm
from src.model.shapes.dots.dot import Dot


class ScanlineSeedFill(FillingAlgorithm):
    requires_seed = True

    def __init__(self):
        self.boundary = set()
        self.filled = set()

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
        self.filled.clear()
        stack = [seed.get_coordinate()]
        operations = []
        while stack:
            start = stack.pop()
            x, y = start
            if y < 0 or y >= height or (x, y) in self.filled:
                continue
            left = x
            while left >= 0 and (left, y) not in self.boundary and (left, y) not in self.filled:
                left -= 1
            left = max(0, left + 1)
            right = x
            while right < width and (right, y) not in self.boundary and (right, y) not in self.filled:
                right += 1
            right = min(width - 1, right - 1)
            for px in range(left, right + 1):
                self.filled.add((px, y))
            operations.append(('line', y, left, right))
            for dy in [-1, 1]:
                ny = y + dy
                if 0 <= ny < height:
                    nx = left
                    while nx <= right:
                        while nx <= right and (nx, ny) in self.boundary or (nx, ny) in self.filled:
                            nx += 1
                        if nx > right:
                            break
                        start_x = nx
                        while nx <= right and (nx, ny) not in self.boundary and (nx, ny) not in self.filled:
                            nx += 1
                        if start_x <= nx - 1:
                            stack.append((nx - 1, ny))
                        nx += 1
        return operations