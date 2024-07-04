# Задача:


# 1. Перепишите вызов функции merge_list_to_dict из предыдущей задачи так, чтобы в нем использовались аргументы с ключевыми словами:
def merge_list_to_dict(first_list, second_list):
    result_list = zip(first_list, second_list)
    result_dict = dict(result_list)
    return result_dict


my_first_list = [0, 1, 2, 3, 4, 10]
my_second_list = [5, 6, 7, 8, 9]

my_result_dict = merge_list_to_dict(
    first_list=[0, 1, 2, 3, 4, 10], second_list=[5, 6, 7, 8, 9]
)

print(my_result_dict)
print(type(my_result_dict))

# 2. Добавьте еще один вызов функции, в котором будет один позиционный аргумент, а второй - аргумент с ключевым словом:
my_result_dict = merge_list_to_dict(my_first_list, second_list=[5, 6, 7, 8, 9])

print(my_result_dict)
print(type(my_result_dict))
