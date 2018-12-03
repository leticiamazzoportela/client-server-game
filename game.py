from time import sleep
from random import randint

def game(id1, palpite1, id2, palpite2):
    if (palpite1 + 1) % 5 == palpite2:
        return ('>>: O jogador '+id1+' VENCEU!!!')
    elif (palpite1 + 2) % 5 == palpite2:
        return ('>>: O jogador '+id1+' VENCEU!!!')
    elif palpite1 == palpite2:
        return '>>: EMPATE'
    else:
        return ('>>: O jogador '+id2+' VENCEU!!!')