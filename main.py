import pygame
from pathlib import Path

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((500,700))
pygame.display.set_caption('Pinball ')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)
running = True

test_surface = pygame.Surface((100,200))
test_surface.fill('Red')
pic_surface = pygame.image.load('bkg2.jpg').convert_alpha()
text_surface = test_font.render('Test', True, 'Green' )
x_pos = 0

# Main event loop
while True:
    
####################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
########################################
    if running:
        screen.blit(pic_surface, (0,0))
        x_pos +=1
        screen.blit(test_surface, (x_pos,100))
        screen.blit(text_surface, (100,100))
        pygame.draw.circle(screen, 'blue', (10,10), 10)
    else:
       screen.blit(pic_surface, (0,0))     
    pygame.display.update()
    clock.tick(60)
   