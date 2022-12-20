import pygame
from pygame.locals import *

class Background(pygame.sprite.Sprite):
    def __init__(self, sprite, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height
        self.image = sprite

        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

    def update(self):
        self.image = pygame.transform.scale(self.image, (self.width, self.height))