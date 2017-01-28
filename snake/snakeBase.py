
pixel_size = 5
pygame = None
surface = None
def init(pgame,surface_):
    pygame = pgame
    surface = surface_


class Snake:

    
    def __init__(self,start_size,growth):
        self.size = start_size
        self.hind = self
        self.rect = pygame.Rect()
        self.dir = 1
        self.changed = False
    
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
        
    def up(self)
        if not self.changed:
            self.dir = 3
            self.changed = True
        
    def down(self):
        if not self.changed:
            self.dir = 2
            self.changed = True

class Tail:
    def __init__(self,ahead):
        self.ahead = ahead
        self.pos = ahead.pos
