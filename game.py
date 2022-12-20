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
from audio import *

# Importa classes do jogo
from player import *
from box import *
from phone import *
from enemy import *
from background import *
from door import *

# --- CONFIGURAÇÕES INICIAIS -------------------------------------------------------------------------------------------------------------------- #

# Inicializa o pygame
pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')

# Cria a janela do jogo
largura_janela = 800
altura_janela = 600

level = 1

screen = pygame.display.set_mode((largura_janela, altura_janela))

# Configura o nome da janela
titulo = "Trabalho Telecomunicações"
pygame.display.set_caption(titulo)

clock = pygame.time.Clock()

fonte = pygame.font.Font('fontes/upheavtt.ttf', 40, bold=True, italic=False)

game_over = False

colision_phone = False

all_sprites = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
phone_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()

# Carrega a spritesheet conservando a transparência do alpha.
spritesheet = pygame.image.load(os.path.join(diretorio_imagens, 'Spritesheet.png')).convert_alpha()

mensagem = ""

# --- Instanciando objetos ---   

background_image = pygame.image.load(os.path.join(diretorio_imagens, 'Background.png')).convert_alpha()
background = Background(background_image, largura_janela, altura_janela) 
all_sprites.add(background)   


door = Door(spritesheet, 670, 0) 
all_sprites.add(door) 
door_group.add(door)

box = Box(spritesheet, 350, 40)
all_sprites.add(box)
obstacles_group.add(box)

box2 = Box(spritesheet, 350, 120)
all_sprites.add(box2)
obstacles_group.add(box2)

box3 = Box(spritesheet, -10350, -1120)
all_sprites.add(box3)
obstacles_group.add(box3)

player = Player(spritesheet, 20, 50)
all_sprites.add(player)

enemy = Enemy(spritesheet, 400, 400)
all_sprites.add(enemy)
enemies_group.add(enemy)

enemy2 = Enemy(spritesheet, -1400, -1400)
all_sprites.add(enemy2)
enemies_group.add(enemy2)

phone = Phone(spritesheet, 300, 300)
all_sprites.add(phone)
phone_group.add(phone)


# --- Níveis ---

def setLevel1():
    global player, phone, box, door, index_comando, comandos

    index_comando = 0
    comandos = []

    player.stop()
    player.setPos(20, 50)

    door.setPos(670, 0)
    box.setPos(350, 50)
    phone.setPos(-1000, -1000)
    enemy.setPos(-1000, -1000)

    

def setLevel2():
    global player, phone, box, door, index_comando, comandos

    index_comando = 0
    comandos = []

    player.stop()
    player.setPos(20, 50)

    door.setPos(450, 0)
    box.setPos(30, 430)
    box2.setPos(675, 50)
    box3.setPos(510, 390)
    enemy.setPos(190, 40)
    enemy2.setPos(280, 280)

    

def setLevel3():
    global player, phone, box, door, index_comando, comandos

    index_comando = 0
    comandos = []

    player.stop()
    player.setPos(650, 450)

    door.setPos(30, 0)
    box.setPos(300, 150)
    box2.setPos(240, 450)
    phone.setPos(560, 180)
    enemy.setPos(30, 180)
    enemy2.setPos(650, 180)


def levelManager():
    global level, mensagem
    if level == 1:
        setLevel1()
    elif level == 2:
        setLevel2()
    elif level == 3:
        setLevel3()
    elif level == 4:
        mensagem = " - Você ganhou! - "

    

# --- Controle de voz ---

index_comando = 0
numero_comandos = 0
comandos = []
collided = False

def voice_command_manager():
    global comandos, index_comando, numero_comandos
    comando_voz = ouvir_microfone()
    comandos = definir_comandos_jogo(comando_voz)
    index_comando = 0
    numero_comandos = len(comandos)
    move()


def move():
    global comandos, index_comando, player

    if index_comando >= numero_comandos:
        index_comando = 0
        comandos = []
    else:
        # print(comandos)
        comando_atual = comandos[index_comando] 
        index_comando += 1
        
        # Checa todos os comandos possíveis
        if "esquerda" in comando_atual:   
            # print("Foi pra esquerda")
            player.dirX = -1
            player.dirY = 0
        if "direita" in comando_atual:
            # print("Foi pra direita")   
            player.dirX = 1
            player.dirY = 0
        if "cima" in comando_atual: 
            # print("Foi pra cima")  
            player.dirX = 0
            player.dirY = -1
        if "baixo" in comando_atual: 
            # print("Foi pra baixo")  
            player.dirX = 0
            player.dirY = 1


def movement_manager():
    global comandos, collided
    if comandos:
        # Checa colisões
        for objeto in obstacles_group:
            if (player.rect.right >= objeto.rect.left and player.rect.right <= objeto.rect.right):
                if (player.rect.bottom >= objeto.rect.top and player.rect.bottom <= objeto.rect.bottom) or (player.rect.top >= objeto.rect.bottom and player.rect.top <= objeto.rect.top):
                    if (player.dirY == -1):
                        player.rect.topleft = player.rect.left - 10, player.rect.top + 10
                    elif (player.dirY == 1):
                        player.rect.topleft = player.rect.left - 10, player.rect.top - 10
                    else:
                        player.rect.topleft = player.rect.left - 10, player.rect.top
                    # print ("COLIDIU 1!") 
                    move() 
            if (player.rect.left >= objeto.rect.left and player.rect.left <= objeto.rect.right):
                if (player.rect.bottom >= objeto.rect.top and player.rect.bottom <= objeto.rect.bottom) or (player.rect.top >= objeto.rect.bottom and player.rect.top <= objeto.rect.top):
                    player.rect.topleft = player.rect.left + 20, player.rect.top
                    # print ("COLIDIU 2!") 
                    move() 
                                     

        if player.rect.left <= 0:
            player.rect.topleft = player.rect.left + 20, player.rect.top
            # print ("COLIDIU!") 
            move()
        if  player.rect.right >= largura_janela-100:
            player.rect.topleft = player.rect.left - 5, player.rect.top
            # print ("COLIDIU!") 
            move()
        if player.rect.bottom >= altura_janela-100:
            player.rect.topleft = player.rect.left, player.rect.top - 10
            # print ("COLIDIU!") 
            move()
        if player.rect.top <= 0:
            player.rect.topleft = player.rect.left, player.rect.top + 20
            # print ("COLIDIU!") 
            move()
    else:
        player.stop()

# ----------------------------------------------------------------------------------------------------------------------- #

# Inicia nível
levelManager()

# Cria o loop do jogo
while True:
    clock.tick(30)
    # Limpa a screen do jogo:
    screen.fill((0, 0, 0))

    # TEXTO DO JOGO:
    texto_formatado = fonte.render(mensagem, True, (140 , 255, 155), (0,0,0))

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
            if event.key == K_SPACE and level < 4:
                # --- Ouve o comando por voz ---
                voice_command_manager()
                    
    # Checa colisões
    if (not colision_phone):
        colision_phone = pygame.sprite.spritecollide(player, phone_group, True) 
        if colision_phone:
            voice_command_manager()

    # Checa colisões com inimigos
    if pygame.sprite.spritecollide(player, enemies_group, False) :
        levelManager()

    # Checa colisão com a porta
    if (pygame.sprite.spritecollide(player, door_group, False) ):
        if level < 4:
            level += 1
            levelManager()
        
    movement_manager()
    
    # Movimentação do personagem        
    player.rect.y = player.rect.y+(player.speed*player.dirY)
    player.rect.x = player.rect.x+(player.speed*player.dirX)

    all_sprites.draw(screen)
    all_sprites.update()

    screen.blit(texto_formatado, (largura_janela/2 - 170,altura_janela/2 - 60))

    # Atualiza a screen a cada iteração do loop principal
    pygame.display.update()
