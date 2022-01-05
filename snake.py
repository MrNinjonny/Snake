import pygame
import random

pygame.init()

window_width = 800
window_height = 600
window_size = (window_width, window_height)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 00)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 50)
large_font = pygame.font.SysFont("comicsansms", 80)
img = pygame.image.load('.\\pics\\snake head.png')

def snake(snake_list, block_size, direction):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    screen.blit(head, (snake_list[-1][0], snake_list[-1][1]))
    for XnY in snake_list[:-1]:
        pygame.draw.rect(screen, green, [XnY[0], XnY[1], block_size, block_size])

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False

        screen.fill (white)
        massage_to_screen("Welcome to Snake", green, -100, size="large")
        massage_to_screen("The objective of the game is to eat red apples", black, -30)
        massage_to_screen("The apples you eat, The longer you get", black, 10)
        massage_to_screen("If you run in to yourself, You die!", black, 50)
        massage_to_screen("Press C to play or Q to Quit", red , 180)
        pygame.display.update()
        clock.tick(15)

def text_objects(text, color, size):
    if size == "small":
        text_surface = small_font.render(text, True, color)
    elif size == "medium":
        text_surface = med_font.render(text, True, color)
    elif size == "large":
        text_surface = large_font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def massage_to_screen(msg, color, y_change = 0, size = "small"):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (window_width / 2), (window_height / 2) + y_change
    screen.blit(text_surf, text_rect)


def game_loop():
    game_exit = False
    game_over = False
    difficulty = 10
    block_size = 20
    apple_thickness = 30
    direction = "right"

    head_x = window_width / 2
    head_y = window_height / 2
    head_x_change = block_size
    head_y_change = 0

    snake_list = []
    snake_length = 1

    rand_apple_x = round(random.randrange(0, window_width - apple_thickness) / block_size) * block_size
    rand_apple_y = round(random.randrange(0, window_height - apple_thickness) / block_size) * block_size

    while not game_exit:
        while game_over:
            screen.fill(white)
            massage_to_screen("Game Over", red, y_change= -50, size = "large")
            massage_to_screen("Press C to play again or Q to quit", green, 50, size = "medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    head_x_change = -block_size
                    head_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    head_x_change = block_size
                    head_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    head_y_change = -block_size
                    head_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    head_y_change = block_size
                    head_x_change = 0
                    direction = "down"

        if head_x > window_width:
            head_x = -block_size
        elif head_x < 0:
            head_x = window_width
        elif head_y > window_height:
            head_y = -block_size
        elif head_y < 0:
            head_y = window_height

        head_x += head_x_change
        head_y += head_y_change

        screen.fill(white)
        pygame.draw.rect(screen, red, [rand_apple_x, rand_apple_y, apple_thickness, apple_thickness])

        snake_head = [head_x, head_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for XnY in snake_list[:-1]:
            if XnY == snake_head:
                game_over = True

        snake(snake_list, block_size, direction)
        pygame.display.update()

        if rand_apple_x < head_x < rand_apple_x + apple_thickness or rand_apple_x < head_x + block_size < rand_apple_x + apple_thickness:
            if rand_apple_y < head_y < rand_apple_y + apple_thickness or rand_apple_y < head_y + block_size < rand_apple_y + apple_thickness:
                rand_apple_x = round(random.randrange(0, window_width - apple_thickness) / block_size) * block_size
                rand_apple_y = round(random.randrange(0, window_height - apple_thickness) / block_size) * block_size
                snake_length += 1

        clock.tick(difficulty)

    pygame.quit()
    quit()

game_intro()
game_loop()