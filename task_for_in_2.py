# Задача №2:

# 1. Создайте функцию filter_list, которая будет фильтровать список
# 2. У функции должно быть два параметра - список и тип значения.
# 3. Функция должна вернуть новый список, в котором остануться только значение того типа, который был передан в вызове функции вторым аргуменнтом.
# 4. Фунуцию можно будет вызвать например так:
#     filter_list([35, True, 'abc', 10], int) и получить [35,10]


# Создаем функцию под требования задачи:
def filter_list(list, a):
    my_list = []
    for elem in list:
        if a == bool and isinstance(elem, bool):
            my_list.append(elem)
        if a != bool and isinstance(elem, a) and type(elem) != bool:
            my_list.append(elem)
    return my_list


# Запускаем функцию и проверяем условие:
print(filter_list([35, None, "abc", 10, 67.9, False, True, 78], bool))


"""ChatGPT сделал замечания и предложил следующий код:"""


def filter_list(lst, value_type):
    return [
        elem
        for elem in lst
        if isinstance(elem, value_type)
        and not (isinstance(elem, bool) and value_type == int)
    ]


# Запускаем функцию и проверяем условие:
print(
    filter_list([35, None, "abc", 10, 67.9, False, True, 78], bool)
)  # Ожидаемый вывод: [False, True]
print(
    filter_list([35, None, "abc", 10, 67.9, False, True, 78], int)
)  # Ожидаемый вывод: [35, 10, 78]
print(
    filter_list([35, None, "abc", 10, 67.9, False, True, 78], float)
)  # Ожидаемый вывод: [67.9]
print(
    filter_list([35, None, "abc", 10, 67.9, False, True, 78], str)
)  # Ожидаемый вывод: ["abc"]
print(
    filter_list([35, None, "abc", 10, 67.9, False, True, 78], type(None))
)  # Ожидаемый вывод: [None]
