# Задача:


# 1. Создайте две переменные и присвойте им одинаковые последовательности типа set. При этом не копируйте одну переменную в другую:
set_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(type(set_1))
# print(type(set_2))
# print(id(set_1))
# print(id(set_2))

# 2. Выведите в терминал результат сравнения двух созданных объектов, объясните результат:
print(set_1 == set_2)  # сравниваются элементы, и они одинаковые

# 3. Сравните два объекта, используя оператор is, объясните результат:
print(set_1 is set_2)  # сравниваются ссылки, и они разные

# 4. Проверьте, есть ли определнные элементы в наборе, используя оператор in:
print(0 in set_1)
print(10 in set_2)
print(10 not in set_2)