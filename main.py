import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
W, H = 600, 800 # Width and Height of Screen
wall_thickness1 = 10
wall_thickness2 = 5
g = 0.8


# Create the screen
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pinball Game")

# Create Background
def bkg():
    right=pygame.draw.line(screen,'green', (W, H), (W, 200), wall_thickness1) #line right
    top= pygame.draw.arc(screen, 'green', (0-(wall_thickness1/2), 0, W+(wall_thickness1), 400), 0, math.pi, wall_thickness1) # arc top
    left  =pygame.draw.line(screen,'green', (0, H), (0, 200), wall_thickness1) #line left
    bottom  =pygame.draw.line(screen,'green', (0, H), (W, H), wall_thickness1) #line bottom

def inner_bkg():
    right=pygame.draw.line(screen,'green', (W-60, H), (W-60, 200), wall_thickness2) #line right
    top= pygame.draw.arc(screen, 'green', (60-(wall_thickness2/2), 60, 480+wall_thickness2, 280), 0, math.pi/3, wall_thickness2) # arc top_right

def circlerect():
    top_left = pygame.draw.circle(screen, 'blue', (200, 200), 25) #circle top left
    top_right = pygame.draw.circle(screen, 'blue', (350, 180), 25) # circle top right
    middle = pygame.draw.polygon(screen, 'blue', [(250, 250), (300,220),(325,300),(275,350)]) # polygon

def ball():
    first_ball = pygame.draw.circle(screen, 'red', (20, 20), 15) #ball
    

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Update the display
    bkg()
    inner_bkg()
    circlerect()
    ball()
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)