import pygame
from pygame.locals import *
import numpy as np

def movement(x, y, rot, keys, counter4, counter5, counterOleo, item_spawn, velocidade, tick, diamante, ferro, coisa, pontuação, invisivel, highscore, highscore_name):
    esquerda = False
    p_mouse = pygame.mouse.get_rel()
    rot = rot + np.clip((p_mouse[0])/200, -0.0015, .0015)*tick
    efeito = -1
    if keys[pygame.K_p] and (not item_spawn):
        if diamante:
            efeito = 0
        elif ferro:
            efeito = 1
            velocidade = velocidade * 2
        elif coisa:
            efeito = 2
        item_spawn = True
    if keys[pygame.K_LEFT] or keys[ord("a")]:
        rot = rot - 0.0015*tick
        counter4 = counter4 + 1
        counter5 = 0
    if keys[pygame.K_LEFT] or keys[ord("d")]:
        rot = rot + 0.0015*tick
        esquerda = True
        counter4 = 0
    if (not (keys[pygame.K_LEFT] or keys[ord("d")])) and (not (keys[pygame.K_LEFT] or keys[ord("a")])):
        counter4 = 0
        counter5 = 0
    x, y = x + tick*velocidade*np.cos(rot), y + tick*velocidade*np.sin(rot)
    if counterOleo < 20 and not invisivel:
        rot = rot + 0.01*tick
        x, y = x + velocidade*np.cos(rot)*tick, y + velocidade*np.sin(rot)*tick
    counterOleo = counterOleo + 1
    orientation = rot/(abs(rot))
    new_value = (abs(rot))%(2*np.pi)
    rot = new_value*orientation
    return x, y, rot, counter4, esquerda, counterOleo, item_spawn, efeito