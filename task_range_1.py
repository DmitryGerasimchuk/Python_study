#Задача:

# 1. Создайте самостоятельно диапазон, причем используя при задании параметры начала, окончания и шага: 
my_range = range(3, 9, 2)
# print(type(my_range))
# print(list(my_range))

# 2. Создайте пустой список:
my_list = []
# print(type(my_list))

# 3. Выполните итерацию по диапазону, используя цикл for.В цикле записывайте элементы диапазона в список: 
for i in my_range:
    my_list.append(i)
print(my_list) 
print(len(my_list))