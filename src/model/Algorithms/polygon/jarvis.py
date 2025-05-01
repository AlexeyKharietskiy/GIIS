from src.model.algorithms.polygon.polygon_build import PolygonBuild
from src.model.shapes.polygons.polygon import Polygon
from src.model.shapes.dots.dot import Dot


class JarvisBuild(PolygonBuild):
    
    def build(self, points: list[Dot]) -> Polygon:
        if len(points) < 3:
            raise ValueError("Мало точек (<3)")
        p0 = min(points, key=lambda p: (p.y, p.x))
        hull = [p0]
        current = p0
        while True:
            next_point = None
            for p in points:
                if p == current:
                    continue
                if next_point is None:
                    next_point = p
                cp = self.cross_product(current, next_point, p)
                dist_curr_p = (p.x - current.x)**2 + (p.y - current.y)**2
                dist_curr_next = (next_point.x - current.x)**2 + (next_point.y - current.y)**2
                if cp < 0 or (cp == 0 and dist_curr_p > dist_curr_next):
                    next_point = p
            if next_point == p0:
                break
            hull.append(next_point)
            current = next_point
        return Polygon(hull)