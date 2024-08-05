#------------------------------------------------------------------------------------------------------------------------------------------#

import pygame
from pygame.locals import *
import numpy as np
from random import randint
from pygamevideo import Video

import scores
import printscores
import funcoes_graficas
import funcoes_de_movimento
#------------------------------------------------------------------------------------------------------------------------------------------#

class Sprite():                                                                         #único propósito dessa classe é armazenar efetivamente
    def __init__(self, coordinates:list, sprite_animations:list, type:str):             #as principais informações que a IA deve possuir
        self.coordinates = coordinates
        self.sprite_animations = sprite_animations
        self.type = type 

#------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------#

def main():
    pode_ser_contramao = False
    moedas_coletadas = 0                                                                
    global reiniciar, voltas, inicio, total, highscore, highscore_name
    voltas = desconto = 0
    reiniciar = False
    inicio = False
    if reiniciar:                                                                       #a função, ao retornar 0, acaba, por isso o return 0
        return 0                                                                        #nesse IF, de modo a acabar com a execução da função,
    cooldown = 0                                                                        #voltando para o menu
    pontuacao = 1   
    efeito = -1
    time_counter = 0
    inventario = [0,0,0,0,0]
    clock = pygame.time.Clock()
    item_spawn = True
    item_gerado = False
    counter3 = 0
    counter5 = 1
    counter4 = 0
    velocidade = 0.03                                                                   #as proximas linhas determinam as coordenadas das placas de curva
    placas_curva = [(90.227809958157, 92.78799252070566), (51.36282482283635, 50.83774316669684),
    (5.647850658334595, 77.14291930556416),
    (7.754217009887637, 5.300902300371192),
    (96.37124588512664, 43.25415639209596)]

    size_interval = 300                                                                 #determina o intervalo entre duas coordenadas adjacentes.
    trajetoIA4 = [(10, 10), (28, 9), (71, 30), (91, 42), (93, 52), (88, 79), (85, 88), (70, 84), (53, 60), (43, 59), (11, 70), (9, 17), (10, 10),(28, 9), (71, 30), (91, 42), (93, 52), (88, 79), (85, 88), (70, 84)]
    trajetoIA1 = [(9, 32),
(21, 8),
(46, 19),
(73, 33),
(88, 54),
(84, 82),
(65, 77),
(44, 60),
(16, 67),
(7, 41),
(12, 12),
(38, 15),
(64, 28),
(89, 44),
(92, 48),
(91, 62),
(80, 88),
(59, 70),
(34, 62),
(7, 62)]
    trajetoIA3 = [(90, 40),
(91, 62),
(77, 86),
(56, 66),
(29, 63),
(5, 55),
(6, 25),
(15, 8),
(41, 13),
(67, 29),
(88, 48),
(92, 48),
(91, 62),
(77, 86),
(56, 66),
(29, 63),
(5, 55),
(6, 25),
(15, 8),
(41, 13)]
    trajetoIA2 = [(18, 11),
(33, 15),
(58, 27),
(85, 41),
(92, 48),
(91, 62),
(79, 86),
(58, 66),
(32, 63),
(6, 61),
(7, 31),
(20, 5),
(45, 19),
(72, 32),
(88, 53),
(86, 82),
(63, 73),
(39, 62),
(11, 66),
(10, 37)]
    L = len(trajetoIA1)
    trajeto_final_IA1 = []
    trajeto_final_IA2 = []
    trajeto_final_IA3 = []
    trajetos_finais = []


#nas próximas linhas, teremos um sistema que pega as coordenadas que foram dadas anteriormente para cada uma das IAs, e liga cada
#coordenada à coordenada próxima, de modo que a IA siga um caminho (aparentemente) contínuo, para que ela não fique teleportando de uma 
#coordenada à próxima.
    for i in range(L):  
        if i == L - 1:
            xIA = trajetoIA1[i][0]                                          #xIA e yIA determinam o par ordenado da posição atual
            yIA = trajetoIA1[i][1]                                          
            trajeto_final_IA1.append(trajetoIA1[i])                         #adiciona o par ordenado ao trajeto final
            dx = (trajetoIA1[0][0] - trajetoIA1[i][0])/size_interval        #calcula o intervalo em X entre duas coordenadas vizinhas
            dy = (trajetoIA1[0][1] - trajetoIA1[i][1])/size_interval        #calcula o intervalo em Y entre duas coordenadas vizinhas
        else:
            xIA = trajetoIA1[i][0]
            yIA = trajetoIA1[i][1]
            trajeto_final_IA1.append(trajetoIA1[i])
            dx = (trajetoIA1[i+1][0] - trajetoIA1[i][0])/size_interval
            dy = (trajetoIA1[i+1][1] - trajetoIA1[i][1])/size_interval
        for j in range(size_interval - 1):
            xIA = xIA + dx 
            yIA = yIA + dy
            trajeto_final_IA1.append((xIA, yIA))                            #adiciona o par ordenado ao trajeto final

    for i in range(L):
        if i == L - 1:
            xIA = trajetoIA2[i][0]
            yIA = trajetoIA2[i][1]
            trajeto_final_IA2.append(trajetoIA2[i])
            dx = (trajetoIA2[0][0] - trajetoIA2[i][0])/size_interval
            dy = (trajetoIA2[0][1] - trajetoIA2[i][1])/size_interval
        else:
            xIA = trajetoIA2[i][0]
            yIA = trajetoIA2[i][1]
            trajeto_final_IA2.append(trajetoIA2[i])
            dx = (trajetoIA2[i+1][0] - trajetoIA2[i][0])/size_interval
            dy = (trajetoIA2[i+1][1] - trajetoIA2[i][1])/size_interval
        for j in range(size_interval - 1):
            xIA = xIA + dx 
            yIA = yIA + dy
            trajeto_final_IA2.append((xIA, yIA))

    for i in range(L):
        if i == L - 1:
            xIA = trajetoIA3[i][0]
            yIA = trajetoIA3[i][1]
            trajeto_final_IA3.append(trajetoIA3[i])
            dx = (trajetoIA3[0][0] - trajetoIA3[i][0])/size_interval
            dy = (trajetoIA3[0][1] - trajetoIA3[i][1])/size_interval
        else:
            xIA = trajetoIA3[i][0]
            yIA = trajetoIA3[i][1]
            trajeto_final_IA3.append(trajetoIA3[i])
            dx = (trajetoIA3[i+1][0] - trajetoIA3[i][0])/size_interval
            dy = (trajetoIA3[i+1][1] - trajetoIA3[i][1])/size_interval
        for j in range(size_interval - 1):
            xIA = xIA + dx 
            yIA = yIA + dy
            trajeto_final_IA3.append((xIA, yIA))

    trajetos_finais.append(trajeto_final_IA1)
    trajetos_finais.append(trajeto_final_IA2)
    trajetos_finais.append(trajeto_final_IA3)

    pygame.init()
    coordinates = []
    pygame.mouse.set_visible(False)
    #enx, eny = 5,5
    halfvres = 100
    hres = 120
    #rot_anterior = 0
    mod = hres/60
#daqui para frente, teremos apenas o carregamento de imagens e a modificação de seus tamanhos, além da criação da tela e de outras
#funcionalidades importantes para o código como um todo.
    tela = pygame.display.set_mode((800, 600))
    frame = np.random.uniform(0,1, (hres, halfvres*2, 3)) 
    sky = pygame.image.load('files/images/bg2.png')
    sky = pygame.surfarray.array3d(pygame.transform.scale(sky, (360, halfvres*2)))/255
    floor = pygame.surfarray.array3d(pygame.image.load('files/images/MarioKart.png')) / 255
    carro_reto0 = pygame.image.load("files/carros/player_frente0.png")
    carro_reto0 = pygame.transform.scale(carro_reto0, (66 * 5, 37 * 5))
    carro_reto1 = pygame.image.load("files/carros/player_frente1.png")
    carro_reto1 = pygame.transform.scale(carro_reto1, (66 * 5, 37 * 5))
    carro_direita0 = pygame.image.load("files/carros/player_direita0.png")
    carro_direita0 = pygame.transform.scale(carro_direita0, (68 * 5, 37 * 5))
    carro_esquerda0 = pygame.transform.flip(carro_direita0, True, False)
    carro_direita1 = pygame.image.load("files/carros/player_direita1.png")
    carro_direita1 = pygame.transform.scale(carro_direita1, (70 * 5, 37 * 5))
    carro_esquerda1 = pygame.transform.flip(carro_direita1, True, False)
    carro_direita2 = pygame.image.load("files/carros/player_direita2.png")
    carro_direita2 = pygame.transform.scale(carro_direita2, (72 * 5, 37 * 5))
    carro_esquerda2 = pygame.transform.flip(carro_direita2, True, False)
    carro_direita3 = pygame.image.load("files/carros/player_direita3.png")
    carro_direita3 = pygame.transform.scale(carro_direita3, (74 * 5, 37 * 5))
    carro_esquerda3 = pygame.transform.flip(carro_direita3, True, False)
    carro_direita4 = pygame.image.load("files/carros/player_direita4.png")
    carro_direita4 = pygame.transform.scale(carro_direita4, (68 * 5, 37 * 5))
    carro_esquerda4 = pygame.transform.flip(carro_direita4, True, False)
    carro_direita5 = pygame.image.load("files/carros/player_direita5.png")
    carro_direita5 = pygame.transform.scale(carro_direita5, (71 * 5, 37 * 5))
    carro_esquerda5 = pygame.transform.flip(carro_direita5, True, False)
    carro_direita6 = pygame.image.load("files/carros/player_direita6.png")
    carro_direita6 = pygame.transform.scale(carro_direita6, (73 * 5, 37 * 5))
    carro_esquerda6 = pygame.transform.flip(carro_direita6, True, False)
    carro_direita7 = pygame.image.load("files/carros/player_direita7.png")
    carro_direita7 = pygame.transform.scale(carro_direita7, (73 * 5, 37 * 5))
    carro_esquerda7 = pygame.transform.flip(carro_direita7, True, False)
    lista_carros = [
        [carro_esquerda0, carro_esquerda1, carro_esquerda2, carro_esquerda3, carro_esquerda4, carro_esquerda5,
         carro_esquerda6, carro_esquerda7],
        [carro_reto0, carro_reto1],
        [carro_direita0, carro_direita1, carro_direita2, carro_direita3, carro_direita4, carro_direita5, carro_direita6,
         carro_direita7]]
    carro_boom0 = pygame.image.load("files/carros/carro_boom0.png")
    carro_boom0 = pygame.transform.scale(carro_boom0, (66 * 5, 37 * 5))
    carro_boom1 = pygame.image.load("files/carros/carro_boom1.png")
    carro_boom1 = pygame.transform.scale(carro_boom1, (66 * 5, 37 * 5))
    carro_boom2 = pygame.image.load("files/carros/carro_boom2.png")
    carro_boom2 = pygame.transform.scale(carro_boom2, (66 * 5, 37 * 5))
    boom0 = pygame.image.load("files/images/boom_zero.png")
    boom1 = pygame.image.load("files/images/boom_one.png")
    boom2 = pygame.image.load("files/images/boom_two.png")
    boom0 = pygame.transform.scale(boom0, (640, 380))
    boom1 = pygame.transform.scale(boom1, (640, 620))
    boom2 = pygame.transform.scale(boom2, (560, 740))
    placa = pygame.image.load("files/images/placa_curva.png")
    placa = pygame.transform.scale(placa, (160 * 13, 400 * 13))
    IA_frente = pygame.image.load("files/carros/inimigo_reto.png")
    IA_direita0 = pygame.image.load("files/carros/inimigo_direita0.png")
    IA_direita1 = pygame.image.load("files/carros/inimigo_direita2.png")
    IA_direita2 = pygame.image.load("files/carros/inimigo_direita4.png")
    IA_direita3 = pygame.image.load("files/carros/inimigo_direita6.png")
    IA_esquerda0 = pygame.transform.flip(IA_direita0, True, False)
    IA_esquerda1 = pygame.transform.flip(IA_direita1, True, False)
    IA_esquerda2 = pygame.transform.flip(IA_direita2, True, False)
    IA_esquerda3 = pygame.transform.flip(IA_direita3, True, False)
    IA_frente = pygame.transform.scale(IA_frente, (47 * 14, 26 * 14))
    IA_esquerda0 = pygame.transform.scale(IA_esquerda0, (47 * 14, 26 * 14))
    IA_esquerda1 = pygame.transform.scale(IA_esquerda1, (47 * 14, 26 * 14))
    IA_esquerda2 = pygame.transform.scale(IA_esquerda2, (47 * 14, 26 * 14))
    IA_direita0 = pygame.transform.scale(IA_direita0, (47 * 14, 26 * 14))
    IA_direita1 = pygame.transform.scale(IA_direita1, (47 * 14, 26 * 14))
    IA_direita2 = pygame.transform.scale(IA_direita2, (47 * 14, 26 * 14))
    moeda0 = pygame.image.load("files/moedas/moeda0.png")
    moeda1 = pygame.image.load("files/moedas/moeda1.png")
    moeda2 = pygame.image.load("files/moedas/moeda2.png")
    moeda3 = pygame.image.load("files/moedas/moeda3.png")
    moeda4 = pygame.image.load("files/moedas/moeda4.png")
    moeda5 = pygame.image.load("files/moedas/moeda5.png")
    moeda6 = pygame.image.load("files/moedas/moeda6.png")
    moeda7 = pygame.image.load("files/moedas/moeda7.png")
    moeda0 = pygame.transform.scale(moeda0, (945/4, 750/4))
    moeda1 = pygame.transform.scale(moeda1, (945/4, 750/4))
    moeda2 = pygame.transform.scale(moeda2, (945/4, 750/4))
    moeda3 = pygame.transform.scale(moeda3, (945/4, 750/4))
    moeda4 = pygame.transform.scale(moeda4, (945/4, 750/4))
    moeda5 = pygame.transform.scale(moeda5, (945/4, 750/4))
    moeda6 = pygame.transform.scale(moeda6, (945/4, 750/4))
    moeda7 = pygame.transform.scale(moeda7, (945/4, 750/4))
    sprite_ghost = pygame.image.load("files/images/panthom.png")
    sprite_nitro = pygame.image.load("files/images/nitro.png")
    sprite_twox = pygame.image.load("files/images/twox.png")
    fantasma = pygame.image.load('files/images/fantasma.png')
    coordenadas_moedas = []
    for i in range(6):
        coordenadas_moedas.append(funcoes_graficas.item_coordinate_generator(floor))
    sprites_IA = [IA_frente, IA_esquerda0, IA_esquerda1, IA_esquerda2, IA_direita0, IA_direita1, IA_direita2]
    OBJ_moedas = Sprite(coordenadas_moedas, [moeda0, moeda1, moeda2, moeda3, moeda4, moeda5, moeda6, moeda7], "moeda")
    ghost =  False
    nitro = False
    twox = False
    sprites_placa = [placa]
    counterOleo = 21
    for i in range(3):
        coordinates.append([0,0])
    IA_carros = Sprite(coordinates, sprites_IA, "IA_carros")
    placas_transito = Sprite(placas_curva, sprites_placa, "placa")
    sprites = [IA_carros, placas_transito, 0, OBJ_moedas]
    pygame.event.set_grab(1)
    clock_setter = clock.tick()
    tempo_limite_velocidade = -7
    tempo_limite_invisibilidade = -7
    invisivel = False
    posx, posy, rot = 92.5, 48.1, np.pi/2
#------------------------------------------------------------------------------------------------------------------------------------------#
    while (1):                                                              #super-loop do jogo.
        if reiniciar:                                                       #caso o jogo acabe, volte para o menu
            return 0
        super_speed = False
        if efeito == 1:                                                     #caso o efeito em atuação seja o de invisibilidade...
            tempo_limite_invisibilidade = time_counter/1000                 #crie um timer para evitar que o efeito dure para sempre
            invisivel = True                                                #deixa o personagem invisível
        if time_counter/1000 - tempo_limite_invisibilidade < 6:
            invisivel = True
        else:
            invisivel = False                                               #caso o timer acabe, termine o efeito de invisibilidade.
        time_counter = time_counter + clock.get_time()
        if (not item_gerado) and item_spawn:                                #caso um item não tiver sido gerado, e não hajam itens spawnados...
            item_gerado = True                                              #gere um item
            itens_index = [sprite_ghost, sprite_nitro, sprite_twox]         #determine a natureza desse item.
            index = randint(0, 2)                                           #determina um dos 3 itens a serem gerados, de forma aleatória.
            item_sorteado = itens_index[index]
            if index == 0:                                                  #determine uma forma de facilmente identificar a natureza desse item
                ghost = False   
                nitro = True
                twox = False
            elif index == 1:
                nitro = False
                ghost = True
                twox = False
            elif index ==  2:
                nitro = False
                ghost = False
                twox = True
            coordenadas_item = [funcoes_graficas.item_coordinate_generator(floor)]  #determina a coordenada do item a ser gerado.
            sprites[2] = Sprite(coordenadas_item, [item_sorteado], "item")  #determina o objeto "sprite" para o item que tenha sido gerado.
        surf = pygame.surfarray.make_surface(frame*255)
        surf = pygame.transform.scale(surf, (1000, 600))
        tela.blit(surf, (0,0))
        fonte = pygame.font.Font('Oxanium-Bold.ttf', 40)
        num_pontos = fonte.render(f"{pontuacao:.2f}", False, (225, 125, 37))    #escreve o tempo decorrido para o jogador.
        tela.blit(num_pontos, (20, 550))                                        #desenha na tela oque foi escrito na última linha.
        num_moedas = fonte.render(f"{moedas_coletadas}", False, (255, 255, 0))  #faz o mesmo que foi feito para o tempo com o número de moedas.
        tela.blit(num_moedas, (70, 482))
        for event in pygame.event.get():                                        #caso ESC seja apertada, termine o programa.
            if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                #print(pontuação)
                exit()
        item_gerado, pontuacao, item_spawn, reiniciar, moedas_coletadas, desconto = funcoes_graficas.desenha_todos_sprites(posx, posy, rot, sprites, item_gerado, item_spawn, inventario, tela, carro_boom0, carro_boom1, carro_boom2, boom0, boom1, boom2, surf, invisivel, efeito, pontuacao, floor, time_counter / 1000, moedas_coletadas, reiniciar, fantasma, ghost, nitro, twox, sprite_ghost, sprite_nitro, sprite_twox, desconto, highscore, highscore_name)
        if reiniciar:                                                           #novamente, caso o jogo acabe, reinicie e volte para o menu
            return True
            break
        for i in range(len(trajetos_finais)):
            if counter3 >= len(trajetos_finais[i]):                             #atualiza a coordenada atual de cada uma das IAs com as coordenadas
                counter3 = 0                                                    #determinadas em seu respectivo trajeto final, de modo que a IA
            coordinates[i][0] = trajetos_finais[i][counter3][0]                 #, com isso, faz parecer que a IA está se mexendo.
            coordinates[i][1] = trajetos_finais[i][counter3][1]
            counter3 = counter3 + 1
        for i in range(hres):                                                   #analiza todo o horizonte
            ang_abertura = rot + np.deg2rad(i/mod - 30)                         #determina o ângulo de abertura
            frame[i][:] = sky[int(np.rad2deg(ang_abertura)%290)][:]             #desenha o ceu.
            sin, cos, cos2 = np.sin(ang_abertura), np.cos(ang_abertura), np.cos(np.deg2rad(i/mod - 30)) #determina o seno do angulo de abertura, seu cosseno, e o fator de correção do efeito de olho de peixe.
            for j in range(halfvres):
                d = ((halfvres)/(halfvres - j))/cos2                            #determina a distância, com seu efeito de olho de peixe corrigido
                x, y = posx + cos*d, posy + sin*d                               #determina as coordenadas X e Y de uma determinada posição.
                color = funcoes_graficas.draw_floor(x, y, halfvres, frame, i, j, floor, posx, posy) #determina uma lista com o valor RGB do pixel sobre o qual o jogador está.
                R, G, B = int(color[0]), int(color[1]), int(color[2])           #determina cada um dos valores RGB
                if R == 112 and G == 112 and B == 112:
                    pode_ser_contramao = False
                if R == 176 and G == 160 and B == 112:                          #os 3 IFs / ELIFs executam caso o o jogador esteja em cima da terra, ou seja, fora da pista de corrida
                    velocidade = 0.0015
                elif R == 114 and G == 128 and B == 88:
                    velocidade = 0.0015
                elif R == 160 and G == 144 and B == 96:
                    velocidade = 0.0015
                elif R == 0 and G == 0 and B == 0:                              #caso o jogador passar por óleo, resete o counterOleo, logo 
                    counterOleo = 0                                             #que, caso este seja abaixo de determinadom valor, seu efeito executa
                elif R == 127 and G == 127 and B == 127:                        #caso o jogador bata em uma parede, faça o carro explodir
                    funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                    total = 999999                                              #evita que o jogador morrendo cedo o dê uma pontuação melhor que o normal.
                    highscore, highscore_name, reiniciar = scores.scorepage(800, 600, total, highscore, highscore_name) #as próximas linhas são referentes à determinação do highscore
                    reiniciar = printscores.printscores(800, 600, highscore_name, highscore)    
                    return True
                    break
                elif efeito  == 0:                                                                              #caso o efeito for o nitro...
                    velocidade = 0.04                                                                           #aumente a velocidade
                    tempo_limite_velocidade = time_counter/1000                                                 #define um tempo limite para o efeito do nitro
                elif (R == 209 and  G == 209 and B == 209) and pode_ser_contramao == False:                     #caso o RGB seja igual ao da linha de chegada, é logico 
                    inicio = True                                                                               #concluir que o jogador atravessou a linha de chegada,
                    pode_ser_contramao = True
                    if time_counter / 1000 - cooldown > 4:                                                      #para evitar que isso execute várias vezes, define-se um timer
                        print("volta realizada!")
                        voltas += 1                                                                             #de cooldown, que é o cooldown mencionado, e acrescenta 1
                        cooldown = time_counter / 1000                                                          #à quantidade de voltas efetuadas.
                    #reiniciar = funções_graficas.explosion_of_death(tela,surf, pontuação, boom0, boom1, boom2)
                elif R == 120 and  G == 0 and B == 0:
                    reiniciar = funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                    return 0
                elif R == 248 and  G == 72 and B == 72:
                    reiniciar = funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                    return 0
                elif R == 0 and  G == 232 and B == 0:
                    reiniciar = funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                    return 0
                elif R == 0 and  G == 136 and B == 0:
                    reiniciar = funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                    return 0
                elif R == 96 and  G == 248 and B == 96:
                    reiniciar = funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                    return 0
                elif R == 0 and  G == 32 and B == 248:
                    reiniciar = funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                    return 0
                elif R == 0 and  G == 0 and B == 96:
                    reiniciar = funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                    return 0
                elif R == 104 and  G == 104 and B == 248:
                    reiniciar = funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                    return 0
                #elif R == 209 and  G == 209 and B == 209:
                #    reiniciar = funcoes_graficas.explosion_of_death(tela, surf, pontuacao, boom0, boom1, boom2)
                #    return 0
                elif time_counter/1000 - tempo_limite_velocidade < 1:
                    velocidade = 0.04
                else:
                    velocidade = 0.015
        if counter4 > 0 and counter4 < 5:   #as próximas linhas determinam a animação do carro no caso dele se deslocar na direita ou esquerda.
            tela.blit(lista_carros[0][int((pygame.time.get_ticks()/100)%2)], (240, 400))
        elif counter4 >= 5 and counter4 < 15:
            tela.blit(lista_carros[0][2 + int((pygame.time.get_ticks()/100)%2)], (240, 400))
        elif counter4 >= 15 and counter4 < 20:
            tela.blit(lista_carros[0][4 + int((pygame.time.get_ticks()/100)%2)], (240, 400))
        elif counter4 >= 20:
            tela.blit(lista_carros[0][6 + int((pygame.time.get_ticks()/100)%2)], (240, 400))
        elif counter5 > 1 and counter5 < 5:
            tela.blit(lista_carros[2][int((pygame.time.get_ticks()/100)%2)], (240, 400))
        elif counter5 >= 5 and counter5 < 15:
            tela.blit(lista_carros[2][2 + int((pygame.time.get_ticks()/100)%2)], (240, 400))
        elif counter5 >= 5 and counter5 < 15:
            tela.blit(lista_carros[2][4 + int((pygame.time.get_ticks()/100)%2)], (240, 400))
        elif counter5 >= 15:
            tela.blit(lista_carros[2][6 + int((pygame.time.get_ticks()/100)%2)], (240, 400))
        else:
            tela.blit(lista_carros[1][int((pygame.time.get_ticks()/100)%2)], (250, 400))
        pygame.display.update()
        if time_counter/1000 < 3:
            velocidade = 0
            rot = np.pi/2   
        #a próxima linha determina as novas coordenadas, o counter4 (que determina o tempo que o jogador passou se mexendo na direita),
        #counter5 (determinado pela booleana bool_esquerda), o counterOleo, a possibilidade de um item ter sido spawnado e o efeito em 
        #execução no atual momento.
        posx, posy, rot, counter4, bool_esquerda, counterOleo, item_spawn, efeito = funcoes_de_movimento.movement(posx, posy, rot, pygame.key.get_pressed(), counter4, counter5, counterOleo, item_spawn, velocidade, clock.tick(), ghost, nitro, efeito, pontuacao, invisivel, highscore, highscore_name)
        pontuacao = (time_counter/1000) - 3 - desconto  #atualiza a pontuação do jogador a cada turno
        if not inicio:                      #evita que a pontuação fique negativa e faz com que, caso o jogo 
            pontuacao = 0
        if pontuacao < 0:
            pontuacao = 0
        if bool_esquerda:                   #atualiza o counter5 (esquerda)  caso bool_esquerda retorne True
            counter5 = counter5 + 1
        else:
            counter5 = 0
        if voltas == 3:                     #caso o número de voltas seja igual a 3, termine o jogo e defina as mudanças no highscore, caso existam.
            total = pontuacao + moedas_coletadas
            highscore, highscore_name, reiniciar = scores.scorepage(800, 600, total, highscore, highscore_name)
            reiniciar = printscores.printscores(800, 600, highscore_name, highscore)
            break

#------------------------------------------------------------------------------------------------------------------------------------------#
reiniciar = inicio = False
voltas = desconto = moedas_coletadas = pontuacao = total = 0
def menu():                                                                                             #determina o menu
    global reiniciar, moedas_coletadas, pontuacao, highscore, highscore_name
    pygame.init()
    pygame_icon = pygame.image.load('files/images/icon.png')                                            #carrega o ícone
    pygame.display.set_icon(pygame_icon)                                                                #coloca o ícone
    pygame.display.set_caption('RaCINg')                                                                #cria o título da tela
    tela = pygame.display.set_mode((800, 600))
    video = Video("files/video/inicio.mp4")                                                             #define o video do menu
    video.play()
    while (1):                                                                                          #loop infinito do menu
        video.draw_to(tela, (0, 0))                                                                     #"desenha" o video
        for event in pygame.event.get():                                                                
            if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:     #caso o jogador queira sair, saia.
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_r:                                                             #caso R seja apertado...
                    t = main()                                                                          #inicie o jogo
                    if t:                                                                               
                        continue
                if event.key == pygame.K_h:                                                             #caso H seja apertado,
                    total = pontuacao - moedas_coletadas                                      
                    reiniciar = printscores.printscores(800, 600, highscore_name, highscore)            #desenhe os highscores.
        pygame.display.update()
        pygame.display.flip()

#------------------------------------------------------------------------------------------------------------------------------------------#
highscore_name = []                                                                                     #próximas linhas determinam o highscore
highscore = []                                                                                          #e o display desse, determinados
score = open('SCORE3D.txt', 'r')                                                                        #no arquivo score3d.txt
contador = 0    
for files in score:
    if contador < 5:
        files = files[:-1]
        highscore_name.append(files)
    else:
        highscore.append(float(files))
    contador += 1
pygame.mixer.music.load('files/music/rancing.wav')                                                      #as próximas linhas determinam 
pygame.mixer.music.set_volume(0.4)                                                                      #a execução da música
pygame.mixer.music.play(-1)
score.close()
menu()
