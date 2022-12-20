import pygame
from pygame.locals import *

# A classe player herda da classe Sprite.
class Player(pygame.sprite.Sprite):
    def __init__(self, spritesheet, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.current_animation = []

        self.idle_sprites = []
        self.walk_down_sprites = []
        self.walk_up_sprites = []
        self.walk_left_sprites = []
        self.walk_right_sprites = []

        # Pega as sprites IDLE
        self.idle_sprites_frames = 8
        for i in range(self.idle_sprites_frames):
            # Idle
            idle = spritesheet.subsurface((i*32, 128), (32, 32))
            self.idle_sprites.append(idle)

        # Pega as sprites WALK
        self.walk_sprites_frames = 4
        for i in range(self.walk_sprites_frames):
            # Walk
            down = spritesheet.subsurface((i*32, 0), (32, 32))
            up = spritesheet.subsurface((i*32, 32), (32, 32))
            right = spritesheet.subsurface((i*32, 64), (32, 32))
            left = spritesheet.subsurface((i*32, 96), (32, 32))      
            self.walk_down_sprites.append(down)
            self.walk_left_sprites.append(left)
            self.walk_up_sprites.append(up)
            self.walk_right_sprites.append(right)

        # Configuração inicial da animação
        self.animation_index = 0
        self.image = self.walk_down_sprites[self.animation_index]
        self.current_animation = self.walk_down_sprites

        self.animate = True
        self.animation_speed = 0.35
 
        self.rect = self.image.get_rect()
        self.rect.topleft = posX,posY

        # Movimentação
        self.speed = 5
        self.dirX = 0
        self.dirY = 0

        self.comandos = []
        self.index_comando = 0

    def update(self):
        if self.animate == True:
            # Animação ANDANDO
            if self.dirX != 0 or self.dirY != 0:
                if self.dirY == 1:
                    self.current_animation = self.walk_down_sprites
                if self.dirY == -1:
                    self.current_animation = self.walk_up_sprites
                if self.dirX == 1:
                    self.current_animation = self.walk_right_sprites
                if self.dirX == -1:
                    self.current_animation = self.walk_left_sprites
            else:
                self.current_animation = self.idle_sprites

            self.animation_index = self.animation_index + self.animation_speed
            if self.animation_index >= len(self.current_animation):
                self.animation_index = 0
            self.image = self.current_animation[int(self.animation_index)]
            self.image = pygame.transform.scale(self.image, (32*3, 32*3))

    def stop(self):
        self.dirX = 0
        self.dirY = 0
        self.current_animation = self.idle_sprites

    def setPos(self, x, y):
        self.rect.topleft = x, y


    
