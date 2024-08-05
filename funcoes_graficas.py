import pygame
import numpy as np
from numba import njit
import time
from random import randint
import scores
import printscores


@njit
def item_coordinate_generator(floor):
    x, y = randint(5, 96), randint(5, 96)
    xx, yy = int(x/100%1*1024), int(y/100%1*1024)
    color = (floor[xx][yy])*255
    R, G, B = int(color[0]), int(color[1]), int(color[2])
    if R == 96 and G == 96 and B == 96:
        return (x, y)
    else:
        return item_coordinate_generator(floor)
    
def explosion_of_death(tela,surf, pontuacão, boom0, boom1, boom2):
    tela.blit(boom0, (120, 360))
    pygame.display.update()
    time.sleep(0.2)
    tela.blit(surf, (0,0))  
    tela.blit(boom1, (120, 200))
    pygame.display.update()
    time.sleep(0.4)
    tela.blit(surf, (0,0))  
    tela.blit(boom2, (120, 200))
    pygame.display.update()
    time.sleep(0.6)
    print(pontuacão)
    return True

@njit
def draw_floor(x:float,y:float, halfvres:float, frame, i:int, j:int, floor, posx:float, posy:float):
    xx, yy = int(x/100%1*1024), int(y/100%1*1024)
    frame[i][halfvres*2 - j - 1] = floor[xx][yy]
    tideX, tideY = int(posx/100%1*1024), int(posy/100%1*1024)
    color = floor[tideX][tideY]
    color = color*255
    return color

def desenha_todos_sprites(posx, posy, rot, sprites, item_gerado, item_spawn, inventario, tela, carro_boom0, carro_boom1, carro_boom2, boom0, boom1, boom2, surf, invisivel, efeito, pontuacão, floor, tempo_universal_segundos, moedas_coletadas, reiniciar, fantasma, diamante, ferro, ouro, sprite_diamante, sprite_ferro, sprite_ouro, menos_dois, highscore, highscore_name):
    angles = []
    fish_eye_corrections  = []
    all_coordinates = []
    coordinate_index_type = []
    if efeito == 2:
        menos_dois += 2
    for i in range(len(sprites)):
        for j in range(len(sprites[i].coordinates)):
            all_coordinates.append((sprites[i].coordinates)[j])
    for i in range(len(sprites)):
        for j in range(len(sprites[i].coordinates)):
            coordinate_index_type.append(sprites[i].type)
    for i in range(len(all_coordinates)):
        angle = (np.arctan((all_coordinates[i][1]-posy)/(all_coordinates[i][0]-posx + 0.01)))
        if abs(posx+np.cos(angle)-all_coordinates[i][0]) > abs(posx-all_coordinates[i][0]):
            angle = (angle - np.pi)%(2*np.pi)
        angles.append(angle)
    indexes_invalidos = []
    for i in range(len(angles)):
        angulo_examinado = angles[i] - rot
        for j in range(len(angles)):
            if (angulo_examinado >= angles[j] - 0.05 and angulo_examinado <= angles[j] + 0.05) and i != j:
                dist_i = np.sqrt((posx - all_coordinates[i][0])**2 + (posy - all_coordinates[i][1])**2)
                dist_j = np.sqrt((posx - all_coordinates[j][0])**2 + (posy - all_coordinates[j][1])**2)
                if dist_i > dist_j:
                    angleF = (rot - angles[j])%(2*np.pi)
                    if angleF > 11*np.pi/6 or angleF < np.pi/6:
                        indexes_invalidos.append(i)
                else:
                    angleF = (rot - angles[i])%(2*np.pi)
                    if angleF > 11*np.pi/6 or angleF < np.pi/6:
                        indexes_invalidos.append(j)
    for i in range(len(angles)):
        follow = True
        if i in indexes_invalidos:
            follow = False
        fish_eye_corrections.append((rot - angles[i])%(2*np.pi))
        if coordinate_index_type[i] == "item":
            if (posx < all_coordinates[i][0] + 1 and posx > all_coordinates[i][0] - 1) and (posy < all_coordinates[i][1] + 1 and posy > all_coordinates[i][1] - 1):
                item_gerado = False
                item_spawn = False
        elif coordinate_index_type[i] == "moeda":
            execute = True
            if (posx < all_coordinates[i][0] + 1 and posx > all_coordinates[i][0] - 1) and (posy < all_coordinates[i][1] + 1 and posy > all_coordinates[i][1] - 1):
                new_coords = item_coordinate_generator(floor)
                for m in range(len(sprites)):
                    for n in range(len(sprites[m].coordinates)):
                        if (sprites[m].coordinates)[n] == all_coordinates[i]:
                            if execute:
                                (sprites[m].coordinates)[n] = new_coords
                                execute = False
                                print("old coords:", all_coordinates[i])
                                print((sprites[m].coordinates)[n])
                all_coordinates[i] = new_coords
                moedas_coletadas = moedas_coletadas + 1
                print("moedas coletadas:", moedas_coletadas)
        elif (int(posx), int(posy)) == (int(all_coordinates[i][0]), int(all_coordinates[i][1])):
            if not invisivel:
                tela.blit(carro_boom0, (260, 380))
                pygame.display.update()
                time.sleep(0.1)
                tela.blit(surf, (0, 0))
                tela.blit(carro_boom1, (260, 380))
                pygame.display.update()
                time.sleep(0.1)
                tela.blit(surf, (0, 0))
                tela.blit(carro_boom2, (260, 380))
                pygame.display.update()
                time.sleep(0.1)
                tela.blit(boom0, (120, 360))
                pygame.display.update()
                time.sleep(0.1)
                tela.blit(surf, (0, 0))
                tela.blit(boom1, (120, 200))
                pygame.display.update()
                time.sleep(0.1)
                tela.blit(surf, (0, 0))
                tela.blit(boom2, (120, 200))
                pygame.display.update()
                time.sleep(0.1)
                total = 9999999
                highscore, highscore_name, reiniciar = scores.scorepage(800, 600, total, highscore, highscore_name)
                reiniciar = printscores.printscores(800, 600, highscore_name, highscore)
                reiniciar = True
            else:
                donothing = True
        angle2_2 = fish_eye_corrections[i]
        enx2 = all_coordinates[i][0]
        eny2 = all_coordinates[i][1]
        angle = angles[i] - rot
        if angle2_2 > 11*np.pi/6 or angle2_2 < np.pi/6:
            if coordinate_index_type[i] == "IA_carros":
                sprite2 = sprites[0].sprite_animations
                if angle < 0.3 and angle > -0.3:
                    spriteD = sprite2[0]
                    spsize = np.asarray(spriteD.get_size())
                elif angle > 0.3 and angle < 0.7:
                    spriteD = sprite2[1]
                    spsize = np.asarray(spriteD.get_size())
                elif angle > 0.7 and angle < 1.1:
                    spriteD = sprite2[2]
                    spsize = np.asarray(spriteD.get_size())
                elif angle > 1.1:
                    spriteD = sprite2[3]
                    spsize = np.asarray(spriteD.get_size())
                elif angle < -0.3 and angle > -0.7:
                    spriteD = sprite2[4]
                    spsize = np.asarray(spriteD.get_size())
                elif angle < -0.7 and angle > -1.1:
                    spriteD = sprite2[5]
                    spsize = np.asarray(spriteD.get_size())
                elif angle < -1.1:
                    spriteD = sprite2[6]
                    spsize = np.asarray(spriteD.get_size())
                dist = np.sqrt((enx2 - posx)**2 + (eny2 - posy)**2)
                scaling = min(1/dist, 2)
                vert = (300 + 300*scaling - scaling*spsize[1]/2)
                hor = (400 - 800*np.sin(angle2_2) - scaling*spsize[0]/2)
                spsurf = pygame.transform.scale(spriteD, scaling*spsize)
                #if follow:
                if True:
                    tela.blit(spsurf, (hor, vert))
            elif coordinate_index_type[i] == "placa":
                sprite2 = (sprites[1].sprite_animations)[0]
                spsize = np.asarray(sprite2.get_size())
                dist = np.sqrt((enx2 - posx)**2 + (eny2 - posy)**2)*10
                cos2 = np.cos(angle2_2)
                scaling = min(1/dist, 2)/cos2
                vert = (300 + 300*scaling - scaling*spsize[1]/2)
                hor = (400 - 800*np.sin(angle2_2) - scaling*spsize[0]/2)
                spsurf = pygame.transform.scale(sprite2, scaling*spsize)
                if follow:
                    tela.blit(spsurf, (hor, vert))
            elif coordinate_index_type[i] == "item":
                inventario[0] = 1
                sprite2 = (sprites[2].sprite_animations)[0]
                spsize = np.asarray(sprite2.get_size())
                dist = np.sqrt((enx2 - posx)**2 + (eny2 - posy)**2)
                cos2 = np.cos(angle2_2)
                scaling = min(1/dist, 2)/cos2
                vert = (300 + 300*scaling - scaling*spsize[1]/2)
                hor = (400 - 800*np.sin(angle2_2) - scaling*spsize[0]/2)
                spsurf = pygame.transform.scale(sprite2, scaling*spsize)
                if follow and item_spawn:
                    tela.blit(spsurf, (hor, vert))
            elif coordinate_index_type[i] == "moeda":
                counter_animação = int(tempo_universal_segundos*10)
                valor_sprite = counter_animação%8
                sprite2 = (sprites[3].sprite_animations[valor_sprite])
                spsize = np.asarray(sprite2.get_size())
                dist = np.sqrt((enx2 - posx)**2 + (eny2 - posy)**2)
                cos2 = np.cos(angle2_2)
                scaling = min(1/dist, 2)/cos2
                vert = (300 + 300*scaling - scaling*spsize[1]/2)
                hor = (400 - 800*np.sin(angle2_2) - scaling*spsize[0]/2)
                spsurf = pygame.transform.scale(sprite2, scaling*spsize)
                tela.blit(spsurf, (hor, vert))
                #print("desenhada uma moeda!")

    ouro_hud = pygame.transform.scale(sprite_ouro, (80, 40))
    item_ouro = pygame.transform.grayscale(ouro_hud)
    tela.blit(item_ouro, (690, 200))
    ferro_hud = pygame.transform.scale(sprite_ferro, (40, 80))
    item_ferro = pygame.transform.grayscale(ferro_hud)
    tela.blit(item_ferro, (710, 110))
    diamante_hud = pygame.transform.scale(sprite_diamante, (80, 80))
    item_diamante = pygame.transform.grayscale(diamante_hud)
    tela.blit(item_diamante, (700, 30))
    num_moedas = pygame.transform.scale(sprites[3].sprite_animations[0], (224 / 5, 224 / 5))
    tela.blit(num_moedas, (20, 480))
    if not item_spawn:
        sprite2 = (sprites[2].sprite_animations[0])
        if ouro == True:
            tela.blit(ouro_hud, (690, 200))
        if ferro == True:
            tela.blit(diamante_hud, (700, 30))
        if diamante == True:
            tela.blit(ferro_hud, (710, 110))
    if invisivel:
        fantasma = pygame.transform.scale(fantasma, (400, 320))
        tela.blit(fantasma, (-150, -100))

    #print(pontuação)
    return item_gerado, pontuacão, item_spawn, reiniciar, moedas_coletadas, menos_dois