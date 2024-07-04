# Задача:


# 1. Создайте функцию update_car_info, в которой все именнованные аргументы будут объединяться в словарь car:
# 2. Добавьте в словарь новый ключ is_available с значением True:
# 3. Верните из функции измененный словарь:
def update_car_info(**car):
    car["is_available"] = True
    # print(car)
    # print(type(car))
    return car


# 4. Вызовите функцию с именнованными аргументами brand и price, их значения могут быть любыми:
new_information = update_car_info(brand="Ford", price=1_000_000)

# 5. Выведите в терминал результат функции:
print(new_information)
