import time
class init:
    def __init__(self,pygame,surface):
        init.pygame = pygame
        init.surface = surface
        class brick(pygame.Rect):
            def __init__(self,pos,durability,brick_size = (20,10)):
                self.size = brick_size
                self.v_durability = durability
                self.colors = [(0,0,0),(255,0,0),(255,102,0),(255,255,0),(0,255,0),(0,0,255),(230,230,250),(255,240,245)]
                self.color = self.colors[durability]
                self.pos = pos
                self.x = pos[0]
                self.y = pos[1]
                self.size
                self.draw()
                
            def draw(self):
                rect = init.pygame.draw.rect(init.surface,self.color,(self.pos,self.size))
                
            def durability(self,decrement,ls,index):
                self.v_durability -= decrement
                self.color = self.colors[self.v_durability]
                self.draw()
                if (self.v_durability < 1):
                    del ls[index]
                    del self

        init.Brick = brick
    def generate_bricks():
        #meant to read a file that maps the list
        return [init.Brick([50,50],1),init.Brick([70,50],2),init.Brick([90,50],3),init.Brick([110,50],4),init.Brick([50,60],7)]
        

class Ball:
    def __init__ (self,pos,ball_size,velocity):
        self.size = ball_size
        self.velocity = velocity
        self.screen = (init.surface.get_width(), init.surface.get_height())
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.wait_time = 0.01
        self.reset = time.time()+self.wait_time
        self.pos = pos
        
    def draw(self,color):
        self.rect = init.pygame.draw.rect(init.surface,color,(self.pos,self.size))
        
    def move(self):
        for vector in range(len(self.velocity)):
            self.pos[vector] += self.velocity[vector]
            if not (self.size[vector] - self.size[vector] < self.pos[vector] < init.surface.get_size()[vector] - self.size[vector]):
                self.velocity[vector] *= -1
            
    def collide(self,brick):
        y_range = (brick.top,brick.bottom)
        x_range = (brick.left,brick.right)
        if (self.rect.left < brick.left < self.rect.right) or (self.rect.left < brick.left < self.rect.right):
            self.velocity[0] *= -1
        if (self.rect.top < brick.top < self.rect.bottom) or (self.rect.top < brick.bottom < self.rect.bottom):
            self.velocity[1] *= -1
                
    def update(self,brick_list,tail_list):
        if(time.time() >= self.reset):
            self.draw(self.black)
            self.move()
            self.draw(self.white)
            brick_index = self.rect.collidelist(brick_list)
            if(brick_index != -1):
                self.collide(brick_list[brick_index])
                brick_list[brick_index].durability(1,brick_list,brick_index)
            tail_index = self.rect.collidelist(tail_list)
            if(tail_index != -1):
                self.collide(tail_list[tail_index])            
            self.reset = time.time()+self.wait_time
    

