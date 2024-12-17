from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class AreaCalculator:
    @staticmethod
    def calculate_total_area(shapes):
        """Розрахунок площі без модифікації існуючих класів"""
        return sum(shape.calculate_area() for shape in shapes)

# Приклад використання
circle = Circle(5)
rectangle = Rectangle(4, 6)
total_area = AreaCalculator.calculate_total_area([circle, rectangle])
print(f"Загальна площа: {total_area}")