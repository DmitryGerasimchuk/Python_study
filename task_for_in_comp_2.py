# Задача №2:

# 1. Создайте список с элементами типа str.
# 2. Из этого списка создайте новый список, в котором останутся только строки, длина которых больше 3.
# 3. Результирующий список выводите в терминал.

my_names = ["Dmitry", "Dima", "Dimas", "Dim", "Di", "D", "Dimasik"]

my_names_big = list()

# Решение задачи через цикл for...in:
# for name in my_names:
#     if len(name) > 3:
#         my_names_big.append(name)

# Решение задачи через короткую запись цикла for...in:
my_names_big = [name for name in my_names if len(name) > 3]

print(my_names_big)
