# Задача:


# 1. Создайте функцию image_info с одним параметром типа dict
# 2. Функция ожидает словарь, в котором должно быть как минимум два ключа:
#     image_id
#     image_title
# 3. Функция должна возвращать строку такого типа:
#     "Image 'my cat' has id 5136" (строка формируется динамическим образом)
# 4. Если хотя бы одного из ключей в словаре нет, функция должна генерировать ошибку TypeError (текст ошибки должен быть любым, но понятным, что ожидается от пользователя)
def image_info(dict):
    if len(dict) < 2:  # проверка на количество ключей: их должно не менее 2
        raise ValueError("В словаре недостаточно обязательных параметров")
    elif (
        not "image_id" in dict
    ):  # проверка наличия в словаре обязательного ключа с номером картинки
        raise TypeError("В словаре отсутсвует обязательный параметр image_id")
    elif (
        not "image_title" in dict
    ):  # проверка наличия в словаре обязательного ключа с наименованием картинки
        raise TypeError("В словаре отсутсвует обязательный параметр image_title")
    return print(f"Image '{dict.get('image_title')}' has id {dict.get('image_id')}.")


# 5. Вызовите функцию и корректно обработайте ошибку в случае возникновения (текст ошибки выведите в терминал)
dict_1 = {
    "image_id": "001",
    "image_title": "Котик",
}  # словарь с двумя обязательными ключами

# 6. Вызовите функцию несколько раз сразными словарями
# dict_1 = {
#     "size": "321",
#     "image_title": "Котик",
# }  # словарь с двумя ключами, но без обязательного image_id

# dict_1 = {
#     "image_id": "001",
#     "name": "Котик",
# }  # словарь с двумя ключами, но без обязательного image_title

# dict_1 = {
#     "image_id": "001",
# }  # словарь с одним ключом

dict_1 = {
    "image_id": "034",
    "size": "321",
    "image_title": "Котик",
    "name": "Мурик",
}  # словарь с множеством ключей, среди которых есть все обязательные

try:
    image_info(dict_1)
except Exception as e:
    print(e)

print("Функция не помешала продоллжить работе программе")


# Код ChatGPT после проверки моего кода - оценка 8 из 10:
# def image_info(image_dict):
#     if 'image_id' not in image_dict:
#         raise KeyError("Словарь должен содержать ключ 'image_id'.")
#     if 'image_title' not in image_dict:
#         raise KeyError("Словарь должен содержать ключ 'image_title'.")
#     return f"Image '{image_dict['image_title']}' has id {image_dict['image_id']}."

# # Вызовы функции с различными словарями
# dict_1 = {
#     "image_id": "001",
#     "image_title": "Котик",
# }

# dict_2 = {
#     "size": "321",
#     "image_title": "Котик",
# }

# dict_3 = {
#     "image_id": "001",
#     "name": "Котик",
# }

# dict_4 = {
#     "image_id": "001",
# }

# dict_5 = {
#     "image_id": "034",
#     "size": "321",
#     "image_title": "Котик",
#     "name": "Мурик",
# }

# # Проверка функции с обработкой ошибок
# for d in [dict_1, dict_2, dict_3, dict_4, dict_5]:
#     try:
#         result = image_info(d)
#         print(result)
#     except KeyError as e:
#         print(f"Ошибка: {e}")

# print("Функция не помешала продолжить работе программе")
