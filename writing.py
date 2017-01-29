
class init:
    def __init__(self,pygame,surface):
        
        init.pygame = pygame
        init.surface = surface
    def font(f_size):
        return init.pygame.font.SysFont(None, font_size, True)


def print_score(score):
    text_image = init.font(12).render(str(score), True, 0xFFFFFF)
    init.surface.blit(text_image, (surface.get_witdth()-text_image.get_width(),0))
    
def print_win():
    green = 0x00FF00
    text_image_top = init.font(30).render("YOU",True,green)
    Text_image_bottom = init.font(30).render("WIN",True,green)
    init.surface.blit(text_image_top,(surface.get_height()/2-text_image_top.get_height(),(surface.get_witdth()-text_image_top.get_width())/2))
    init.surface.blit(text_image_bottom,(surface.get_height()/2-text_image_bottom.get_height(),(surface.get_witdth()-text_image_bottom.get_width())/2))
    
def print_loss():
    red = 0xFF0000
    text_image_top = init.font(30).render("YOU",True,red)
    Text_image_bottom = init.font(30).render("WIN",True,red)
    init.surface.blit(text_image_top,(surface.get_height()/2-text_image_top.get_height(),(surface.get_witdth()-text_image_top.get_width())/2))
    init.surface.blit(text_image_bottom,(surface.get_height()/2-text_image_bottom.get_height(),(surface.get_witdth()-text_image_bottom.get_width())/2))
