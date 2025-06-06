from src.model.shapes.dots.dot import Dot


class InterpolationDot(Dot):
    def __init__(self, x, y, x_ref_coord, y_ref_coord):
        super().__init__(x, y)
        self.x_ref_coord = x_ref_coord
        self.y_ref_coord = y_ref_coord

    def __iter__(self):
        return iter((self.x, self.y, self.x_ref_coord, self.y_ref_coord))

    def get_ref_info(self):
        return self.x_ref_coord, self.y_ref_coord
