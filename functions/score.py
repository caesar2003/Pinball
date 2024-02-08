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

#score_written = False
def score(current_score, lives):
    #global score_written
    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Score:{round(current_score)}', True, (237, 178, 106))
    # Textposition
    text_rect = text.get_rect()
    text_rect.center = (width / 2-30, height-20)  
    screen.blit(text, text_rect)
    if lives == 0:
        with open("sonstiges/data.txt", "a") as file:
                file.write(f'{round(current_score)}\n')
                #score_written = True
    elif lives!= 0:
        current_score += 1/60
    for ball in ball_group:
        if ball.ball_coll:
            current_score+=15
            sound.bumpsound()
    return current_score, lives

def new_ball():
    Ball(width-15-25, height-20-70, speed= [0,0])
    #Ball(50, 50, speed= [0,0])

def new_ball_spawn(ball_group, lives):
    ball_coord_death = 700
    if len(ball_group) == 0 and lives==3:
        new_ball()
        sound.new_ball_sound()
        lives = 3
    for ball in ball_group:
        if  (ball.coords.y > height or ball.coords.y < 0 or ball.coords.x < 0 or ball.coords.x > width) and lives == 3:
            new_ball()
            ball.kill()
            sound.new_ball_sound()
            lives = 2
        elif (ball.coords.y > height or ball.coords.y < 0 or ball.coords.x < 0 or ball.coords.x > width) and lives == 2:
            new_ball()
            ball.kill()
            sound.new_ball_sound()
            lives = 1
        elif (ball.coords.y > height or ball.coords.y < 0 or ball.coords.x < 0 or ball.coords.x > width) and lives ==1:
            ball.kill()
            lives = 0

            

    
    font = pygame.font.SysFont(None, 36)
    if lives==1:
        text = font.render(f"{lives} life left", True, (223, 207, 190))
    else:
        text = font.render(f"{lives} lives left", True, (223, 207, 190))
    # Textposition
    text_rect = text.get_rect()
    text_rect.center = (width/2-50, 25)  
    screen.blit(text, text_rect)
    return lives

def highscores():
    try:
        with open('sonstiges/data.txt', "r") as file:
            lines = file.readlines()
            data = [line.strip() for line in lines]  # Strip newline characters and store each line in a list
            data = list(map(int, data))
            data.sort(reverse=True)
            return data[:3]
    except FileNotFoundError:
        print(f"File not found.")
        return None

def write_highscore(highscores):
    i = 1
    a = 15
    for highscore in highscores:
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"{i}. {highscore}", True, (79, 120, 155))
        # Textposition
        text_rect = text.get_rect()
        text_rect.topleft = (20, a)  
        screen.blit(text, text_rect)
        i+=1
        a+=20


