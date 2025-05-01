from src.model.algorithms.polygon.polygon_build import PolygonBuild
from src.model.algorithms.polygon.graham import GrahamBuild
from src.model.algorithms.polygon.jarvis import JarvisBuild


class PolygonFactory:
    def __init__(self):
        self.polygons = {
            "Graham": GrahamBuild, 
            "Jarvis": JarvisBuild
        }
        
    def get_builder(self, algorithm: str) -> PolygonBuild:
        return self.polygons[algorithm]