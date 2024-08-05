import pygame
from os.path import join

def cars():
    sprite_index = 0
    sprite_corredores = pygame.image.load(join('images', 'spritesheet_oficial.png'))
    sprite_width = sprite_corredores.get_width() // 5
    sprite_height = sprite_corredores.get_height() // 2
    for row in range(2):
        for col in range(5):
            x = col * 112
            y = row * 192
            rect = pygame.Rect(x, y, sprite_width, sprite_height)
            sprite = sprite_corredores.subsurface(rect)
            sprite = pygame.transform.scale(sprite, (79, 130))
            sprite_path = f"car_{sprite_index}.png"
            pygame.image.save(sprite, sprite_path)
            sprite_index += 1