# Задача:

# 1. Создайте пустой словарь:
my_dict = {}
# print(type(my_dict))

# 2. Трижды попросите пользователя сначала ввести название ключа, а потом ввести значение этого ключа. Всего должно быть 6 запросов на ввод текста:
print("Привет! Давай заполним пустой словарь данными. Для этого тебе нужно каждый раз вводить данные в следующей последовательности: ключ - значение. Погнали!")
print()
print('Первая пара:')
one_key = input('Введи первый ключ: ')
one_value = input('Введи первое значение: ')

print()
print('Вторая пара:')
two_key = input('Введи второй ключ: ')
two_value = input('Введи второе значение: ')

print()
print('Третья пара:')
three_key = input('Введи третий ключ: ')
three_value = input('Введи третье значение: ')

print()
print('Давай посмотрим итог:')
# print(one_key, one_value, two_key, two_value, three_key, three_value)

# 3. Во время получения данных от пользователя добавляйте в словарь ключи со значениями согласно тому, что ввел пользователь:
my_dict[one_key] = one_value
my_dict[two_key] = two_value
my_dict[three_key] = three_value

# 4. Выведите результирующий словарь в терминал:
print(my_dict)
print()

# 5. Добавьте две новых пары (ключ - значение) в словарь:
print('Немного волшебства: я добавил еще данные:')
my_dict['age'] = 'Да кому эти данные интересны!'
my_dict['animal'] = 'I love them all'
print(my_dict)
print()

# 6. Удалите один ключ из словаря:
print('Согласен! Про возраст скроем: посмотри итоговый вариант словаря:')
del my_dict['age']
print(my_dict)
print(type(my_dict))