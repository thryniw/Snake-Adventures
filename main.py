import snake.snakeBase as Snake
import breakout.Breakout as breakout
from pygame.locals import *
import pygame
import time


pygame.init()
surface = pygame.display.set_mode((800,700))
Snake.init(pygame,surface)
snake = Snake.Snake(4,0,[400,550])

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
    if snake.update():
        while not handle_events():
            pass
        break
    pygame.display.update()
    if handle_events(): break;
    time.sleep(0.04)
