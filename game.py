# Instalar a lib pygame
# pip install pygame --pre

# --- IMPORTAÇÕES -------------------------------------------------------------------------------------------------------------------- #

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

# ----------------------------------------------------------------------------------------------------------------------- #

# Variáveis de controle do jogador:
posX = largura_janela/2
posY = altura_janela/2
velocidade = 5
direcaoX = 0
direcaoY = 0

# Cria o loop do jogo
while True:
    clock.tick(30)
    # Limpa a tela do jogo:
    tela.fill((0,0,0))
    # A cada iteração do loop principal, o loop a seguir vai checar os eventos
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
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

    pygame.draw.rect(tela, (0,255,128), (posX, posY, 40, 50))
    
    # Movimentação do personagem
    posY = posY+(velocidade*direcaoY)
    posX = posX+(velocidade*direcaoX)

    if (posY >= altura_janela):
        posY = 0
    
    if (posX >= largura_janela):
        posX = 0

    if (posY < 0):
        posY = altura_janela
    
    if (posX < 0):
        posX = largura_janela

    # Atualiza a tela a cada iteração do loop principal
    pygame.display.update()
