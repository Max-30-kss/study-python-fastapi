import calculator

def main():
    print("Калькулятор")
    print("Оберіть операцію: +, -, *, /")
    operation = input("Введіть операцію: ")
    
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: введіть коректні числа!")
        return

    if operation == "+":
        result = calculator.add(a, b)
    elif operation == "-":
        result = calculator.subtract(a, b)
    elif operation == "*":
        result = calculator.multiply(a, b)
    elif operation == "/":
        result = calculator.divide(a, b)
    else:
        print("Помилка: Невідома операція!")
        return

    print(f"Результат: {result}")

if __name__ == "__main__":
    main()