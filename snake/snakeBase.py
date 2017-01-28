
pixel_size = 5
pygame = None
surface = None
def init(pgame,surface_):
    pygame = pgame
    surface = surface_


class Snake:

    color = 0x5555FF

    def __init__(self,start_size,growth,pos):
        self.size = start_size
        self.hind = self
        self.rect = pygame.Rect()
        self.dir = 1
        self.changed = False
        self.pos = pos

    def size_up(self):
        self.hind = Tail(self.hind)
        size += 1

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
        move = 0
        if self.dir % 2: move = 1
        else: move = -1
        if self.dir// 2: pos[1] += move
        else: pos[0] += move
        
    def update(self):
        self.hind.erase()
        move()
        #self.hi
        
    def draw(self):
        pass

class Tail:
    color = 0xFFFFFF
    def __init__(self,ahead):
        self.ahead = ahead
        self.pos = ahead.pos
