from src.controller.polygon.factory import PolygonFactory
from src.model.algorithms.polygon.graham import GrahamBuild
from src.model.algorithms.polygon.jarvis import JarvisBuild
from src.model.shapes.dots.dot import Dot
from src.model.shapes.polygons.polygon import Polygon
from src.model.shapes.lines.line import Line
from view.polygon.polygon_drawer import DrawingInterface
from src.model.algorithms.polygon.intersections import find_intersections

class PolygonController:
    def __init__(self, daddy_window, algorithm):
        self.daddy_window = daddy_window
        self.join_mode = False
        self.adjust_mode = False
        self.algorithm = algorithm
        self.shapes = []
        self.window = DrawingInterface(self.daddy_window, self)
        self.input_window = None
        
    def add_line(self, start: tuple, end: tuple):
        line = Line(start, end)
        self.shapes.append(line)
        intersections = []
        for shape in self.shapes:
            if isinstance(shape, Polygon):
                inters = find_intersections(line, shape.points)
                intersections.extend(inters)
        return intersections
        
    def add_polygon(self, points, algorithm):
        dots = [Dot(*point) for point in points]
        builder = PolygonFactory().get_builder(algorithm)
        polygon = builder().build(dots)
        self.shapes.append(polygon)
        return polygon
        
    def add_dot(self, x: int, y: int):
        self.shapes.append(Dot(x, y))
        
    def is_point_inside(self, point: tuple):
        dot = Dot(*point)
        for shape in self.shapes:
            if isinstance(shape, Polygon):
                if shape.is_point_inside(dot):
                    return True, shape
        return False, None
    
    def get_edges(self):
        polygon = None
        for shape in self.shapes:
            if isinstance(shape, Polygon):
                polygon = shape
        return polygon
    
    def change_algorithm(self, algorithm):
        self.algorithm = algorithm
        self.window = DrawingInterface(self.daddy_window, self)

        