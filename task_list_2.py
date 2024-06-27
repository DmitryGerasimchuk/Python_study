# Задача 2:

# 1. Создайте два списка:
list_1 = ['Слава', 'Дима']
list_2 = [40, 37]
# print(list_1, list_2)

# 2. Объедините два списка, используя оператор +:
family_list = list_1 + list_2
# print(family_list)

# 3. Определите, какой магический метод списков вызывается при использовании оператора +:
# print(dir(family_list))

# 4. Выполните слияние списков, используя этот магический метод:
new_family_list = list_1.__add__(list_2)
# print(new_family_list)

# 5. Результат выведите в терминал:
print(family_list)
print(new_family_list)