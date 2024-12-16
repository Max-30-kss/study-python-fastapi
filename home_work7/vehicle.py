class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.is_engine_running = False
    
    def start_engine(self):
        self.is_engine_running = True
        print(f"Двигун автомобіля {self.make} {self.model} запущений.")
    
    def display_info(self):
        super().display_info()
        print(f"Тип палива: {self.fuel_type}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_capacity):
        super().__init__(make, model, year)
        self.engine_capacity = engine_capacity
    
    def wheelie(self):
        print(f"Мотоцикл {self.make} {self.model} робить wheelie!")
    
    def display_info(self):
        super().display_info()
        print(f"Об'єм двигуна: {self.engine_capacity} куб. см")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, frame_type):
        super().__init__(make, model, year)
        self.frame_type = frame_type
    
    def pedal(self):
        print(f"Їду на велосипеді {self.make} {self.model}.")
    
    def display_info(self):
        super().display_info()
        print(f"Тип рами: {self.frame_type}")

def main():
    # Створення об'єктів
    toyota_car = Car("Toyota", "Camry", 2022, "Бензин")
    harley_moto = Motorcycle("Harley-Davidson", "Street 750", 2021, 750)
    trek_bike = Bicycle("Trek", "FX 3", 2023, "Алюмінієва")

    # Демонстрація методів
    print("Інформація про транспортні засоби:")
    vehicles = [toyota_car, harley_moto, trek_bike]
    
    for vehicle in vehicles:
        vehicle.display_info()
        print()  # Порожній рядок для читабельності
    
    # Додаткові демонстраційні методи
    toyota_car.start_engine()
    harley_moto.wheelie()
    trek_bike.pedal()

if __name__ == "__main__":
    main()