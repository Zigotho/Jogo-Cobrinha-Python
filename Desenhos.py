import pygame as pg

caminho = 'Imagens/'
altura = 600
largura = 800


# ~~~~~~~~~~~~~~Desenhar a Cobra~~~~~~~~~~~~~~~


class cobra:
    Imagem_cobra = pg.image.load(caminho + 'cobra/cobra.png')
    rectCobra = Imagem_cobra.get_rect()

    @staticmethod
    def getcobra_pos():
        cobra_pos = [(largura / 2, altura / 2), (largura / 2 + 10, altura / 2), (largura / 2 + 20, altura / 2),
                     (largura / 2 + 30, altura / 2)]
        return cobra_pos


# ~~~~~~~~~~~~~~Desenhar a Maça~~~~~~~~~~~~~~~
maca = pg.image.load(caminho + 'maca/maca.png')
macaDourada = pg.image.load(caminho + 'maca/maca_Dourada.png')

# ~~~~~~~~~~~~~~Desenhar a parede~~~~~~~~~~~~~~~
parede = pg.image.load(caminho + 'cenario/parede.png')
rectParede = parede.get_rect()

# ~~~~~~~~~~~~~~Desenhar a Chao~~~~~~~~~~~~~~~
chao = pg.image.load(caminho + 'cenario/chao.png')
mato = pg.image.load(caminho + 'cenario/mato.png')


icone = pg.image.load(caminho + 'cenario/snake.ico')
