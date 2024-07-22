# Задача:


# 1. Создайте список из 3-х словарей.
# 2. С помощью оператора распаковки списков создайте три переменных, каждая из которых будет содержать по одному словарю.
# 3. Создайте функцию, которая будет принимать два аргумента и в вызове функции вы должны распаковать словарь. Функцию вызовите трижды.

my_family = [
    {
        "name": "Dmitry",
        "age": 37,
    },
    {
        "name": "Svytoslav",
        "age": 41,
    },
    {
        "name": "Irina",
        "age": 37,
    },
]
# print(type(my_family))
# print(my_family)

Dima, Slava, Ira = my_family
# print(Dima)
# print(Slava)
# print(Ira)
# print(type(Dima))


def info_family(name, age):
    return f"{name} является членом моей семьи. Этому человеку {age} лет"


print(info_family(**Dima))
print(info_family(Ira["name"], Ira["age"]))
print(info_family(name=Slava["name"], age=Slava["age"]))
