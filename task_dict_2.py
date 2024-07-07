# Задача:

# 1. Создайте три разных словаря и объедините их двумя разными способами:
dict_1 = {
    "one": 1,
    "two": 2,
    "three": 3,
}

dict_2 = {
    "four": 4,
    "five": 5,
    "six": 6,
}

dict_3 = {
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

print(type(dict_1), type(dict_2), type(dict_3))

dict_123_1 = {
    **dict_1,
    **dict_2,
    **dict_3,
}

print(dict_123_1)

dict_123_2 = dict_1 | dict_2 | dict_3

print(dict_123_2)
