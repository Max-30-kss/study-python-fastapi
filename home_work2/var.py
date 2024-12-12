# Завдання 1: Створення змінних
string_var = "Hello, World!"
integer_var = 42
float_var = 3.14
bool_var = True
list_var = [1, 2, 3]
dict_var = {"key": "value", "number": 10}
tuple_var = (1, 2, 3)
none_var = None
print(integer_var == 42)  # True
print(float_var > 2.5)    # True
print(string_var == "Hello, World!")  # True
print("abc" < "def")                # True
# Порівняння булевих значень
print(bool_var == True)  # True
print(bool_var != False) # True

# Порівняння списків
print(list_var == [1, 2, 3])  # True
print(list_var != [3, 2, 1])  # True

# Порівняння словників
print(dict_var == {"key": "value", "number": 10})  # True
print(dict_var != {"key": "value"})                # True

# Порівняння кортежів
print(tuple_var == (1, 2, 3))  # True
print(tuple_var < (1, 2, 4))   # True