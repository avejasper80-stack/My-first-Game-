import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game - Snake")

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

snake = [(100,100)]
food = (random.randint(0,29)*20, random.randint(0,19)*20)
dx, dy = 20, 0

def draw():
    WIN.fill(WHITE)
    for x,y in snake:
        pygame.draw.rect(WIN, GREEN, (x,y,20,20))
    pygame.draw.rect(WIN, RED, (*food,20,20))
    pygame.display.update()

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: dx,dy = -20,0
            if event.key == pygame.K_RIGHT: dx,dy = 20,0
            if event.key == pygame.K_UP: dx,dy = 0,-20
            if event.key == pygame.K_DOWN: dx,dy = 0,20

    head = (snake[0][0]+dx, snake[0][1]+dy)
    snake.insert(0, head)
    if head == food:
        food = (random.randint(0,29)*20, random.randint(0,19)*20)
    else:
        snake.pop()
    draw()

pygame.quit()