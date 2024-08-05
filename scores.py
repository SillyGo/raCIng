
import pygame
from sys import exit

pygame.init()


def scorepage(WINDOW_WIDTH, WINDOW_HEIGHT, pontuacao, highscore, highscore_name):
    tela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    tela.fill((0, 0, 0,))
    texto_do_usuario = ""
    entrada_concluida= False
    fontebase = pygame.font.Font('Oxanium-Bold.ttf', 40)
    fontebase2 = pygame.font.Font('Oxanium-Bold.ttf', 30)
    while True:
        tela.fill((0, 0, 0))
        texto = fontebase.render(texto_do_usuario, False, (255, 255, 255))
        tela.blit(texto, (230, 250))
        if pontuacao < float(highscore[-1]):
            palavras = fontebase2.render("PARABÉNS PELO SCORE, QUAL SEU NOME?", False, (255, 255, 255))
            tela.blit(palavras, (100, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        highscore.pop(-1)
                        highscore.append(pontuacao)
                        highscore_name.pop(-1)
                        highscore.sort()
                        index=highscore.index(pontuacao)
                        highscore_name.insert(index,texto_do_usuario)
                        salvar=open('SCORE.txt', 'w')
                        for g in highscore_name:
                            salvar.write(f"{g}\n")
                        for i in highscore:
                            salvar.write(f"{i}\n")
                        salvar.close()
                        return highscore, highscore_name, True
                        break
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    elif event.key == pygame.K_BACKSPACE:
                        texto_do_usuario = texto_do_usuario[:-1]
                    else:
                        texto_do_usuario += event.unicode
            pygame.display.update()

        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_RETURN:
                        return highscore, highscore_name, True
                        break
            charlie=pygame.image.load('files/images/gameover.png')
            charlie = pygame.transform.scale(charlie, (2300/4, 380/4))
            tela.blit(charlie, (120, 200))
            coisa="Aperte ENTER para continuar"
            continuar = fontebase.render(coisa, False, (255, 255, 255))
            tela.blit(continuar, (130, 450))
            pygame.display.update()




