import pygame
import sys
# from random import randint

# clock = pygame.time.Clock()

pygame.init() # инициация пакета для создания игры

pygame.display.set_caption("Arhwolf Pygame")

screen_width, screen_height = 800, 600 # ширина и высота экрана
screen = pygame.display.set_mode((screen_width, screen_height)) # описание игрового дисплея 888 на 600
fill_color = (32, 52, 71) # цвет фона дисплея - синий

rect_width, rect_height = 100, 200 # ширина и высота прямоугольника
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height / 2 - rect_height / 2
rect_color = pygame.Color('lightyellow') # цвет прямоугольника

STEP = 10 # шаг перемещения

while True: # пустой экран (цикл), по которому бегает курсор мышки. Выход из программы через модуль sys
    for event in pygame.event.get(): # возвращает последовательность событий
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y = rect_y - STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y += STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP:
                rect_x += STEP


    # screen.fill((255, 100, 50))  # изменение цвета дисплея через использование картежа
    # screen.fill(pygame.Color('white')) # изменение цвета дисплея через библиотеку
    # screen.fill((randint(0, 255), randint(0, 255), randint(0, 255))) # изменение цвета дисплея рандомно
    screen.fill(fill_color)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update() # применение изменений

    # clock.tick(1) # скорость изменения фона в секунду (и скорость регистрации движения курсора мыши)