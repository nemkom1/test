import pygame, sys, random

width = 900
height = 800
FPS = 10
size = 20  # размер змеи

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

up = (0, -1)  # по х не изменяется, по у движется против оси
down = (0, 1)  # по х не изменяется, по у движется вдоль оси
left = (-1, 0)  # по у не изменяется, по х движется против оси
right = (1, 0)  # по у не изменяется, по х движется вдоль оси

speed = 10

pygame.init()

sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def add_part_of_snake(snake, snake_tail, head):
    update = [-size * x for x in head]
    if len(snake_tail) == 0:
        snake_tail.append(snake.move(update[0], update[1]))
    else:
        snake_tail.append(snake_tail[len(snake_tail)-1].move(update[0], update[1]))

def draw_snake(snake, snake_tail, head):
    tmp = snake.move(0,0)
    head_speed = [speed * x for x in head]
    snake.move_ip(head_speed[0], head_speed[1])
    pygame.draw.rect(sc, green, snake)
    if len(snake_tail) == 0:
        return
    pygame.draw.rect(sc, black, snake_tail[len(snake_tail)-1])
    for i in range(0, len(snake_tail) - 1):
        snake_tail[len(snake_tail) - 1 - i] = snake_tail[len(snake_tail) - 2 - i]
        pygame.draw.rect(sc, green, snake_tail[len(snake_tail) - 1 - i])
    snake_tail[0] = tmp
    pygame.draw.rect(sc, green, snake_tail[0])

def make_new_apple():
    apple_x = random.randint(0, width - size)
    apple_y = random.randint(0, height - size)
    apple = pygame.Rect(apple_x, apple_y, size, size)
    return apple

def finish():
    pygame.quit()
    sys.exit()


def main():
    snake = pygame.Rect(width / 2, height / 2, size, size)
    head = up
    apple = make_new_apple()
    snake_tail = []

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                finish()

            if event.type == pygame.KEYDOWN:  # если клавиша нажата
                if event.key == pygame.K_LEFT and head != right:  # если нажата именно стрелочка влево
                    head = left

                if event.key == pygame.K_RIGHT and head != left:  # если нажата именно стрелочка вправо
                    head = right

                if event.key == pygame.K_UP and head != down:  # если нажата именно стрелочка вверх
                    head = up

                if event.key == pygame.K_DOWN and head != up:  # если нажата именно стрелочка вниз
                    head = down

                if event.key == pygame.K_w and head != down:
                    head = up

                if event.key == pygame.K_d and head != left:
                    head = right

                if event.key == pygame.K_a and head != right:
                    head = left

                if event.key == pygame.K_s and head != up:
                    head = down

        if snake.bottom > height or snake.top < 0 or snake.left < 0 or snake.right > width:
            return  # нас выбросит из функции

        if snake.colliderect(apple):
            add_part_of_snake(snake, snake_tail, head)
            apple = make_new_apple()
        if len(snake_tail) != 0 and snake.collidelist(snake_tail) != -1:
            return



        sc.fill(black)
        draw_snake(snake, snake_tail, head)
        snake_head = [speed * x for x in head]
        snake.move_ip(snake_head[0], snake_head[1])
        pygame.draw.rect(sc, green, snake)
        pygame.draw.rect(sc, red, apple)
        clock.tick(FPS)
        pygame.display.update()


main()