import pygame
from pygame.locals import *

# Tamanho da tela
largura = 1000
altura = 700

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 39, 118)
amarelo = (255, 253, 0)
verde = (0, 156, 59)


def desenhar():
    pygame.draw.polygon(tela, amarelo,
                        ((85, altura / 2), (largura / 2, 85), (largura - 85, altura / 2), (largura / 2, altura - 85)))
    pygame.draw.circle(tela, azul, (largura / 2, altura / 2), 175)


tela = pygame.display.set_mode((largura, altura))

while True:
    tela.fill(verde)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        desenhar()

        pygame.display.update()
