import snake.snakeBase as Snake
import pygame

pygame.init()
surface = pygame.display.set_mode((600,700))
Snake.init(pygame,surface)
snake = Snake.Snake(1,0,[50,50])
while True:
    snake.update()
