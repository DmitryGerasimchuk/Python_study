# Задача:


# 1. Создайте функцию merge_list_to_dict:
# 2. У функции должно быть два параметра:
# 3. Функция должна объединять два списка, используя встроенную функцию zip:
# 4. Конвертируйте zip в словарь и верните его из функции:
def merge_list_to_dict(list_1, list_2):
    list_3 = zip(list_1, list_2)
    dict_1 = dict(list_3)
    return dict_1


# 5. Вызовите функцию, передав ей два списка в качестве аргументов:
my_list_1 = [0, 1, 2, 3, 4, 10]
my_list_2 = [5, 6, 7, 8, 9]

my_dict = merge_list_to_dict(my_list_1, my_list_2)

# 6. Выведите результат вызова функции в терминал:
print(my_dict)
print(type(my_dict))
