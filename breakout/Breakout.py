import time
class init:
    pygame = None
    suface = None
    def __init__(self,pgame,surface):
        init.pygame = pgame
        init.surface = surface

class ball:
    def __init__ (self,ball_size,velocity):
        self.size = ball_size
        self.velocity = velocity
        self.screen = (init.surface.get_width(), init.surface.get_height())
        self.white = (155,155,155)
        self.black = (0,0,0)
        self.wait_time = 0.02
        self.reset = time.time()+self.wait_time
        
    def draw(self,color):
        self.rect = init.pygame.draw.rect(init.surface,color,(self.pos,self.size))
        
    def move(self):
        for vector in range(len(self.velocity)):
            self.pos[vector] += velocity[vector]
        if (self.rect.top < 0):
            velocity[1] *= -1
        if (self.rect.left < 0 or self.rect.right > self.screen[0]):
            velocity[0] *= -1
            
    def collide(self,brick):
        y_range = (brick.top,brick.bottom)
        x_range = (brick.left,brick.right)
        if (self.rect.collidepoint(brick.top,range(x_range)) or self.rect.collidepoint(brick.bottom,range(x_range))):
            velocity[1] *= -1
        if (self.rect.collidepoint(brick.left,range(y_range)) or self.rect.collidepoint(brick.bottom,range(y_range))):
            velocity[0] *= -1
                
    def update(self,brick_list,tail_list):
        if(time.time() < reset):
            self.draw(self.black)
            self.move()
            brick_index = self.rect.collidelist(brick_list)
            if(brick_index != -1):
                self.collide(brick_list[brick_index])
                brick_list[brick_index].durbility(1)
            tail_index = self.rect.collidelist(tail_list)
            if(tail_index != -1):
                self.collide(tail_list[tail_index])            
            self.reset = time.time()+self.wait_time
    
class brick:
    def __init__(self,brick_size,durability):
        self.size = brick_size
        self.durability = durability
        self.colors = [(255,0,0),(255,102,0),(255,255,0),(0,255,0),(0,0,255),(230,230,250),(255,240,245)]
        self.color = self.colors[durability-1]
        
    def draw(self):
        rect = init.pygame.draw.rect(init.surface,self.color,(x,y,self.size)