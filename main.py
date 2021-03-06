import snake.snakeBase as Snake
import breakout.Breakout as breakout
from pygame.locals import *
import pygame
import time
import writing

pygame.display.init()
surface = pygame.display.set_mode((500,400))
pygame.display.set_caption('snake_breakout')
Snake.init(pygame,surface)
breakout.init(pygame,surface)
writing.init(pygame,surface)
brick_list = breakout.init.generate_bricks()

snake = Snake.Snake(12,0,[250,200])
ball = breakout.Ball([250,250],(10,10),[-3,-3])

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
    if  ball.update(brick_list,snake.tail) or snake.update(brick_list):
        while not handle_events():
            writing.print_loss()
            pygame.display.update()
        break
    for event in breakout.init.events:
        Snake.generate_food()
        ball.wait_time -= 0.002
    breakout.init.events.clear()
    writing.print_score(str(ball.score))
    pygame.display.update()
    if len(brick_list) == 0:
        while not handle_events():
            writing.print_win()
            pygame.display.update()
        break
    if handle_events(): break;
    time.sleep(0.04)
pygame.display.quit()
