# Задача 1:

# 1. Создайте список из 5 элементов разных типов:
my_list = [100, 'zero', None, False, {'age':0}]
# print(my_list)
# print(type(my_list))
# print(len(my_list))

# 2. Удалите третий элемент:
my_list.pop(2)
# print(my_list)

# 3. Выведите в терминал длину списка:
print(len(my_list))

# 4. Поменяйте порядок следования элементов в списке:
my_list.reverse()
# print(my_list)

# 5. Создайте еще один список с двумя элементами:
new_my_list = ['Dima', 'Gerasimchuk']
# print(new_my_list)

# 6. Расширьте первый список элементами второго списка:
my_list.append(new_my_list[0])
my_list.append(new_my_list[1])
# print(type(my_list))
# print(len(my_list))

# 7. Выведите в терминале расширенный список из 6 элементов
print(my_list)