import pygame
import time
from pygame.locals import *
from sys import exit

pygame.init()

def printscores(WINDOW_WIDTH, WINDOW_HEIGHT,HIGHSCORE_label_nomes,HIGHSCORE_label_pontos):
    tela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    tela.fill((0, 0, 0,))
    posicao = 0
    contador=0
    print_y=200
    print_yp=200
    fontebase = pygame.font.Font('Oxanium-Bold.ttf', 40)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == K_m:
                    return True
                    break
        if contador == 0:
            for i in HIGHSCORE_label_nomes:
                posicao += 1
                nomes = fontebase.render(f"{posicao}° - {i}", False, (255, 255, 255))
                tela.blit(nomes, (60, print_y))
                print_y+=60
            for h in HIGHSCORE_label_pontos:
                pontos = fontebase.render(f"{h}", False, (255, 255, 255))
                tela.blit(pontos, (600, print_yp))
                print_yp += 60
            contador+=1
            texto = ''
            texto = fontebase.render("Aperte M para voltar", False, (255, 255, 255))
            tela.blit(texto, (200, 520))
            logo = pygame.image.load('files/images/logo.png')
            logo = pygame.transform.scale(logo, (400, 150))
            tela.blit(logo, (200, 20))
            pygame.display.update()
