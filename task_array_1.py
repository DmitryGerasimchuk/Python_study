# Задача:


# 1. Создайте новый файл под названием process_array.py и в этом файле нужно ожидать аргументы от пользователя, которые будут являться именем файла, из которого необходимо будет создать массив

import sys

# Получаем имя файла из аргументов командной строки
if len(sys.argv) != 2:
    print("Внимание ошибка: введены значения, которые не могут быть названием файла")

my_array = sys.argv[1]

# Открываем файл и читаем его содержимое
with open("process_array.py", "w") as my_file:
    my_file.write(my_array)

with open("process_array.py", "r") as my_file:
    print(my_file)