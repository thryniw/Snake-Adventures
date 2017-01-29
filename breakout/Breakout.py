import time
class init:
    def __init__(self,pygame,surface):
        init.pygame = pygame
        init.surface = surface
        class brick(pygame.Rect):
            def __init__(self,pos,durability,brick_size = (40,20)):
                self.size = brick_size
                self.v_durability = durability
                self.colors = [(0,0,0),(255,0,0),(255,102,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130),(140,0,140)]
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
                    init.events.append(Event('generate food'))
                    
        init.events = []
        init.Brick = brick
    def generate_bricks():
        rainbow = []
        dur = 0
        for column in range(0,460,40):
            dur = (dur+1) % 7 + 1
            for row in range(0,7*20,20):
                rainbow.append(init.Brick([column,row],dur))
        return rainbow
        

class Ball:
    def __init__ (self,pos,ball_size,velocity):
        self.size = ball_size
        self.velocity = velocity
        self.screen = (init.surface.get_width(), init.surface.get_height())
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.wait_time = 0.05
        self.reset = time.time()+self.wait_time
        self.pos = pos
        self.score = 0
        
    def draw(self,color):
        self.rect = init.pygame.draw.rect(init.surface,color,(self.pos,self.size))
        
    def move(self):
        for vector in range(len(self.velocity)):
            self.pos[vector] += self.velocity[vector]
            if not (self.size[vector] - self.size[vector] < self.pos[vector] < init.surface.get_size()[vector] - self.size[vector]):
                self.velocity[vector] *= -1
            
    def collide_brick(self,ls,ind):
        brick = ls[ind]
        if (self.rect.left < brick.left < self.rect.right) or (self.rect.left < brick.right < self.rect.right):
            self.velocity[0] *= -1
        if (self.rect.top < brick.top < self.rect.bottom) or (self.rect.top < brick.bottom < self.rect.bottom):
            self.velocity[1] *= -1
            ls[ind].durability(1,ls,ind)
        self.score += brick.v_durability * 10
    
    def collide_tail(self,tail):
        if tail.dir=='h': self.velocity[1] *= -1
        else: self.velocity[0] *= -1
        tail.draw()
    
    def update(self,brick_list,tail_list):
        if(time.time() >= self.reset):
            self.draw(self.black)
            self.move()
            self.draw(self.white)
            brick_index = self.rect.collidelist(brick_list)
            if(brick_index != -1):
                self.collide_brick(brick_list,brick_index)
            tail_index = self.rect.collidelist(tail_list)
            if(tail_index != -1):
                self.collide_tail(tail_list[tail_index])            
            self.reset = time.time()+self.wait_time
    
class Event:
    def __init__(self,description):
        self.description = description
