# jogador.py

import pygame
from config import *  # Importa todas as constantes (ALTURA_TELA, POSICOES_FAIXAS, etc)


class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            imagem_original = pygame.image.load('assets/player.png').convert_alpha()
        except pygame.error:
            print("Ops, não achei a imagem 'assets/player.png'. Verifique a pasta.")
            sys.exit()

        self.image = pygame.transform.scale(imagem_original, (45, 90))
        self.rect = self.image.get_rect()

        self.faixa_atual = 1
        self.rect.centerx = POSICOES_FAIXAS[self.faixa_atual]
        self.rect.bottom = ALTURA_TELA - 40

    def update(self):
        self.rect.centerx = POSICOES_FAIXAS[self.faixa_atual]

    def mudar_faixa(self, direcao):
        if direcao == 'esquerda':
            self.faixa_atual = max(0, self.faixa_atual - 1)
        elif direcao == 'direita':
            self.faixa_atual = min(len(POSICOES_FAIXAS) - 1, self.faixa_atual + 1)