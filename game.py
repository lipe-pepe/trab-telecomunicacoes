# Instalar a lib pygame
#  

# --- IMPORTAÇÕES -------------------------------------------------------------------------------------------------------------------- #

from random import randint
from re import S
# Importa todas as funções e constantes do pygame
import pygame
from pygame.locals import *

# Função que fechará a janela do jogo
from sys import exit
import os

# Importa as funções de reconhecimento de fala
from audio import ouvir_microfone

# Importa classes do jogo
from player import *
from box import *

# --- CONFIGURAÇÕES INICIAIS -------------------------------------------------------------------------------------------------------------------- #

# Inicializa o pygame
pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')

# Cria a janela do jogo
largura_janela = 640
altura_janela = 480

tela = pygame.display.set_mode((largura_janela, altura_janela))

# Configura o nome da janela
titulo = "Trabalho Telecomunicações"
pygame.display.set_caption(titulo)

clock = pygame.time.Clock()

fonte = pygame.font.SysFont('arial', 40, bold=True, italic=False)

game_over = False

all_sprites = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()

# Carrega a spritesheet conservando a transparência do alpha.
spritesheet = pygame.image.load(os.path.join(diretorio_imagens, 'Spritesheet.png')).convert_alpha()

# Instanciando objetos            

box = Box(spritesheet)
all_sprites.add(box)
obstacles_group.add(box)

player = Player(spritesheet)
all_sprites.add(player)



# ----------------------------------------------------------------------------------------------------------------------- #

# Cria o loop do jogo
while True:
    clock.tick(30)
    # Limpa a tela do jogo:
    tela.fill((255,255,240))

    # A cada iteração do loop principal, o loop a seguir vai checar os eventos
    for event in pygame.event.get():     
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                player.dirX = -1
                player.dirY = 0
            if event.key == K_s:
                player.dirX = 0
                player.dirY = 1
            if event.key == K_d:
                player.dirX = 1
                player.dirY = 0
            if event.key == K_w:
                player.dirX = 0
                player.dirY = -1
            if event.key == K_SPACE:
                # --- Ouve o comando por voz ---
                comando_voz = ouvir_microfone()
                if type(comando_voz) is str:
                    # Passamos para letras minúsculas para evitar erros
                    comando_voz = comando_voz.lower()
                    # Checa todos os comandos possíveis
                    if "fechar" in comando_voz:   
                        pygame.quit()
                        exit()
                    if "esquerda" in comando_voz:   
                        player.dirX = -1
                        player.dirY = 0
                    if "direita" in comando_voz:   
                        player.dirX = 1
                        player.dirY = 0
                    if "cima" in comando_voz:   
                        player.dirX = 0
                        player.dirY = -1
                    if "baixo" in comando_voz:   
                        player.dirX = 0
                        player.dirY = 1 

    # Checa colisões
    colisions = pygame.sprite.spritecollide(player, obstacles_group, False) 
    if colisions:
        player.dirX = 0
        player.dirY = 0 
    
    # Movimentação do personagem        
    player.rect.y = player.rect.y+(player.speed*player.dirY)
    player.rect.x = player.rect.x+(player.speed*player.dirX)

    all_sprites.draw(tela)
    all_sprites.update()

    # Atualiza a tela a cada iteração do loop principal
    pygame.display.update()
