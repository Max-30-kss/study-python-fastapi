def calculate_average(numbers):
    if not numbers:
        return "Помилка: список порожній"
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if not numbers:
        return "Помилка: список порожній"
    return max(numbers)