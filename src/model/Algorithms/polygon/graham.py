import math
from src.model.shapes.polygons.polygon import Polygon
from src.model.algorithms.polygon.polygon_build import PolygonBuild
from src.model.shapes.dots.dot import Dot


class GrahamBuild(PolygonBuild):
    
    @staticmethod
    def polar_angle(p0, p1):
        dx = p1.x - p0.x
        dy = p1.y - p0.y
        return math.atan2(dy, dx)
    
    def build(self, points: list[Dot]) -> Polygon:
        if len(points) < 3:
            raise ValueError("Мало точек (<3)")
        p0 = min(points, key=lambda p: (p.y, p.x))
        sorted_points = sorted(
            points, 
            key=lambda p: (
                self.polar_angle(p0, p), 
                (p.x - p0.x)**2 + (p.y - p0.y)**2
                )
            )
        stack = [sorted_points[0], sorted_points[1]]
        for i in range(2, len(sorted_points)):
            while (
                len(stack) >= 2 and 
                self.cross_product(stack[-2], stack[-1], sorted_points[i]) <= 0
                ):
                stack.pop()
            stack.append(sorted_points[i])
        
        return Polygon(stack)