# Задача:

# 1. Создайте любой словарь, используя ключи с значениями разных типов.
# 2. Конвертируйте словарь в JSON.
# 3. Результирующий JSON выведите в терминал.
# 4. Выведите в терминал тип результирующего значения.
import json as js

my_info = {
    "name": "Dmitry",
    "age": 37,
    "favorite_numbers": [3, 9, 63],
    "marrige": False,
    "city": "Moscow",
}

my_info_json = js.dumps(my_info, indent=3)
print(my_info_json)

print(type(my_info_json))  # <class 'str'>
