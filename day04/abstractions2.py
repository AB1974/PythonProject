import math
from abc import ABC, abstractmethod


class Volume(ABC):
    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Area of square = side^2
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Area of circle = π * radius^2
        return math.pi * (self.radius ** 2)


class Cube(Shape, Volume):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Surface area of cube = 6 * side^2
        return 6 * (self.side ** 2)

    def volume(self):
        # Volume of cube = side^3
        return self.side ** 3


class Cylinder(Shape, Volume):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        # Surface area of cylinder = 2πr^2 + 2πrh
        return (2 * math.pi * self.radius ** 2) + (2 * math.pi * self.radius * self.height)

    def volume(self):
        # Volume of cylinder = πr^2h
        return math.pi * (self.radius ** 2) * self.height


# Example Usage:
if __name__ == "__main__":
    square = Square(4)
    print(f"Square Area: {square.area()}")  # Output: Square Area: 16

    circle = Circle(3)
    print(f"Circle Area: {circle.area():.2f}")  # Output: Circle Area: 28.27

    cube = Cube(3)
    print(f"Cube Surface Area: {cube.area()}")  # Output: Cube Surface Area: 54
    print(f"Cube Volume: {cube.volume()}")  # Output: Cube Volume: 27

    cylinder = Cylinder(3, 5)
    print(f"Cylinder Surface Area: {cylinder.area():.2f}")  # Output: Cylinder Surface Area: 150.80
    print(f"Cylinder Volume: {cylinder.volume():.2f}")  # Output: Cylinder Volume: 141.37
