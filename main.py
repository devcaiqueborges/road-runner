import pygame
import sys
import random

from config import *
from jogador import Jogador
from obstaculo import Obstaculo

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Road Runner Demo")

try:
    fundo_pista = pygame.image.load('assets/background-1.png').convert()
    fundo_pista = pygame.transform.scale(fundo_pista, (LARGURA_TELA, ALTURA_TELA))
    pygame.mixer.music.load(MUSICA_FUNDO)
except pygame.error:
    print("Ops, não achei a imagem 'assets/background-1.png'. Verifique a pasta.")
    sys.exit()

# efeito de rolagem infinita do fundo
fundo_pista_rect1 = fundo_pista.get_rect(topleft=(0, 0))
fundo_pista_rect2 = fundo_pista.get_rect(topleft=(0, -ALTURA_TELA))


def tela_final(pontuacao):
    pygame.mixer.music.stop()

    fonte_grande = pygame.font.Font(None, 48)
    fonte_pequena = pygame.font.Font(None, 32)

    texto_game_over = fonte_grande.render("GAME OVER", True, BRANCO)
    texto_pontuacao = fonte_pequena.render(f"Pontuacao Final: {pontuacao}", True, BRANCO)
    texto_instrucao = fonte_pequena.render("Pressione R para reiniciar ou Q para sair", True, BRANCO)

    esperando_input = True
    while esperando_input:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    iniciar_jogo()
                if evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        tela.fill(PRETO)
        tela.blit(texto_game_over, (LARGURA_TELA / 2 - texto_game_over.get_width() / 2, ALTURA_TELA / 2 - 60))
        tela.blit(texto_pontuacao, (LARGURA_TELA / 2 - texto_pontuacao.get_width() / 2, ALTURA_TELA / 2))
        tela.blit(texto_instrucao, (LARGURA_TELA / 2 - texto_instrucao.get_width() / 2, ALTURA_TELA / 2 + 40))
        pygame.display.flip()


def iniciar_jogo():
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

    jogo_rodando = True
    clock = pygame.time.Clock()
    fonte = pygame.font.Font(None, 36)

    tempo_inicial = pygame.time.get_ticks()
    timer_obstaculos = pygame.time.get_ticks()

    grupo_sprites = pygame.sprite.Group()
    grupo_obstaculos = pygame.sprite.Group()

    jogador = Jogador()
    grupo_sprites.add(jogador)

    while jogo_rodando:
        clock.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jogador.mudar_faixa('esquerda')
                if evento.key == pygame.K_RIGHT:
                    jogador.mudar_faixa('direita')

        fundo_pista_rect1.y += VELOCIDADE_PISTA
        fundo_pista_rect2.y += VELOCIDADE_PISTA
        if fundo_pista_rect1.top >= ALTURA_TELA:
            fundo_pista_rect1.bottom = fundo_pista_rect2.top
        if fundo_pista_rect2.top >= ALTURA_TELA:
            fundo_pista_rect2.bottom = fundo_pista_rect1.top

        agora = pygame.time.get_ticks()
        if agora - timer_obstaculos > INTERVALO_OBSTACULOS:
            timer_obstaculos = agora
            imagem_aleatoria = random.choice(IMAGENS_OBSTACULOS)
            novo_obstaculo = Obstaculo(imagem_aleatoria)

            if not pygame.sprite.spritecollideany(novo_obstaculo, grupo_obstaculos):
                grupo_sprites.add(novo_obstaculo)
                grupo_obstaculos.add(novo_obstaculo)

        if pygame.sprite.spritecollideany(jogador, grupo_obstaculos):
            jogo_rodando = False

        pontuacao = (pygame.time.get_ticks() - tempo_inicial) // 1000

        grupo_sprites.update()

        tela.fill(PRETO)
        tela.blit(fundo_pista, fundo_pista_rect1)
        tela.blit(fundo_pista, fundo_pista_rect2)
        grupo_sprites.draw(tela)

        texto_score = fonte.render(f"SCORE: {pontuacao}", True, BRANCO)
        tela.blit(texto_score, (10, 10))

        pygame.display.flip()

    tela_final(pontuacao)


if __name__ == "__main__":
    iniciar_jogo()