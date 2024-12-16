class Animal:
    def __init__(self, name, species, age):
        """Ініціалізація атрибутів класу"""
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        """Метод для виведення звуку, який видає тварина"""
        if self.species == "dog":
            print(f"{self.name} каже: Гав-гав!")
        elif self.species == "cat":
            print(f"{self.name} каже: Мяу!")
        else:
            print(f"{self.name} видає унікальний звук.")

# Створення двох об'єктів класу Animal
animal1 = Animal("Рижик", "cat", 3)
animal2 = Animal("Рекс", "dog", 5)

# Виклик методу make_sound()
animal1.make_sound()
animal2.make_sound()