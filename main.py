import snake.snakeBase as Snake
import breakout.Breakout as breakout
from pygame.locals import *
import pygame



pygame.init()
surface = pygame.display.set_mode((800,700))
Snake.init(pygame,surface)
snake = Snake.Snake(3,0,[50,50])

def handle_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
        if event.type == KEYDOWN:
            if event.key == K_UP:
                snake.up()
            elif event.key == K_DOWN:
                snake.down()
            elif event.key == K_LEFT:
                snake.left()
            elif event.key == K_RIGHT:
                snake.right()

while True:
    snake.update()
    pygame.display.update()
    if handle_events(): break;
