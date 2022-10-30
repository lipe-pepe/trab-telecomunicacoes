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

# Importa as funções de reconhecimento de fala
from audio import ouvir_microfone

# --- CONFIGURAÇÕES INICIAIS -------------------------------------------------------------------------------------------------------------------- #

# Inicializa o pygame
pygame.init()

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

def reiniciar_jogo():
    global pontuacao, comprimento, lista_cabeca, lista_cobra, x_item, y_item, game_over, y_player, y_player
    pontuacao = 0
    comprimento = comprimento_inicial
    x_player = largura_janela/2
    y_player = altura_janela/2
    lista_cabeca = []
    lista_cobra = []
    x_item = randint(40, 600)
    y_item = randint(50, 430)
    game_over = False

# --- PLAYER -------------------------------------------------------------------------------------------------------------------- #

# A classe player herda da classe Sprite.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.walk_down_sprites = []
        self.walk_down_sprites.append(pygame.image.load('sprites\player\walk\down_0.png'))

# Variáveis do jogador:
x_player = largura_janela/2
y_player = altura_janela/2
velocidade = 7
direcaoX = 1
direcaoY = 0

# Variáveis de movimento:  
comprimento_inicial = 3 
comprimento = comprimento_inicial
crescimento = 3

# Todas as posições que a cobra já teve:
lista_cobra = []

def aumenta_cobra(lista_cobra):
    for pos in lista_cobra:
        pygame.draw.rect(tela, (0,255,128), (pos[0], pos[1], 20, 20))

# Variáveis do item:
x_item = randint(40, 600)
y_item = randint(50, 430)

# Variáveis de jogo:
pontuacao = 0

# ----------------------------------------------------------------------------------------------------------------------- #

# Cria o loop do jogo
while True:
    clock.tick(30)
    # Limpa a tela do jogo:
    tela.fill((0,0,0))

    # Texto:
    mensagem = f'Pontos: {pontuacao}'
    textoFormatado = fonte.render(mensagem, True, (255, 255, 255))
    # A cada iteração do loop principal, o loop a seguir vai checar os eventos
    for event in pygame.event.get():     
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a and direcaoX == 0:
                direcaoX = -1
                direcaoY = 0
            if event.key == K_s and direcaoY == 0:
                direcaoX = 0
                direcaoY = 1
            if event.key == K_d and direcaoX == 0:
                direcaoX = 1
                direcaoY = 0
            if event.key == K_w and direcaoY == 0:
                direcaoX = 0
                direcaoY = -1
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
                        direcaoX = -1
                        direcaoY = 0
                    if "direita" in comando_voz:   
                        direcaoX = 1
                        direcaoY = 0
                    if "cima" in comando_voz:   
                        direcaoX = 0
                        direcaoY = -1
                    if "baixo" in comando_voz:   
                        direcaoX = 0
                        direcaoY = 1


    player = pygame.draw.rect(tela, (0,255,128), (x_player, y_player, 20, 20))

    item = pygame.draw.rect(tela, (255,32,0), (x_item, y_item, 20, 20))

    # Checa a colisão do player com o item
    if player.colliderect(item):
        x_item = randint(40, 600)
        y_item = randint(50, 430)
        pontuacao = pontuacao+1
        comprimento = comprimento+crescimento

    # Posição atual da cabeca da cobra:
    lista_cabeca = []
    lista_cabeca.append(x_player)
    lista_cabeca.append(y_player)

    lista_cobra.append(lista_cabeca)

    # Se tiverem mais de um elementos igual a lista_cabeca na cobra, ela encostou em si mesma:
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'GAME OVER! Pressione R para reiniciar'
        textoFormatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = textoFormatado.get_rect()
        game_over =  True
        while game_over:
            # Limpa a tela do jogo:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()    
            ret_texto.center = (largura_janela//2, 20)
            tela.blit(textoFormatado, ret_texto)
            # Atualiza a tela a cada iteração do loop principal
            pygame.display.update()

    if (y_player > altura_janela):
        y_player = 0
    if (x_player > largura_janela):
        x_player = 0
    if (y_player < 0):
        y_player = altura_janela
    if (x_player < 0):
        x_player = largura_janela

    if len(lista_cobra) > comprimento:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    
    # Movimentação do personagem
    y_player = y_player+(velocidade*direcaoY)
    x_player = x_player+(velocidade*direcaoX)

    tela.blit(textoFormatado, (20, 20))
    # Atualiza a tela a cada iteração do loop principal
    pygame.display.update()
