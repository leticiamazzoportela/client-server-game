# Função para verificar quem venceu a partida
# Autora: Letícia Mazzo
# Data de Criação: 26/11/2018
# Data de Modificação: 04/12/2018

def game(id1, palpite1, id2, palpite2):
    if palpite2 == 0: # Pedra
        if palpite1 == 2 or palpite1 == 3:
            return ('>>: O jogador '+id2+' VENCEU!!!', id2)
        else:
            return ('>>: O jogador '+id1+' VENCEU!!!', id1)
    elif palpite2 == 1: # Papel
        if palpite1 == 0 or palpite1 == 4:
            return ('>>: O jogador '+id2+' VENCEU!!!', id2)
        else:
            return ('>>: O jogador '+id1+' VENCEU!!!', id1)
    elif palpite2 == 2: # Tesoura
        if palpite1 == 3 or palpite1 == 1:
            return ('>>: O jogador '+id2+' VENCEU!!!', id2)
        else:
            return ('>>: O jogador '+id1+' VENCEU!!!', id1)
    elif palpite2 == 3: # Lagarto
        if palpite1 == 1 or palpite1 == 4:
            return ('>>: O jogador '+id2+' VENCEU!!!', id2)
        else:
            return ('>>: O jogador '+id1+' VENCEU!!!', id1)
    elif palpite2 == 4: # Spock
        if palpite1 == 0 or palpite1 == 2:
            return ('>>: O jogador '+id2+' VENCEU!!!', id2)
        else:
            return ('>>: O jogador '+id1+' VENCEU!!!', id1)
    elif palpite1 == palpite2:
        return ('>>: EMPATE', None)
    else:
        return ('>>: O jogador '+id1+' VENCEU!!!', id1)