import pygame

class Pista(pygame.sprite.Sprite):
    def __init__(self, index, pistas, height, groups, y = 0):
        super().__init__(groups)
        self.pistas = pistas
        self.pistas_index = index % len(self.pistas)
        self.image = pistas[self.pistas_index]
        if index % len(self.pistas) < 6:
            self.image = pygame.transform.scale(self.image, (950, 4000))
        self.rect = self.image.get_frect(bottomleft = (0, y))
        print(self.rect.right)
        self.direction = pygame.math.Vector2(0, 1)
        self.height = height

    def update(self, scrool, dt):
        self.rect.center += self.direction * dt * scrool
        if self.rect.top > self.height:
            self.kill()