import pygame
from pathlib import Path

# Initialize PyGame
pygame.init()

# Initial window size
s_width = 600
s_height = 800

# Define spacetime 
GRAVITY = [0.,0.3] # x-y direction
DT = 1 # ms (discretization of time) 

# Making display screen
screen = pygame.display.set_mode((s_width, s_height), pygame.RESIZABLE)
bg_orig=pygame.image.load(Path(__file__).parents[0] / Path("bkg.jpg")).convert()
clock = pygame.time.Clock()

# Setup 
running = True

# You could declare components (the initial ball, the other items, ...) here




# Main event loop
while running:
    for event in pygame.event.get():
        # Get's all the user action (keyboard, mouse, joysticks, ...)
        continue

    # Adjust screen
    s_width, s_height = screen.get_width(), screen.get_height()
    bg = pygame.transform.scale(bg_orig, (s_width, s_height))
    screen.blit(bg, (0, 0)) # redraws background image


    # Here the action could take place


    pygame.display.flip() # Update the display of the full screen
    clock.tick(60) # 60 frames per second

# Done! Time to quit.
