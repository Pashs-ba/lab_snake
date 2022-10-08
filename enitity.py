import pygame


class BaseSprite(pygame.sprite.Sprite):
    size = 10

    def __init__(self, x, y):
        super().__init__()
        self.image: pygame.Surface = pygame.Surface((self.size, self.size))
        self.rect: pygame.Rect = pygame.Rect((x, y, self.size, self.size))
