class Road:
    _length: int
    _width: int

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        total = int(self._length * self._width * self.weight * self.depth / 1000)
        return print(f"Масса асфальта\n {self._length} м * {self._width} м * {self.weight} кг * {self.depth} см = ", total, "т")


r = Road(30, 2500, 15, 10)
r.mass()