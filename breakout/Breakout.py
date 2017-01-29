import time
class init:
    pygame = None
    suface = None
    def __init__(self,pgame,surface):
        init.pygame = pgame
        init.surface = surface

class ball:
    def __init__ (self,pos,ball_size,velocity):
        self.size = ball_size
        self.velocity = velocity
        self.screen = (init.surface.get_width(), init.surface.get_height())
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.wait_time = 0.25
        self.reset = time.time()+self.wait_time
        self.pos = pos
        
    def draw(self,color):
        self.rect = init.pygame.draw.rect(init.surface,color,(self.pos,self.size))
        
    def move(self):
        for vector in range(len(self.velocity)):
            self.pos[vector] += self.velocity[vector]
            if(-self.size[vector] < self.pos[vector] < init.surface.get_width() - self.size[vector]):
                self.velocity[vector] *= -1
            
    def collide(self,brick):
        y_range = (brick.top,brick.bottom)
        x_range = (brick.left,brick.right)
        if (self.rect.left < brick.left < self.rect.right) or (self.rect.left < brick.left < self.rect.right):
            self.velocity[1] *= -1
        if (self.rect.top < brick.top < self.rect.bottom) or (self.rect.top < brick.bottom < self.rect.bottom):
            self.velocity[0] *= -1
                
    def update(self,brick_list,tail_list):
        if(time.time() < self.reset):
            self.draw(self.black)
            self.move()
            self.draw(self.white)
            brick_index = self.rect.collidelist(brick_list)
            if(brick_index != -1):
                self.collide(brick_list[brick_index])
                brick_list[brick_index].durability(1,brick_list)
            tail_index = self.rect.collidelist(tail_list)
            if(tail_index != -1):
                self.collide(tail_list[tail_index])            
            self.reset = time.time()+self.wait_time
    
class brick:
    def __init__(self,brick_size,durability):
        self.size = brick_size
        self.durability = durability
        self.colors = [(0,0,0),(255,0,0),(255,102,0),(255,255,0),(0,255,0),(0,0,255),(230,230,250),(255,240,245)]
        self.color = self.colors[durability]
        
    def draw(self):
        rect = init.pygame.draw.rect(init.surface,self.color,(x,y,self.size))
        
    def durability(decrement,ls,index):
        self.durability -= decrement
        if (self.durability < 1):
            self.color = self.colors[self.durability]
            self.draw()
            del ls[index]
            del self
