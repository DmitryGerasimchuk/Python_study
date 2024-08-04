# Задача:

# 1. Создайте класс Image.
# 2. У каждого экземпляра класса Image должно быть три собственных атрибута
# - resolution
# - title
# - extension
# 3. В классе должен быть метод resize, с помощью которого можно поменять разрешение изображения. Вы должны просто менять значения атрибута resolution.
# 4. Создайте несколько экземпляров класса Image и вызовите метод resize.


# создание класса и прописывание трех методов - изменение разрешения, вывод информации о файле и изменение названия файла
class Image:
    def __init__(self, resolution="1920x1980", title="New image", extension=".jpg"):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, resolution):
        self.resolution = resolution

    def print_info(self):
        print(
            f"Основаная информация о настоящей картинке: разрешение - {self.resolution}, название файла - {self.title}, разрешение файла - {self.extension}"
        )

    def rename(self, title):
        self.title = title


# создание первого экземпляра класса
my_first_image = Image()
# проверка экземпляра (относится ли он к данному классу и где находится в памяти)
print(my_first_image)
# вывод информации о файле
my_first_image.print_info()
# вывод информации об экземпляре, в том числе информации, которая идет по умолчанию
print(my_first_image.__dict__)
# изменение стандартного разрешения на 1000х1000
my_first_image.resize("1000x1000")
# проверка изменения через вывод информации о файле
my_first_image.print_info()

# создание второго экземпляра класса
my_second_image = Image()
# вывод информации об экземпляре, в том числе информации, которая идет по умолчанию
my_second_image.print_info()
# изменение стандартного разрешения на 0х0
my_second_image.resize("0x0")
# проверка изменения через вывод информации о файле
my_second_image.print_info()

# проверка двух экземпляров (а точно они разные)
print(my_first_image == my_second_image)
# вывод информации о файле
my_first_image.print_info()
# переименование второго файла
my_second_image.rename("Новая картинка")
# проверка изменения через вывод информации о файле
my_second_image.print_info()
# проверка разности название двух файлов
print(my_first_image.title == my_second_image.title)
print(my_second_image.title)
print(my_first_image.title)
