import pygame

def no_control(player, oil_sprites):
    if pygame.sprite.spritecollide(player, oil_sprites, False, pygame.sprite.collide_mask):
        return True
    else:
        return False

def slow(player, slow_sprites):
    if pygame.sprite.spritecollide(player, slow_sprites, False, pygame.sprite.collide_mask):
        return True
    else:
        return False

def difficult(lapse):
    return int(lapse*(9/10))