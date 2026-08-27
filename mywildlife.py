import pygame
pygame.init()
screenwidth = 500
screenheight = 500
displaysurface = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Wildlife Information Display")
background_image =pygame.transform.scale(pygame.image.load("background.png").convert(),(screenwidth, screenheight))
wildlifeimage = pygame.transform.scale(
    pygame.image.load("tiger.png").convert_alpha(),
    (220, 220))
wildlife_rect = wildlifeimage.get_rect(
    center=(screenwidth,screenheight // 2 - 30))
headingfont = pygame.font.Font(None, 42)
factfont = pygame.font.Font(None, 28)
headingtext = headingfont.render("Wildlife Spotlight: Tiger",True,pygame.Color("black"))
heading_rect = headingtext.get_rect(
center=(screenwidth // 2, 45))


facttext = factfont.render("Tigers are powerful wild cats.",True, pygame.Color("black"))

fact_rect = facttext.get_rect(center=(screenwidth // 2, 420))

 
def gameloop():
    clock = pygame.time.Clock()
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
        
        displaysurface.blit(
            background_image,
            (0, 0)
        )
 
        
        displaysurface.blit(
            wildlifeimage,
            wildlife_rect
        )
 
        
        displaysurface.blit(
            headingtext,
            heading_rect
        )
 
        displaysurface.blit(
            facttext,
            fact_rect
        )
 
        
        pygame.display.flip()
 
        
        clock.tick(30)
 
    pygame.quit()
if __name__ == "__main__":
    gameloop()
