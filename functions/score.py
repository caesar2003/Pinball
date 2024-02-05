import pygame
import numpy as np

from classes.ball import Ball
from classes.wall import Wall
from classes.circle import Circle
from classes.flipper import Flipper
from classes.shot import Shot
import functions.collisions as col
import functions.general as general
import functions.system as system
from functions.rectangle import rect
from functions.events import event
import functions.sound as sound
import vars.const as const
import vars.setup as setup
from vars.setup import clock
from vars.setup import screen, bg, bg_rect, width, height
from vars.setup import wall_group, ball_group, circle_group, flipper_group, shot_group

score_written = False
def score(current_score, lives):
    global score_written
    font = pygame.font.SysFont(None, 36)
    text = font.render(str(round(current_score)), True, 'RED')
    # Textposition
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 2)  
    screen.blit(text, text_rect)
    if lives == 0 and not score_written:
        with open("data.txt", "a") as file:
                file.write(f'{round(current_score)}\n')
                score_written = True
    elif lives!= 0:
        current_score += 1/60
    return current_score


def new_ball_spawn(ball_group, lives):
    if len(ball_group) == 0:
        Ball(420, 300 , speed= [5,-5])
        lives = 3
    for ball in ball_group:
        if ball.index == 0 and ball.coords.y > 800 and lives == 3:
            Ball(420, 300 , speed= [-1,-5])
            lives = 2
        elif ball.index == 1 and ball.coords.y > 800 and lives == 2:
            Ball(420, 300 , speed= [-1,-5])
            lives = 1
        elif ball.index == 2 and ball.coords.y > 800 and lives ==1:
            lives = 0

            

    
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"{lives} lives left", True, 'RED')
    # Textposition
    text_rect = text.get_rect()
    text_rect.center = (width // 3, height // 2)  
    screen.blit(text, text_rect)
    return lives

def highscores():
    try:
        with open('data.txt', "r") as file:
            lines = file.readlines()
            data = [line.strip() for line in lines]  # Strip newline characters and store each line in a list
            data = list(map(int, data))
            data.sort(reverse=True)
            print(data)
            return data[:3]
    except FileNotFoundError:
        print(f"File not found.")
        return None

def write_highscore(highscores):
    i = 1
    a = 20
    for highscore in highscores:
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"{i}. {highscore}", True, 'RED')
        # Textposition
        text_rect = text.get_rect()
        text_rect.center = (width // 3, a)  
        screen.blit(text, text_rect)
        i+=1
        a+=20


