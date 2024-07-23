# Этот класс нарушает SRP, так как он имеет две несвязанные задачи: вычисление площади и вычисление периметра.
class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# ================================================
# Решение

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.PI * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * self.PI * self.radius
