import pygame
from pygame.locals import *

class Box(pygame.sprite.Sprite):
    def __init__(self, spritesheet):
        pygame.sprite.Sprite.__init__(self)

        self.image = spritesheet.subsurface((0, 6*32), (32, 32))

        self.rect = self.image.get_rect()
        self.rect.topleft = 300,100

    def update(self):
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
    
    