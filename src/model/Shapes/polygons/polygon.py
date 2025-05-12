from src.model.shapes.dots.dot import Dot

def cross_product(p1: Dot, p2: Dot, p3: Dot):
        v1 = p2 - p1
        v2 = p3 - p2
        return v1.x * v2.y - v1.y * v2.x
    
class Polygon:
    def __init__(self, points: list[Dot]):
        self.points = points
        self.internal_normals = None
        self.seed = None
        self.filled = False
        self.sides = [
            (
                self.points[i],
                self.points[(i + 1) % len(self.points)]
                ) 
            for i in range(len(self.points))
            ]
        self.is_convex: bool = self.check_convexity
        
        
    def check_convexity(self):
        n = len(self.points)
        if n < 3:
            return False
        sign = None
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]
            p3 = self.points[(i + 2) % n]
            cp = cross_product(p1, p2, p3)
            if cp != 0:
                current_sign = cp > 0
                if sign is None:
                    sign = current_sign
                elif sign != current_sign:
                    return False
        return True
    
    def is_point_inside(self, point):
        n = len(self.points)
        inside = False
        p1 = self.points[0]
        for i in range(n + 1):
            p2 = self.points[i % n]
            if point.y > min(p1.y, p2.y):
                if point.y <= max(p1.y, p2.y):
                    if point.x <= max(p1.x, p2.x):
                        if p1.y != p2.y:
                            xinters = (point.y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x
                        if p1.x == p2.x or point.x <= xinters:
                            inside = not inside
            p1 = p2
        return inside
    
    def get_internal_normals(self):
        n = len(self.points)
        normals = []
        center = sum(self.points, Dot(0, 0)) * (1 / n)
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]
            side = p2 - p1
            normal = Dot(-side.y, side.x)
            to_center = center - p1
            if normal.x * to_center.x + normal.y * to_center.y < 0:
                normal = Dot(-normal.x, -normal.y)
            normals.append(normal)
        return normals