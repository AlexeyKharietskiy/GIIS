class Dot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Dot):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        return iter((self.x, self.y))
    
    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return self.__class__(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_coordinate(self):
        return self.x, self.y