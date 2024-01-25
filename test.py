import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball and Wall Collision")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_pos = [width // 2, height // 2]
ball_speed = [5, 2]

# Wall properties
wall_pos = [200, 200]
wall_size = [400, 200]

clock = pygame.time.Clock()

def check_collision(ball_pos, ball_radius, wall_pos, wall_size):
    ball_left = ball_pos[0] - ball_radius
    ball_right = ball_pos[0] + ball_radius
    ball_top = ball_pos[1] - ball_radius
    ball_bottom = ball_pos[1] + ball_radius

    wall_left, wall_top = wall_pos
    wall_right = wall_pos[0] + wall_size[0]
    wall_bottom = wall_pos[1] + wall_size[1]

    return not (ball_right < wall_left or ball_left > wall_right or
                ball_bottom < wall_top or ball_top > wall_bottom)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check for collision with the wall
    if check_collision(ball_pos, ball_radius, wall_pos, wall_size):
        # Collision detected, reverse the direction of the ball
        ball_speed[0] = -ball_speed[0]
        ball_speed[1] = -ball_speed[1]

    # Clear the screen
    screen.fill(black)

    # Draw the wall
    pygame.draw.rect(screen, white, (wall_pos[0], wall_pos[1], wall_size[0], wall_size[1]))

    # Draw the ball
    pygame.draw.circle(screen, red, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
