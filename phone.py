import pygame
from pygame.locals import *

class Phone(pygame.sprite.Sprite):
    def __init__(self, spritesheet, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.current_animation = []

        self.image = spritesheet.subsurface((0, 6*32), (32, 32))

        self.rect = self.image.get_rect()
        self.rect.topleft = posX,posY

        self.sprites = []

         # Pega as sprites IDLE
        self.idle_sprites_frames = 6
        for i in range(self.idle_sprites_frames):
            # Idle
            idle = spritesheet.subsurface((i*32, 224), (32, 32))
            self.sprites.append(idle)

        self.animate = True
        self.animation_speed = 0.35

        # Configuração inicial da animação
        self.animation_index = 0
        self.image = self.sprites[self.animation_index]
        self.current_animation = self.sprites

    def update(self):
        if self.animate == True:
            self.animation_index = self.animation_index + self.animation_speed
            if self.animation_index >= len(self.current_animation):
                self.animation_index = 0
            self.image = self.current_animation[int(self.animation_index)]
            self.image = pygame.transform.scale(self.image, (32*3, 32*3))

    def setPos(self, x, y):
        self.rect.topleft = x, y
    
    