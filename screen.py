import pygame
from os.path import join
import time
import score_menu
def init(display_surface, clock, WINDOW_WIDTH, WINDOW_HEIGHT,highscore,highscore_name,font_base):
    press = False
    show = True
    flash_timer = 0
    flash_interval = 300
    game = True
    while not press:
        flash_timer += clock.get_rawtime()
        display_surface.fill('black')
        menu_surf = pygame.image.load(join('images', 'init', 'menunovao.png'))
        menu_surf = pygame.transform.scale(menu_surf, (700, 300))
        scoreimage= pygame.image.load('images/init/scoreimage.png')
        menu_rect = menu_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT/3))
        init_surf = pygame.image.load(join('images', 'init', 'pressione r.png'))
        init_surf = pygame.transform.scale(init_surf, (500, 70))
        scoreimage = pygame.transform.scale(scoreimage, (500, 70))
        init_rect = init_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT*3/4))
        if flash_timer >= flash_interval:
            flash_timer = 0
            show = not show
            display_surface.fill('black')
        if show:
            display_surface.blit(init_surf, init_rect)
            display_surface.blit(scoreimage, (380, 620))
        display_surface.blit(menu_surf, menu_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                press = True
                return False
        if pygame.key.get_just_pressed()[pygame.K_r]:
            press = True
            return True
        if pygame.key.get_just_pressed()[pygame.K_h]:
            score_menu.scorepage(highscore_name,highscore,WINDOW_WIDTH,WINDOW_HEIGHT,font_base)
        pygame.display.flip()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

def end(font_base, WINDOW_WIDTH, WINDOW_HEIGHT,pontuacao,highscore_name,highscore,qnt_moedas):
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    fontebase2 = pygame.font.Font('Oxanium-Bold.ttf',30)
    display_surface.fill((0, 0, 0,))
    if pontuacao > highscore[-1]:
        texto_do_usuario = ""
        entrada_concluida = False
        x = 0
        while True:
            display_surface.fill((0, 0, 0))
            novorecorde = pygame.image.load(join('images', 'end', 'NOVORECORDE.png'))
            novorecorde = pygame.transform.scale(novorecorde, (600, 130))
            display_surface.blit(novorecorde, (370, 20))
            escrevanome=font_base.render('Qual seu nome motorista?', False,(255,125,37))
            display_surface.blit(escrevanome, (500, 320))
            texto = font_base.render(texto_do_usuario, False, (255, 125, 37))
            display_surface.blit(texto, (500, 400))

            # escrever aqui o nome do jogador
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if x == 0:
                            entrada_concluida = True
                    elif event.key == pygame.K_BACKSPACE:
                        texto_do_usuario = texto_do_usuario[:-1]
                    else:
                        if len(texto_do_usuario) <= 9:
                            texto_do_usuario += event.unicode
                        else:
                            limite = fontebase2.render("o limite de caractéres é 9", False, (255, 125, 37))
                            display_surface.blit(limite, (50, 600))
                            time.sleep(0.7)

            pygame.display.update()

            if entrada_concluida:
                highscore.pop()
                highscore_name.pop()
                highscore.append(pontuacao)
                highscore.sort(reverse=True)
                index = highscore.index(pontuacao)
                highscore_name.insert(index, texto_do_usuario)
                salvar = open('SCORE.txt', 'w')
                for i in highscore_name:
                    salvar.write(f"{i}\n")
                for h in highscore:
                    salvar.write(f"{h}\n")
                x += 1
                entrada_concluida = False
                if score_menu.scorepage(highscore_name,highscore,WINDOW_WIDTH,WINDOW_HEIGHT,font_base):
                    return True
                else:
                    return False


            # print ranking
    else:
        display_surface.fill('black')
        while True:
            derrota_surf = pygame.image.load(join('images', 'end', 'voceperdeu.png'))
            derrota_surf = pygame.transform.scale(derrota_surf, (640, 180))
            derrota_rect = derrota_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT/3))
            display_surface.blit(derrota_surf, derrota_rect)
            tentardnv_surf = pygame.image.load(join('images', 'end', 'pressionerpratentardenovo.png'))
            tentardnv_surf = pygame.transform.scale(tentardnv_surf, (500, 70))
            tentardnv_rect = tentardnv_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT*3/5))
            display_surface.blit(tentardnv_surf, tentardnv_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return False
                    exit()

            if pygame.key.get_pressed()[pygame.K_r]:
                return True
                pass

            pygame.display.update()