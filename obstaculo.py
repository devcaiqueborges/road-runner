# obstaculo.py

import pygame
import random
from config import *  # Importa todas as constantes


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, nome_arquivo_imagem):
        super().__init__()
        try:
            imagem_original = pygame.image.load(f'assets/{nome_arquivo_imagem}').convert_alpha()
        except pygame.error:
            print(f"Ops, não achei a imagem 'assets/{nome_arquivo_imagem}'. Verifique a pasta.")
            sys.exit()

        self.image = pygame.transform.scale(imagem_original, (40, 70))
        self.rect = self.image.get_rect()

        indice_faixa = random.randrange(len(POSICOES_FAIXAS))
        self.rect.centerx = POSICOES_FAIXAS[indice_faixa]
        self.rect.y = random.randrange(-150, -50)
        self.velocidade_y = random.randrange(4, 7)

    def update(self):
        self.rect.y += self.velocidade_y
        if self.rect.top > ALTURA_TELA:
            self.kill()