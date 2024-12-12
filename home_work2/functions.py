#Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = str(125)
print(num_str)  

# Заміна символів у рядку
message = "Hi, my name is Python!"
message_replaced = message.replace("y", "0").replace("i", "1")
print(message_replaced)  

# Розділення і з'єднання рядків
split_test = "This is a split test"
split_list = split_test.split(" ")
string_join = " ".join(split_list)
print(string_join)  

# Довжина рядка
print(len(string_join))  

# Робота зі списками
# Додавання елементів до списку
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)  

# Розширення списку
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)  

# Індекс елемента у списку
index_of_6 = list_extend.index(6)
print(index_of_6)  

# Довжина списку
print(len(list_append))  

# Робота зі словниками
# Виведення значень за ключами
dict_test = {"car": "Toyota", "price": 4900, "where": "EU"}
print(dict_test["car"])   
print(dict_test["where"]) 

# Виведення ключів і значень
print(dict_test.keys())   
print(dict_test.values()) 

# Виведення пар ключ-значення
print(dict_test.items())  
