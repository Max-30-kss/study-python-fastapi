class User:
    def __init__(self, name='', email='', password=''):
        self.__name = name
        self.__email = email
        self.__password = password
    
    # Геттери
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    # Сеттери
    def set_name(self, name):
        self.__name = name
    
    def set_email(self, email):
        self.__email = email
    
    def set_password(self, password):
        self.__password = password

# Створення об'єкта та встановлення значень
user = User()
user.set_name("Іван Петров")
user.set_email("ivan.petrov@example.com")
user.set_password("securePassword123")

# Виведення значень
print("Ім'я:", user.get_name())
print("Електронна пошта:", user.get_email())
print("Пароль:", user.get_password())