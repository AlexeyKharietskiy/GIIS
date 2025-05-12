from src.model.shapes.polygons.model import PolygonModel
from src.controller.polygon.window_factory import PolygonWinFactory
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
        self.model = PolygonModel()
        self.current_vertices = []
        self.selecting_seed = False
        self.algorithm = "ScanlineSortedEdgeList"
        self.daddy_window = daddy_window
        self.join_mode = False
        self.adjust_mode = False
        self.algorithm_window = algorithm
        self.shapes = []
        self.window = PolygonWinFactory().create_window(self.daddy_window, self, self.algorithm_window)
        self.input_window = None
        self.update_seed_button_state()
        
        
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

    def on_canvas_click(self, x, y):
        if self.selecting_seed:
            if self.model.polygons:
                seed = Dot(x, y)
                self.model.polygons[-1].seed = seed
                self.window.draw_seed(seed)
            self.selecting_seed = False
            self.update_seed_button_state()
        else:
            dot = Dot(x, y)
            self.current_vertices.append(dot)
            self.window.canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")

    def on_build_polygon(self):
        if len(self.current_vertices) >= 3:
            polygon = self.model.add_polygon(self.current_vertices)
            self.window.draw_polygon(polygon.points)
            self.current_vertices = []
            self.update_seed_button_state()

    def on_select_seed(self):
        if self.model.polygons and self.algorithm in ["SimpleSeedFill", "ScanlineSeedFill"]:
            self.selecting_seed = True
            self.update_seed_button_state()

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm
        self.update_seed_button_state()

    def update_seed_button_state(self):
        state = "normal" if self.algorithm in ["SimpleSeedFill", "ScanlineSeedFill"] and self.model.polygons else "disabled"
        if self.window:
            self.window.select_seed_button.config(state=state)

    def on_fill_polygons(self):
        width = self.window.canvas.winfo_width()
        height = self.window.canvas.winfo_height()
        debug = self.window.debug_var.get()
        for polygon in self.model.polygons:
            if not polygon.filled:
                operations = self.model.get_operations(self.algorithm, polygon, width, height)
                if operations:
                    self.window.perform_operations(operations, debug)
                    polygon.filled = True
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.window = view
        self.current_vertices = []
        self.selecting_seed = False
        self.algorithm = "ScanlineSortedEdgeList"
        self.update_seed_button_state()

    