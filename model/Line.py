from Shape import Shape


class Line(Shape):
    def draw(self, alghoritm):
        points = algorithm.compute_points(self.start, self.end)
        for point in points:
            canvas.create_rectangle(point[0] - 1, point[1] - 1, point[0] + 1, point[1] + 1, fill="black")