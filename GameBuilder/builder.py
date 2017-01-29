import math,time
class init:
    def __init__(self,pgame,surface,brick_types):
        init.pygame = pgame
        init.surface = surface
        init.width = surface.get_width()
        init.height = surface.get_height()
        init.bricks = brick_types
        init.brick_width = brick_types[0].get_size[0]
        
class Brick_Origin:
    def __init__(self,pos,color,size):
        self.copies = []
        self.size = size
        self.color = color
        self.pos = pos
        wait_time = 0.1
        self.reset = time.time() + self.wait_time        
        
    def draw(self):
        self.rect = init.pygame.draw.rect(init.surface,self.color,(self.origin_pos,self.size))
    
    def update(self):
        if(time.time() >= self.reset):
            draw()
            
            self.reset = time.time()+self.wait_time            
    
    def handle_mouse_down(self,pos):
        
        for brick in self.bricks:
            if (brick.collidepoint(pos)):
                drag_brick()
                
                brick.update()    
    
class Copy:
    def __init__(self,pos,size,color):
        self.origin_pos = pos
        self.color = color
        self.size = size
        self.rate = 3        
        wait_time = 0.02
        self.reset = time.time() + self.wait_time
        
    def handle_mouse_down(self,pos):
        for brick in self.bricks:
            if (brick.collidepoint(pos)):
                drag_brick()
                self.update()     
    
    def illegal_position(self):
        while(not(-3 < distance < 3)):
            distance = hypo()
            for axis in range(2):
                self.pos[axis] += velocity[axis]
            self.draw()
        self.erase()
    
    def hypo(self):
        delta = (origin[brick].x - self.pos[0],origin[brick].y - self.pos[1])
        distance = math.sqrt(delta_x**2 + delta_y**2)
        for i in range(2):
            self.velocity[i] = self.rate * delta[i] / distance
        return distance
