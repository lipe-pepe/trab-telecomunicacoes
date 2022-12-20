import pygame
from pygame.locals import *

class Door(pygame.sprite.Sprite):
    def __init__(self, spritesheet, posX, posY):
        pygame.sprite.Sprite.__init__(self)

        self.image = spritesheet.subsurface((9*32, 0), (32, 32))

        self.rect = self.image.get_rect()
        self.rect.topleft = posX, posY

    def update(self):
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))

    def setPos(self, x, y):
        self.rect.topleft = x, y