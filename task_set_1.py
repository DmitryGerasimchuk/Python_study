# Задача:

# 1. Создайте набор с несколькими элементами типа int:
nums = {1, 3, 5, 7, 9}
# print(nums)
# print(type(nums))
# print(type(1))

# 2. Добавьте в него еще один элемент:
nums.add(0)
# print(nums)
# print(type(nums))

# 3. Создайте еще один набор с несколькими элементами, причем некоторые должны быть такими же как в первом наборе:
new_nums = {0, 3, 6, 9}
# print(new_nums)
# print(type(new_nums))

# 4. Найдите общие элементы в двух наборах и поместите их в новый набор:
my_nums = nums & new_nums
# print(my_nums)

# 5. Конвертируйте результирующий набор в список и выведите список в терминал:
my_nums_list = list(my_nums)
print(type(my_nums_list))
print(my_nums_list)