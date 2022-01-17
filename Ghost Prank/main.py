import pygame
from time import sleep

pygame.init()
pygame.mixer.init()


# Create windows
windows = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.music.load('soothing.mp3')
pygame.mixer.music.play()

sleep(5)

pygame.mixer.music.load("scary.mp3")
pygame.mixer.music.play()

image = pygame.image.load("ghost.jpg")
windows.blit(image, (0,0))
pygame.display.update()
sleep(5)