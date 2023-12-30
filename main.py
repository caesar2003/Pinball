import pygame
from pathlib import Path

# Initialize PyGame
pygame.init()
screen_width = 600
screen_height= 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pinball')
clock = pygame.time.Clock()
running = True
screen.fill('blue')
####################################################################
ball_radius = 20
ball_x = 25
ball_y = 25
ball_vx = 10
ball_vy = 20
g = 0.3
dt = 0.5



# Main event loop
while running:
    
####################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
########################################
    screen.fill('blue')
    ball_vy = ball_vy + g * dt
    ball_vx = ball_vx
    if ball_y + ball_radius>= screen.get_height():
        ball_vy = ball_vy * (-1)
    if ball_y - ball_radius<= 0:
         ball_vy = ball_vy * (-1)
    if ball_x+ball_radius >= screen.get_width():
        ball_vx = ball_vx * (-1)
    if ball_x - ball_radius<= 0:
        ball_vx = ball_vx * (-1)
    ball_y = ball_y + ball_vy * dt + 0.5 * g *dt**2
    ball_x = ball_x + ball_vx *dt
    pygame.draw.circle(screen, 'green', (ball_x,ball_y), ball_radius)
    pygame.display.update()
    clock.tick(60)
   