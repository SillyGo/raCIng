import pygame
import screen
def scorepage(HIGHSCORE_label_nomes,HIGHSCORE_label_pontos,WINDOW_WIDTH, WINDOW_HEIGHT,fontebase):
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    display_surface.fill((0, 0, 0,))
    print_y=180
    print_yp=180
    clock = pygame.time.Clock()
    contador=0
    while True:
        highscore=pygame.image.load('images/end/highscore.png')
        menu=pygame.image.load('images/end/menu.png')
        menu=pygame.transform.scale(menu,(250,100))
        highscore=pygame.transform.scale(highscore,(430,80))
        display_surface.blit(highscore,(440,20))
        display_surface.blit(menu,(60,600))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if pygame.key.get_just_pressed()[pygame.K_m]:
            if screen.init(display_surface,clock,WINDOW_WIDTH,WINDOW_HEIGHT,HIGHSCORE_label_pontos,HIGHSCORE_label_nomes,fontebase):
                return True
            else:
                return False
        if contador == 0:
            for i in HIGHSCORE_label_nomes:
                nomes = fontebase.render(f"{i}", False, (255, 125, 37))
                display_surface.blit(nomes, (450, print_y))
                print_y+=60
            for h in HIGHSCORE_label_pontos:
                pontos = fontebase.render(f"{h}", False, (255, 125, 37))
                display_surface.blit(pontos, (850, print_yp))
                print_yp += 60
        pygame.display.update()
        contador+=1