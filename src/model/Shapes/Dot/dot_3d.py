from src.model.Shapes.Dot.dot import Dot


class Dot3D(Dot):
    def __init__(self, x: int, y: int, z: int):
        super().__init__(x, y, intensity=1)
        self.z = z
        
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
        
    def __eq__(self, other):
        if isinstance(other, Dot):
            return (
                self.x == other.x 
                and self.y == other.y
                and self.z == other.z
                )
        return False