from abc import ABC, abstractmethod

# Абстракція для підключення до бази даних
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

# Конкретна реалізація підключення до бази даних
class MySQLDatabase(DatabaseConnection):
    def connect(self):
        print("Connecting to MySQL database...")

class PostgreSQLDatabase(DatabaseConnection):
    def connect(self):
        print("Connecting to PostgreSQL database...")

# Сервіс користувача, який залежить від абстракції
class UserService:
    def __init__(self, db: DatabaseConnection):
        self.db = db  # Залежність через абстракцію

    def get_user(self, user_id):
        self.db.connect()
        print(f"Fetching user with ID: {user_id}")

# Використання
mysql_db = MySQLDatabase()
postgres_db = PostgreSQLDatabase()

user_service_mysql = UserService(mysql_db)
user_service_postgres = UserService(postgres_db)

user_service_mysql.get_user(1)
user_service_postgres.get_user(2)