# 3. Таблиця множення
number = 5  # Задане число
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 4. Сума чисел
numbers = [1, 2, 3, 4, 5]  # Заданий список
sum_of_numbers = sum(numbers)
print(f"Сума чисел: {sum_of_numbers}")

# 5. Факторіал числа
num = 5  # Задане число
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Факторіал {num}: {factorial}")

# 6. Парні числа
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 7. Пошук простих чисел
start, end = 10, 30  # Заданий діапазон
for num in range(start, end + 1):
    if num > 1:  # Прості числа починаються з 2
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()
