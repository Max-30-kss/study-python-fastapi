import utilities

def main():
    print("Робота зі списком чисел")
    
    try:
        numbers = list(map(float, input("Введіть числа через пробіл: ").split()))
    except ValueError:
        print("Помилка: введіть коректні числа!")
        return

    if not numbers:
        print("Помилка: список порожній")
        return

    average = utilities.calculate_average(numbers)
    maximum = utilities.find_max(numbers)

    print(f"Середнє значення: {average}")
    print(f"Найбільше число: {maximum}")

if __name__ == "__main__":
    main()