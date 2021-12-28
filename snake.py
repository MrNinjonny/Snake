import pygame
import random
pygame.init()

window_width = 800
window_height = 600
window_size = (window_width, window_height)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)


def massage_to_screnn(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [window_width / 2, window_height / 2])


def game_loop():
    game_exit = False
    game_over = False
    difficulty = 10
    block_size = 20

    head_x = window_width / 2
    head_y = window_height / 2
    head_x_change = 0
    head_y_change = 0

    rand_apple_x = round(random.randrange(0, window_width - block_size)/block_size) * block_size
    rand_apple_y = round(random.randrange(0, window_height - block_size)/block_size) * block_size
    
    while not game_exit:
        while game_over:
            screen.fill(white)
            massage_to_screnn("Game Over, press C to play again or Q to quit", red)
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
                elif event.key == pygame.K_RIGHT:
                    head_x_change = block_size
                    head_y_change = 0
                elif event.key == pygame.K_UP:
                    head_y_change = -block_size
                    head_x_change = 0
                elif event.key == pygame.K_DOWN:
                    head_y_change = block_size
                    head_x_change = 0

        if head_x >= window_width:
            head_x = 0
        elif head_x < 0:
            head_x = window_width - 1
        elif head_y >= window_height:
            head_y = 0
        elif head_y < 0:
            head_y = window_height - 1

        head_x += head_x_change
        head_y += head_y_change

        screen.fill(white)
        pygame.draw.rect(screen, red, [rand_apple_x, rand_apple_y, block_size, block_size])
        pygame.draw.rect(screen, black, [head_x, head_y, block_size, block_size])
        pygame.display.update()

        if head_x == rand_apple_x and head_y == rand_apple_y:
            print("eat")

        clock.tick(difficulty)

    pygame.quit()
    quit()

game_loop()
