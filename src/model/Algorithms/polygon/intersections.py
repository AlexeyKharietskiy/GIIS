from src.model.shapes.lines.line import Line
from src.model.shapes.dots.dot import Dot


def line_intersection(
    p1: Dot, 
    p2: Dot, 
    p3: Dot, 
    p4: Dot
    ):
    dx12 = p2.x - p1.x
    dy12 = p2.y - p1.y
    dx34 = p4.x - p3.x
    dy34 = p4.y - p3.y
    den = dx12 * dy34 - dy12 * dx34
    if den == 0:
        return None
    t = ((p3.x - p1.x) * dy34 - (p3.y - p1.y) * dx34) / den
    u = -((p1.x - p3.x) * dy12 - (p1.y - p3.y) * dx12) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return Dot(p1.x + t * dx12, p1.y + t * dy12)
    return None

def find_intersections(line: Line, polygon):
    intersections = []
    n = len(polygon)
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        intersection = line_intersection(line.start, line.end, p1, p2)
        if intersection:
            intersections.append(intersection)
    return intersections