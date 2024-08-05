import pygame
from os.path import join
from random import randint, choice
from background import Pista
from screen import *
from interactions import *
import imports

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.original_image = pygame.image.load(join('car_6.png')).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (48.5, 80))
        self.image = self.original_image
        self.rect = self.image.get_frect(center = (476, WINDOW_HEIGHT - 160))
        self.direction = pygame.math.Vector2()
        self.speed = 270
        self.rotation = 0
        self.block = 0

    def update(self, dt, size, surf):
        self.original_image = surf
        self.original_image = pygame.transform.scale(self.original_image, size)
        self.image = self.original_image
        self.rect = self.image.get_frect(center = (self.rect.center))
        if no_control(player, oil_sprites):
            self.block = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.block >= 1805 or pygame.time.get_ticks() < 1805:
            self.rotation = 0
            right = int(pygame.key.get_pressed()[pygame.K_d]) if self.rect.right < 687 else 0
            left = int(pygame.key.get_pressed()[pygame.K_a]) if self.rect.left > 265 else 0
            self.direction.x = right - left
            self.direction = self.direction.normalize() if self.direction else self.direction
        else:
            self.rotation += 200 * dt
            if self.rotation <= 360:
                self.image = pygame.transform.rotozoom(self.original_image, self.rotation, 1)
                self.rect = self.image.get_frect(center = self.rect.center)
            self.direction.x = 0
        self.rect.center += self.direction * self.speed * dt
class Random(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f'car_{randint(0,5)}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (48.5, 80))
        self.grid = [310, 407, 497, 595]
        self.rect = self.image.get_frect(bottomleft = (choice(self.grid), 0))
        self.direction = pygame.math.Vector2((0, 1))

    def update(self, scrool, dt):
        self.rect.center += self.direction * randint(scrool[0], scrool[1]) * dt
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

class Oil(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = (randint(290, 615), 0))
        self.direction = pygame.math.Vector2((0, 1))

    def update(self, scrool, dt):
        self.rect.center += self.direction * scrool * dt
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

class Slow(pygame.sprite.Sprite):
    def __init__(self, surf,  groups):
        super().__init__(groups)
        self.image = surf
        self.grid = [340, 430, 520, 617]
        self.rect = self.image.get_frect(midbottom = (choice(self.grid), 0))
        self.direction = pygame.math.Vector2((0, 1))

    def update(self, scrool, dt):
        self.rect.center += self.direction * scrool * dt
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

class Coins(pygame.sprite.Sprite):
    def __init__(self, frames, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.grid = [315, 407, 498, 593]
        self.rect = self.image.get_frect(bottomleft = (choice(self.grid), 0))
        self.direction = pygame.math.Vector2((0, 1))

    def update(self, scrool, dt):
        self.frame_index += 5 * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.center += self.direction * scrool * dt
        if self.rect.top > WINDOW_HEIGHT or collect_coins():
            self.kill()

class Nitro(pygame.sprite.Sprite):
    def __init__(self, surf,  groups):
        super().__init__(groups)
        self.image = surf
        self.grid = [340, 430, 520, 617]
        self.rect = self.image.get_frect(midbottom = (choice(self.grid), 0))
        self.direction = pygame.math.Vector2((0, 1))

    def update(self, scrool, dt):
        self.rect.center += self.direction * scrool * dt
        if self.rect.top > WINDOW_HEIGHT or collect_nitro():
            self.kill()

class Pill(pygame.sprite.Sprite):
    def __init__(self, surf,  groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(surf, (100, 100))
        self.grid = [340, 430, 520, 617]
        self.rect = self.image.get_frect(midbottom = (choice(self.grid), 0))
        self.direction = pygame.math.Vector2((0, 1))

    def update(self, scrool, dt):
        self.rect.center += self.direction * scrool * dt
        if self.rect.top > WINDOW_HEIGHT or collect_pill():
            self.kill()

class Star(pygame.sprite.Sprite):
    def __init__(self, surf,  groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(surf, (50, 50))
        self.grid = [340, 430, 520, 617]
        self.rect = self.image.get_frect(midbottom = (choice(self.grid), 0))
        self.direction = pygame.math.Vector2((0, 1))

    def update(self, scrool, dt):
        self.rect.center += self.direction * scrool * dt
        if self.rect.top > WINDOW_HEIGHT or collect_star():
            self.kill()

def collision():
    global time_not_collisions
    if used_star():
        time_not_collisions = pygame.time.get_ticks()
    if pygame.time.get_ticks() - time_not_collisions > 10000:
        if pygame.sprite.spritecollide(player, random_sprites, True, pygame.sprite.collide_mask):
             return True

def collect_coins():
    global qnt_moedas
    if pygame.sprite.spritecollide(player, coins_sprites, True, pygame.sprite.collide_mask):
        qnt_moedas += 1
        return True
    else:
        return False

def collect_nitro():
    global nitro_capacity
    if nitro_capacity < 4:
        if pygame.sprite.spritecollide(player, nitro_sprites, True, pygame.sprite.collide_mask):
            nitro_capacity += 1
            return True
        else:
            return False
    else:
        return False

def collect_pill():
    global pill
    global timer_pill
    if not pill:
        if pygame.sprite.spritecollide(player, pill_sprites, True, pygame.sprite.collide_mask):
            timer_pill = 7.00
            pill = True
            return True
        else:
            return False
    else:
        return False

def collect_star():
    global star
    global timer_star
    if not star:
        if pygame.sprite.spritecollide(player, star_sprites, True, pygame.sprite.collide_mask):
            timer_star = 8.00
            star = True
            return True
        else:
            return False
    else:
        return False

def used_nitro():
    global nitro_capacity
    global nitro_blocked
    if pygame.key.get_just_pressed()[pygame.K_SPACE] and nitro_capacity > 0 and pygame.time.get_ticks() - nitro_blocked > 3000:
        nitro_capacity -= 1
        nitro_blocked = pygame.time.get_ticks()
        return True
    else:
        return False

def used_pill():
    global pill
    global pill_blocked
    if pygame.key.get_just_pressed()[pygame.K_s] and pill and pygame.time.get_ticks() - pill_blocked > 7000:
        pill = False
        pill_blocked = pygame.time.get_ticks()
        return True
    else:
        return False

def used_star():
    global star
    global star_blocked
    global ghost
    if pygame.key.get_just_pressed()[pygame.K_r] and star and pygame.time.get_ticks() - star_blocked > 8000:
        star = False
        ghost = True
        star_blocked = pygame.time.get_ticks()
        return True
    else:
        return False

def size_display():

    global pontuacao, grey_pill, grey_star, timer_pill, timer_star, timer_init

    fps_surf = font_items.render(f'FPS: {clock.get_fps():.2f}', True, (20, 240, 50))
    dps_rect = fps_surf.get_rect(topleft = (20,20))
    display_surface.blit(fps_surf, dps_rect)

    coin_surf = pygame.image.load(join('images', 'coin_frames', 'frame-1.png'))
    coin_surf = pygame.transform.scale(coin_surf, (60, 60))
    coin_rect = coin_surf.get_rect(center=(WINDOW_WIDTH - 210, 90))

    display_surface.blit(coin_surf, coin_rect)
    num_coins_surf = font_coins.render(str(qnt_moedas), True, (240, 240, 240))
    num_coins_rect = num_coins_surf.get_frect(center=(WINDOW_WIDTH - 100, 100))
    display_surface.blit(num_coins_surf, num_coins_rect)

    timer_surf = font_dist.render(f'TIMER - {((pygame.time.get_ticks() - timer_init)/1000):.2f}', True, (240, 240, 240))
    timer_rect = timer_surf.get_rect(center=(WINDOW_WIDTH - 160, 240))
    display_surface.blit(timer_surf, timer_rect)

    dist_surf = font_dist.render(f'SCORE - {pontuacao}', True, (240, 240, 240))
    dist_rect = dist_surf.get_rect(center=(WINDOW_WIDTH - 160, 180))
    display_surface.blit(dist_surf, dist_rect)

    research_surf = batery_surf[nitro_capacity]
    research_rect = research_surf.get_rect(center=(WINDOW_WIDTH - 160, 320))
    display_surface.blit(research_surf, research_rect)

    show_nitro_surf = font_dist.render('NITRO RESEARCH', True, (240, 240, 240))
    show_nitro_rect = show_nitro_surf.get_rect(center=(WINDOW_WIDTH - 160, 375))
    display_surface.blit(show_nitro_surf, show_nitro_rect)

    show_time_pill = font_time.render(f'{timer_pill:.2f}', True, (240, 240, 240))
    time_pill_rect = show_time_pill.get_frect(center=(WINDOW_WIDTH - 220, 440))
    display_surface.blit(show_time_pill, time_pill_rect)
    show_time_star = font_time.render(f'{timer_star:.2f}', True, (240, 240, 240))
    time_star_rect = show_time_star.get_frect(center=(WINDOW_WIDTH - 85, 440))
    display_surface.blit(show_time_star, time_star_rect)

    item_pill_surf = pygame.transform.grayscale(pill_surf)
    item_pill_surf = pygame.transform.scale(item_pill_surf, (140, 140))
    if pill:
        grey_pill = pygame.time.get_ticks()
    if pygame.time.get_ticks() - grey_pill < 7000 and pygame.time.get_ticks() > 7000:
        item_pill_surf = pill_surf
        item_pill_surf = pygame.transform.scale(item_pill_surf, (140, 140))
    item_pill_rect = item_pill_surf.get_rect(center=(WINDOW_WIDTH - 220, 485))
    display_surface.blit(item_pill_surf, item_pill_rect)

    item_star_surf = pygame.transform.grayscale(star_surf)
    item_star_surf = pygame.transform.scale(item_star_surf, (67, 67))
    if star:
        grey_star = pygame.time.get_ticks()
    if pygame.time.get_ticks() - grey_star < 8000 and pygame.time.get_ticks() > 8000:
        item_star_surf = star_surf
        item_star_surf = pygame.transform.scale(item_star_surf, (67, 67))
    item_star_rect = item_star_surf.get_rect(center=(WINDOW_WIDTH - 85, 485))
    display_surface.blit(item_star_surf, item_star_rect)

    items_surf = font_items.render('REDUCTION PILL        MAGIC STAR', True, (240, 240, 240))
    items_rect = items_surf.get_rect(center=(WINDOW_WIDTH - 160, 550))
    display_surface.blit(items_surf, items_rect)

    rs_surf = font_key.render('PRESS S                              PRESS R', True, (240, 240, 240))
    rs_rect = rs_surf.get_rect(center=(WINDOW_WIDTH - 153, 570))
    display_surface.blit(rs_surf, rs_rect)

    special_surf = font_dist.render('SPECIAL ITEMS', True, (240, 240, 240))
    special_rect = special_surf.get_rect(center=(WINDOW_WIDTH - 160, 610))
    display_surface.blit(special_surf, special_rect)

    left_surf = font_key.render('LEFT', True, (240, 240, 240))
    left_rect = left_surf.get_rect(center=(WINDOW_WIDTH - 225, 680))
    display_surface.blit(left_surf, left_rect)
    a_surf = font_dist.render('A', True, (240, 240, 240))
    a_rect = a_surf.get_rect(center=(WINDOW_WIDTH - 185, 680))
    display_surface.blit(a_surf, a_rect)
    pygame.draw.rect(display_surface, (240, 240, 240), a_rect.inflate(20,5).move(0, -4), 2, 5)

    d_surf = font_dist.render('D', True, (240, 240, 240))
    d_rect = d_surf.get_rect(center=(WINDOW_WIDTH - 135, 680))
    display_surface.blit(d_surf, d_rect)
    pygame.draw.rect(display_surface, (240, 240, 240), d_rect.inflate(20, 5).move(0, -4), 2, 5)
    right_surf = font_key.render('RIGHT', True, (240, 240, 240))
    right_rect = right_surf.get_rect(center=(WINDOW_WIDTH - 90, 680))
    display_surface.blit(right_surf, right_rect)

def menu_sound(menu_music, game_music):
    game_music.stop()
    menu_music.set_volume(0.4)
    menu_music.play(-1)

def game_sound(menu_music, game_music):
    menu_music.stop()
    game_music.set_volume(0.4)
    game_music.play(-1)

# setup inicial
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 760
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
logo = pygame.image.load(join('images', 'logo.png'))
pygame.display.set_icon(logo)
pygame.display.set_caption('RaCIng 2D')
clock = pygame.time.Clock()
last_pontuacao, timer_init = 0, 0

# importando as fontes
font_base = pygame.font.Font('Oxanium-Bold.ttf')
font_coins = pygame.font.Font('Oxanium-Bold.ttf', 60)
font_dist = pygame.font.Font('Oxanium-Bold.ttf', 20)
font_items = pygame.font.Font('Oxanium-Bold.ttf', 15)
font_time = pygame.font.Font('Oxanium-Bold.ttf', 13)
font_key = pygame.font.Font('Oxanium-Bold.ttf', 12)

# importando os sprites
pista_surf = [pygame.image.load(join('images', f'pista-{0}.png')).convert_alpha() for i in range(6)]
pista_cin = pygame.image.load(join('images', f'pista-{1}.png')).convert_alpha()
pista_cin = pygame.transform.scale(pista_cin, (950, 1615))
pista_surf.append(pista_cin)
imports.cars()
oil_surf = pygame.image.load(join('images', 'oil.png')).convert_alpha()
oil_surf = pygame.transform.scale(oil_surf, (47, 47))
slow_surf = pygame.image.load(join('images', 'slow.png')).convert_alpha()
slow_surf = pygame.transform.scale(slow_surf, (40, 80))
coins_surf = [pygame.image.load(join('images', 'coin_frames', f'frame-{i}.png')).convert_alpha() for i in range(3)]
nitro_surf = pygame.image.load(join('images', 'nitro.png')).convert_alpha()
nitro_surf = pygame.transform.scale(nitro_surf, (40, 80))
batery_surf = [pygame.image.load(join('images', 'bateria', f'{i}.png')).convert_alpha() for i in range(5)]
batery_surf = [pygame.transform.scale(batery_surf[i], (100, 50)) for i in range(5)]
pill_surf = pygame.image.load(join('images', 'pill.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'magic_star.png')).convert_alpha()

# setup de encerramento
highscore_name = []
highscore = []
score = open('SCORE2D.txt', 'r')
contador = 0
for files in score:
    if contador < 5:
        files = files[:-1]
        highscore_name.append(files)
    else:
        highscore.append(int(files))
    contador += 1
score.close()

#importando as musicas
menu_music = pygame.mixer.Sound(join('audio', 'menu_music.mp3'))
game_music = pygame.mixer.Sound(join('audio', 'game_music.mp3'))

menu_sound(menu_music, game_music)

running = init(display_surface, clock, WINDOW_WIDTH, WINDOW_HEIGHT,highscore,highscore_name,font_base)
timer_init = pygame.time.get_ticks()

game_sound(menu_music, game_music)

while running:

    print('inicio')
    game = True
    exit, star, pill, ghost = False, False, False, False
    lapse_create = 5000
    last_time = pygame.time.get_ticks()
    scrool_all = 800
    scrool_random = [120, 125]
    time_slow, time_nitro, time_pill, time_ghost, time_not_collisions = 0, 0, 0, 0, 0
    qnt_moedas, index, nitro_capacity, nitro_blocked = 0, 0, 0, 0
    pill_blocked, star_blocked, grey_pill, grey_star = 0, 0, 0, 0
    timer_pill, timer_star = 0.00, 0.00

    #sprites
    player_sprites = pygame.sprite.Group()
    background_sprites = pygame.sprite.Group()
    oil_sprites = pygame.sprite.Group()
    random_sprites = pygame.sprite.Group()
    slow_sprites = pygame.sprite.Group()
    coins_sprites = pygame.sprite.Group()
    nitro_sprites = pygame.sprite.Group()
    pill_sprites = pygame.sprite.Group()
    star_sprites = pygame.sprite.Group()

    # setando a pista
    pista = Pista(index, pista_surf, WINDOW_HEIGHT, background_sprites, WINDOW_HEIGHT)

    # setando o player
    player = Player(player_sprites)

    # criando os eventos
    random_set = pygame.event.custom_type()
    pygame.time.set_timer(random_set, lapse_create)
    oil_set = pygame.event.custom_type()
    pygame.time.set_timer(oil_set, 5000)
    slow_set = pygame.event.custom_type()
    pygame.time.set_timer(slow_set, 6000)
    coins_set = pygame.event.custom_type()
    pygame.time.set_timer(coins_set, 800)
    nitro_set = pygame.event.custom_type()
    pygame.time.set_timer(nitro_set, 9000)
    pill_set = pygame.event.custom_type()
    pygame.time.set_timer(pill_set, 18000)
    star_set = pygame.event.custom_type()
    pygame.time.set_timer(star_set, 25000)

    while game:

        dt = clock.tick() / 1000
        pontuacao = (((pygame.time.get_ticks() - timer_init) // 100) + (qnt_moedas * 10))

        if pygame.time.get_ticks() - last_time > 9000:
            if lapse_create > 1100:
                lapse_create = difficult(lapse_create)
                last_time = pygame.time.get_ticks()
                if lapse_create < 1100:
                    lapse_create = 1100

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                exit = True
            if event.type == random_set:
                Random(random_sprites)
                pygame.time.set_timer(random_set, lapse_create)
            if event.type == nitro_set:
                Nitro(nitro_surf, nitro_sprites)
            if event.type == pill_set:
                Pill(pill_surf, pill_sprites)
            if event.type == star_set:
                Star(star_surf, star_sprites)
            if event.type == oil_set:
                Oil(oil_surf, oil_sprites)
            if event.type == slow_set:
                Slow(slow_surf, slow_sprites)
            if event.type == coins_set:
                Coins(coins_surf, coins_sprites)

        if pista.rect.top > -5:
            index += 1
            pista = Pista(index, pista_surf, WINDOW_HEIGHT, background_sprites)

        if slow(player, slow_sprites):
            time_slow = pygame.time.get_ticks()
        if (pygame.time.get_ticks() - time_slow < 6000) and (pygame.time.get_ticks() > 6000):
            scrool_all = 450
            scrool_random = [60, 62]
        else:
            if used_nitro():
                time_nitro = pygame.time.get_ticks()
            if (pygame.time.get_ticks() - time_nitro < 3000) and (pygame.time.get_ticks() > 3000):
                scrool_all = 1800
                scrool_random = [245, 250]
            else:
                scrool_all = 900
                scrool_random = [120, 125]

        if used_pill():
            time_pill = pygame.time.get_ticks()
        if pygame.time.get_ticks() - time_pill < 7000 and pygame.time.get_ticks() > 7000:
            timer_pill = (7000 - pygame.time.get_ticks() + time_pill) / 1000  if pygame.time.get_ticks() - time_pill < 7000 else 0
            size = (24.25, 40)
        else:
            size = (48.5, 80)

        if ghost:
            time_ghost = pygame.time.get_ticks()
            ghost = False
        if pygame.time.get_ticks() - time_ghost < 10000 and pygame.time.get_ticks() > 10000:
            timer_star = (8000 - pygame.time.get_ticks() + time_ghost) / 1000 if pygame.time.get_ticks() - time_ghost < 8000 else 0.00
            player_surf = pygame.image.load(join('images', 'ghost.png')).convert_alpha()
        else:
            player_surf = pygame.image.load('car_6.png').convert_alpha()

        # update
        background_sprites.update(scrool_all, dt)
        oil_sprites.update(scrool_all, dt)
        player_sprites.update(dt, size, player_surf)
        random_sprites.update(scrool_random, dt)
        slow_sprites.update(scrool_all, dt)
        coins_sprites.update(scrool_all, dt)
        nitro_sprites.update(scrool_all, dt)
        pill_sprites.update(scrool_all, dt)
        star_sprites.update(scrool_all, dt)

        # printagem do frame
        display_surface.fill('black')
        background_sprites.draw(display_surface)
        oil_sprites.draw(display_surface)
        slow_sprites.draw(display_surface)
        nitro_sprites.draw(display_surface)
        pill_sprites.draw(display_surface)
        star_sprites.draw(display_surface)
        coins_sprites.draw(display_surface)
        random_sprites.draw(display_surface)
        player_sprites.draw(display_surface)
        size_display()
        pygame.display.update()

        # game over
        if collision():
            game = False

    if exit == False:
        menu_sound(menu_music, game_music)
        running = end(font_base, WINDOW_WIDTH, WINDOW_HEIGHT, pontuacao, highscore_name, highscore, qnt_moedas)
        if running:
            game_sound(menu_music, game_music)
            last_pontuacao = pontuacao
            timer_init = pygame.time.get_ticks()

    else:
        running = False

pygame.quit()