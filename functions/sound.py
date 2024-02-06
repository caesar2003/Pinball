import pygame
def moneyboy():
    ball_sound = pygame.mixer.Sound("music/MoneyBoy.wav")
    ball_sound.set_volume(1.0)
    ball_sound.play()
def drehden():
    ball_sound = pygame.mixer.Sound("music/DrehdenSwagauf.wav")
    ball_sound.set_volume(1.0)
    ball_sound.play()
def background_music():
    ball_sound = pygame.mixer.Sound("music/backgroundmusic.mp3")
    ball_sound.set_volume(0.04)
    ball_sound.play()
def new_ball_sound():
    ball_sound = pygame.mixer.Sound("music/neuerBall.wav")
    ball_sound.set_volume(0.04)
    ball_sound.play()
def bumpsound():
    ball_sound = pygame.mixer.Sound("music/bumpsound.wav")
    ball_sound.set_volume(0.04)
    ball_sound.play()