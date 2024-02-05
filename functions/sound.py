import pygame
def ball_spawn_sound():
    ball_sound = pygame.mixer.Sound("ball_respawn_sound.mp3")
    ball_sound.set_volume(0.5)
    ball_sound.play()
def moneyboy():
    ball_sound = pygame.mixer.Sound("MoneyBoy.wav")
    ball_sound.set_volume(1.0)
    ball_sound.play()
def drehden():
    ball_sound = pygame.mixer.Sound("DrehdenSwagauf.wav")
    ball_sound.set_volume(1.0)
    ball_sound.play()