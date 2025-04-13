class Dot:
    def __init__(self, x, y, intensity=1):
        self.x = x
        self.y = y
        self.intensity = intensity

    def __eq__(self, other):
        if isinstance(other, Dot):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        return iter((self.x, self.y))

    def get_coordinate(self):
        return self.x, self.y