# config.py

import pygame

# Constantes do Jogo
LARGURA_TELA = 400
ALTURA_TELA = 600
VELOCIDADE_PISTA = 3
INTERVALO_OBSTACULOS = 700 # Milissegundos

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Ajuste manual das posições X de cada faixa para centralizar o carro.
POSICOES_FAIXAS = [108, 168, 230, 290]

# Lista com os nomes dos arquivos de imagem dos carros inimigos
IMAGENS_OBSTACULOS = [
    'obstacle_compact_blue.png',
    'obstacle_coupe_midnight.png',
    'obstacle_sedan_gray.png',
    'obstacle_sport_green.png'
]
MUSICA_FUNDO = 'assets/sons/8-bit.mp3'