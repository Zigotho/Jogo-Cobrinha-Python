from os import environ
import pygame as pg
from pygame.locals import *
from Sistemas import *


environ['SDL_VIDEO_CENTERED'] = '1'

cima = 0
direita = 1
baixo = 2
esquerda = 3
funcionando = False

pontos = 0
altura = Desenhos.altura
largura = Desenhos.largura
Dourada = False
porcentagem = 0
abrir = open('highscore.txt', 'r')
hs = int(abrir.read())
print(funcionando)


pg.init()
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption("Jogo da Cobra")
pg.display.set_icon(Desenhos.icone)
pg.font.init()
fonte_padrao = pg.font.get_default_font()
texto = pg.font.SysFont(fonte_padrao, 30)

maca = Desenhos.maca
macaDourada = Desenhos.macaDourada

cobra = Desenhos.cobra.getcobra_pos()
cobra_skin = Desenhos.cobra.Imagem_cobra
parede = Desenhos.parede
mato = Desenhos.mato
chao = Desenhos.chao
maca_pos = no_grid_aleatorio()
fps = pg.time.Clock()
direcao = esquerda
while True:
    tela.fill((255, 255, 255))
    fps.tick(10)

# ~~~~~~~~~~~~~~Controles~~~~~~~~~~~~~~~
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and not direcao == baixo:
                direcao = cima
            if event.key == K_RIGHT and not direcao == esquerda:
                direcao = direita
            if event.key == K_DOWN and not direcao == cima:
                direcao = baixo
            if event.key == K_LEFT and not direcao == direita:
                direcao = esquerda
            if event.key == K_r:
                funcionando = True
                direcao = esquerda
                pontos = 0
                Dourada = False
                maca = Desenhos.maca

# ~~~~~~~~~~~~~~Controle das colisoes~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~Colisao com a maça~~~~~~~~~~~~~~~
    if colisao(cobra[0], maca_pos):
        maca_pos = no_grid_aleatorio()
        cobra.append((0, 0))
        if Dourada:
            cobra.append((0, 0))
            pontos += 20
        else:
            pontos += 10
        porcentagem = random.randrange(0, 10)
        if porcentagem > 8:
            Dourada = True
            maca = macaDourada
        else:
            Dourada = False
            maca = Desenhos.maca
    # ~~~~~~~~~~~~~~Colisao com a cobra~~~~~~~~~~~~~~~
    for j in range(len(cobra) - 1, 1, -1):
        if cobra[0] == cobra[j]:
            funcionando = False
            cobra = Desenhos.cobra.getcobra_pos()
            direcao = esquerda
            maca_pos = no_grid_aleatorio()
            if pontos > hs:
                abrir = open('highscore.txt', 'w')
                abrir.write(str(pontos))
                hs = pontos
    # ~~~~~~~~~~~~~~Colisao com a Parede~~~~~~~~~~~~~~~
    if cobra[0][0] >= largura-40 or cobra[0][1] >= altura-40 or cobra[0][0] <= 40 or cobra[0][1] <= 40:
        funcionando = False
        cobra = Desenhos.cobra.getcobra_pos()
        direcao = esquerda
        maca_pos = no_grid_aleatorio()
        if pontos > hs:
            abrir = open('highscore.txt', 'w')
            abrir.write(str(pontos))
            hs = pontos
# ~~~~~~~~~~~~~~Faz o player andar~~~~~~~~~~~~~~~
    if funcionando:
        if direcao == cima:
            cobra[0] = (cobra[0][0], cobra[0][1] - 10)
        if direcao == direita:
            cobra[0] = (cobra[0][0] + 10, cobra[0][1])
        if direcao == baixo:
            cobra[0] = (cobra[0][0], cobra[0][1] + 10)
        if direcao == esquerda:
            cobra[0] = (cobra[0][0] - 10, cobra[0][1])
        for i in range(len(cobra) - 1, 0, -1):
            cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

# ~~~~~~~~~~~~~~Desenha na tela~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~Desenha Chao~~~~~~~~~~~~~~~
    for p in range(40, largura, 40):
        for i in range(40, altura, 40):
            tela.blit(chao, (p, i))
    tela.blit(mato, (160, 160))
    # ~~~~~~~~~~~~~~Desenha player~~~~~~~~~~~~~~~

    for pos in range(len(cobra)-1):
        tela.blit(cobra_skin, cobra[pos])
    tela.blit(Desenhos.cobra.Imagem_cobra_cabeca, cobra[0])
    # ~~~~~~~~~~~~~~Desenha Objetivo~~~~~~~~~~~~~~~
    tela.blit(maca, maca_pos)
    # ~~~~~~~~~~~~~~Desenhar a parede~~~~~~~~~~~~~~~
    for p in range(0, altura, 40):
        tela.blit(parede, (largura-40, p))  # direita
        tela.blit(parede, (0, p))  # esquerda
    for i in range(0, largura, 40):
        tela.blit(parede, (i, altura - 40))  # baixo
        tela.blit(parede, (i, 0))  # cima
    # ~~~~~~~~~~~~~~Desenha Textos~~~~~~~~~~~~~~~
    txt = texto.render('Pontos: ' + str(pontos), 1, (255, 255, 255))
    tela.blit(txt, (largura / 2/2 - 60, 5))
    txt = texto.render('Highscore: ' + str(hs), 1, (255, 255, 255))
    tela.blit(txt, (largura / 2 + (largura/2)-250, 5))
    if not funcionando:
        txt = texto.render('Aperte "R" para iniciar ', 1, (255, 255, 255))
        tela.blit(txt, (largura / 2 - 120, altura/2-50))
    pg.display.update()
