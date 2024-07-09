# Задача:


# 1. Даны три переменных:
# my_name = "Dmitry"
# my_hobby = "reading books"
# time = 23
# Используя понятие f-строк, написать предложение "Дмитрий любит читать книги в 23 часа" так, чтобы все слова в предложении начинались с заглавной буквы:
my_name = "Dmitry"
my_hobby = "reading books"
time = 23

info = f"{my_name} likes {my_hobby} at {time} o'clock"
info_title = info.title()
print(
    info
)  # обычная строка: тут метод использовать нежелательно, так как не все слова будут с заглавной буквы
print(info_title)

# 2. Создайте еще одну строку, используя f-строки, но чтобы в ней было 4 разных типа переменных (до формирования строки):
word_1 = "Dmitry"
word_2 = [10, 30]
word_3 = 9
word_4 = False

info_4 = f"{word_3} июля {word_1} встал в {word_2}. Что не есть хорошо, а наоборот - {word_4}."
print(info_4)
