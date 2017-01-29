from collections import deque
from time import time
pixel_size = 10
pixel = (pixel_size,pixel_size)



class init:
    
    def __init__(self,pygame,surface):
        init.pygame = pygame
        init.surface = surface
        class Tail(pygame.Rect):
            color = 0xFFFFFF
            def __init__(self,pos,direction):
                self.pos = pos
                self.x = pos[0]
                self.y = pos[1]
                self.size = pixel
                self.dir = direction
                
            def erase(self):
                init.pygame.draw.rect(init.surface,0x000000, self)
                
            def draw(self):
                init.pygame.draw.rect(init.surface,self.color, self)
        init.Tail = Tail 

class Snake:

    color = 0x5555FF
    def __init__(self,start_size,growth,pos):
        self.tail = deque()
        self.dir = 1
        self.changed = False
        self.pos = pos
        self.wait_time = 0.2
        self.refresh = time() + self.wait_time
        while len(self.tail) < start_size:
            self.size_up()

    def size_up(self):
        if self.dir == 1 or self.dir == 0:
            direct = 'h'
        else: direct = 'v'
        self.tail.append(init.Tail(self.pos,direct))

    def left(self):
        if not self.changed and self.dir != 1:
            self.dir = 0
            self.changed = True

    def right(self):
        if not self.changed and self.dir != 0:
            self.dir = 1
            self.changed = True

    def up(self):
        if not self.changed and self.dir != 3:
            self.dir = 2
            self.changed = True

    def down(self):
        if not self.changed and self.dir != 2:
            self.dir = 3
            self.changed = True

    def __move(self):
        move = pixel_size
        if self.dir % 2: pass  # move *=1
        else: move *= -1
        if self.dir// 2: self.pos[1] += move
        else: self.pos[0] += move
        self.changed = False
        
    def update(self,brick_list):
        if time() >= self.refresh:
            if self.dir == 1 or self.dir == 0:
                direct = 'h'
            else: direct = 'v'    
            self.tail[-1].erase()
            self.tail.pop()
            self.tail.appendleft(init.Tail(self.pos,direct))
            self.tail[0].draw()
            self.__move()
            self.__draw()
            self.refresh = time() + self.wait_time
            if init.pygame.Rect(self.pos,pixel).collidelist(self.tail) != -1:
                return True
            for axis in range(2):
                if not (-pixel_size < self.pos[axis] < init.surface.get_size()[axis]):
                    return True
            if init.pygame.Rect(self.pos,pixel).collidelist(brick_list) != -1: return True
                    
    def __eat(self,food_list):
        index = init.pygame.Rect(self.pos,pixel).collidelist(self.tail)
        if index != -1:
            del food_list[index]
            self.size_up()
        
    def __draw(self):
        init.pygame.draw.rect(init.surface,self.color, init.pygame.Rect(self.pos,pixel))
