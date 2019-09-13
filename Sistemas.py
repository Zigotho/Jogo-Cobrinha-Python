import Desenhos
import random


def no_grid_aleatorio():
    x = random.randrange(40, Desenhos.altura - 40)
    y = random.randrange(40, Desenhos.altura - 40)
    return x // 10 * 10, y // 10 * 10


def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])



