# Рассмотрим класс Shape с методом draw():

# class Shape:
#     def draw(self):
#         # drawing a shape
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def draw(self):
#         # drawing a rectangle
#         pass

# Если мы заменим Rectangle в коде на Square (квадрат), где width = height, это может привести к ошибкам,
# т.к. Square может иметь специфическую логику отрисовки.
#
# Решение:
#
# Определим абстрактный метод draw() в базовом классе Shape и переопределим его в каждом подклассе,
# учитывая особенности отрисовки:

class Shape:
    def draw(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        # Отрисовка прямоугольника
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self):
        # Отрисовка квадрата
        pass

# Теперь замена Rectangle на Square в коде будет корректной, т.к. Square корректно реализует метод draw().
