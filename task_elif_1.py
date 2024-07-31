# Задача:

# 1. Создайте функцию route_info, которой будет передаваться словарь.
# 2. Если в словаре есть ключ distance и его значение - целое число, верните строку "Distance to your destination is <distance>"
# 3. Иначе, если в словаре есть ключи speed и time, верните строку "Distance to your destination is <speed * time>"
# 4. Иначе верните строку "No distance info is available"
# 5. Вызовите функцию неколько раз с разными аргументами


# Создаем функцию в соответствии с указанными условиями:
def route_info(dict):
    if dict.get("distance") and type(dict["distance"]) is int:
        return f"Distance to your destination is {dict['distance']}"
    if dict.get("speed") and dict.get("time"):
        return f"Distance to your destination is {dict['speed'] * dict['time']}"
    return f"No distance info is available"


# Создаем словари, по которым будем проверять работу функцииЖ
my_dict1 = {
    "distance": 15,
}

my_dict2 = {
    "distance": 15.0,
}

my_dict3 = {
    "distance": 15.0,
    "speed": 5,
    "time": 3,
}

my_dict4 = {
    "speed": 3,
    "time": 5,
}

# my_dict5 = {
#     "speed": "True",
#     "time": "True",
# }

my_dict6 = {
    "name": "Dmitry",
}


print(route_info(my_dict1))
print()

print(route_info(my_dict2))
print()

print(route_info(my_dict3))
print()

print(route_info(my_dict4))
print()

# print(route_info(my_dict5))
# print()

print(route_info(my_dict6))
print()


# Альтернативное решение задачи:
# Создаем функцию в соответствии с указанными условиями:
def route_info(dict):
    if dict.get("distance") and type(dict["distance"]) is int:
        answer = f"Distance to your destination is {dict['distance']}"
    elif dict.get("speed") and dict.get("time"):
        answer = f"Distance to your destination is {dict['speed'] * dict['time']}"
    else:
        answer = f"No distance info is available"
    return answer


print(route_info(my_dict1))
print()

print(route_info(my_dict2))
print()

print(route_info(my_dict3))
print()

print(route_info(my_dict4))
print()

# print(route_info(my_dict5))
# print()

print(route_info(my_dict6))
