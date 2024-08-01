# Задача:

# 1. Создайте цикл, в котором нужно попросить пользователя ввести в терминал для числа.
# 2. Выведите в терминал результат деления первого числа на второе.
# 3. После этого спросите пользователя, хочет ли он продолжить yes/no.
# 4. Если ответ отрицательный, то нужно выйти из цикла.
# 5. Иначе нужно повторить все сначала.

# Приветствие программы, чтобы пользователь понимал, что программа делает
print("Программа, которая выполняет деление одного числа на второе")
print()  # пустая строка, чтобы удобно было смотреть в терминале

while True:
    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число (не равное 0): "))
    result = number1 / number2
    print()  # пустая строка, чтобы удобно было смотреть в терминале
    print(result)
    print()  # пустая строка, чтобы удобно было смотреть в терминале
    question = input("Желаете повторить операцию деления ('да' -> y, 'нет' -> n): ")
    if question == "y":
        print("Отлично! Продолжаем")
        continue
    elif question == "n":
        break
    else:
        print("Вы нажали на неверную кнопку. Я буду это понимать как ответ 'да'")

print()  # пустая строка, чтобы удобно было смотреть в терминале
print("Спасибо, что использовали программу!")


""" ChatGPT внимательно изучил код и предложил улучшения:"""

# Приветствие программы, чтобы пользователь понимал, что программа делает
print("Программа, которая выполняет деление одного числа на второе")
print()  # пустая строка, чтобы удобно было смотреть в терминале

while True:
    try:
        number1 = float(input("Введите первое число: "))
        number2 = float(input("Введите второе число (не равное 0): "))
        if number2 == 0:
            print(
                "Ошибка: Деление на ноль невозможно. Пожалуйста, введите второе число заново."
            )
            continue
        result = number1 / number2
        print()  # пустая строка, чтобы удобно было смотреть в терминале
        print(f"Результат деления: {result}")
        print()  # пустая строка, чтобы удобно было смотреть в терминале
    except ValueError:
        print("Ошибка: Введены некорректные данные. Пожалуйста, введите числа заново.")
        continue

    question = input(
        "Желаете повторить операцию деления ('да' -> y, 'нет' -> n): "
    ).lower()
    if question == "y":
        print("Отлично! Продолжаем")
    elif question == "n":
        break
    else:
        print("Вы нажали на неверную кнопку. Я буду это понимать как ответ 'да'")

print()  # пустая строка, чтобы удобно было смотреть в терминале
print("Спасибо, что использовали программу!")
