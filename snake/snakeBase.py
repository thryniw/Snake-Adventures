from collections import deque
from time import time
pixel_size = 5
pixel = (pixel_size,pixel_size)

def init(pgame,surface_):
    Snake.pygame = pgame
    Snake.surface = surface_
    print('pygame initialised')


class Snake:

    color = 0x5555FF
    pygame = None
    surface = None
    def __init__(self,start_size,growth,pos):
        self.tail = deque()
        self.dir = 1
        self.changed = False
        self.pos = pos
        self.wait_time = 0.5
        self.refresh = time() + self.wait_time
        while len(self.tail) < start_size:
            self.size_up()

    def size_up(self):
        self.tail.append(Tail(self.pos))

    def left(self):
        if not self.changed:
            self.dir = 1
            self.changed = True

    def right(self):
        if not self.changed:
            self.dir = 0
            self.changed = True

    def up(self):
        if not self.changed:
            self.dir = 3
            self.changed = True

    def down(self):
        if not self.changed:
            self.dir = 2
            self.changed = True

    def __move(self):
        move = pixel_size
        if self.dir % 2: pass  # move *=1
        else: move *= -1
        if self.dir// 2: pos[1] += move
        else: self.pos[0] += move
        
    def update(self):
        if time() >= self.refresh:
            self.tail[-1].erase()
            self.tail.pop()
            self.tail.appendleft(Tail(self.pos))
            self.tail[0].draw()
            self.__move()
            self.__draw()
            self.refresh = time() + self.wait_time
        #self.hi
        
    def __draw(self):
        self.pygame.draw.rect(Snake.surface,self.color, self.pygame.Rect(pos,pixel))

class Tail:
    color = 0xFFFFFF
    def __init__(self,pos):
        self.pos = pos
        
    def erase(self):
        Snake.pygame.draw.rect(Snake.surface,0x000000, Snake.pygame.Rect(self.pos,pixel))
        
    def draw(self):
        Snake.pygame.draw.rect(Snake.surface,self.color, Snake.pygame.Rect(self.pos,pixel))
