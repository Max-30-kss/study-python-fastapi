import requests 

# windows_activate = ".\venv\Scripts\activate"

site = "https://jsonplaceholder.typicode.com"

# Виконуємо GET-запит
response = requests.get(url=site)
print(response.text)
print("-----------")