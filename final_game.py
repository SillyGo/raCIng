
import pygame
from pygame.locals import *
tela = pygame.display.set_mode((800, 600))
menu_int = pygame.image.load("menu_int.png")
tela.blit(menu_int, (0,0))
pygame.display.update()

while (1):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if (event.type == KEYDOWN and event.key == K_2):
            with open('main2D.py', 'r') as file:
                code = file.read()
                exec(code)
        if (event.type == KEYDOWN and event.key == K_3):
            with open("main3D.py", "r") as file:
                code = file.read()
                exec(code)