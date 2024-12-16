class Rectangle:
    def __init__(self, width, height):
        """Ініціалізація атрибутів класу"""
        self.width = width
        self.height = height

    def calculate_area(self):
        """Метод для обчислення площі прямокутника"""
        return self.width * self.height

# Створення двох об'єктів класу Rectangle
rectangle1 = Rectangle(8, 15)
rectangle2 = Rectangle(5, 3)

# Виклик методу calculate_area() і виведення площі
print(f"Площа першого прямокутника: {rectangle1.calculate_area()} кв. одиниць")
print(f"Площа другого прямокутника: {rectangle2.calculate_area()} кв. одиниць")