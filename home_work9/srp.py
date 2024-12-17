class UserRepository:
    def __init__(self, database):
        self.database = database

    def create_user(self, user_data):
        """Відповідає лише за створення користувача в базі даних"""
        return self.database.insert(user_data)

    def update_user(self, user_id, user_data):
        """Відповідає лише за оновлення даних користувача"""
        return self.database.update(user_id, user_data)

    def delete_user(self, user_id):
        """Відповідає лише за видалення користувача"""
        return self.database.delete(user_id)

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def validate_data(self):
        """Метод валідації даних користувача"""
        if not self.name or len(self.name) < 2:
            raise ValueError("Некоректне ім'я")
        
        if not self.email or '@' not in self.email:
            raise ValueError("Некоректна електронна пошта")
        
        if self.age < 0 or self.age > 120:
            raise ValueError("Некоректний вік")

class UserService:
    def __init__(self, repository):
        self.repository = repository

    def register_user(self, user):
        """Реєстрація користувача з попередньою валідацією"""
        user.validate_data()
        return self.repository.create_user(user.__dict__)