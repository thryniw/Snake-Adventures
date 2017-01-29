
class init:
    def __init__(self,pygame,surface):
        pygame.font.init()
        init.pygame = pygame
        init.surface = surface
    def font(f_size):
        font =  init.pygame.font.SysFont(None, f_size)
        return font


def print_score(score):
    font = init.font(24)
    text_image = font.render(str(score), True, (255,255,255,255))
    init.pygame.draw.rect(init.surface,(0,0,0,255),init.pygame.Rect((init.surface.get_width()-text_image.get_width(),0),text_image.get_size()))
    init.surface.blit(text_image, (init.surface.get_width()-text_image.get_width(),0))
    
def print_win():
    green = (0,255,0,255)
    text_image_top = init.font(30).render("YOU",True,green)
    text_image_bottom = init.font(30).render("WIN",True,green)
    init.surface.blit(text_image_top,((init.surface.get_width()-text_image_top.get_width())//2,init.surface.get_height()//2-text_image_top.get_height()))
    init.surface.blit(text_image_bottom,((init.surface.get_width()-text_image_bottom.get_width())//2,init.surface.get_height()//2))
def print_loss():
    red = (255,0,0,255)
    font = init.font(30)
    text_image_top = font.render("YOU",True,red)
    text_image_bottom = font.render("LOST",True,red)
    init.surface.blit(text_image_top,((init.surface.get_width()-text_image_top.get_width())//2,init.surface.get_height()//2-text_image_top.get_height()))
    init.surface.blit(text_image_bottom,((init.surface.get_width()-text_image_bottom.get_width())//2,init.surface.get_height()//2))
    
