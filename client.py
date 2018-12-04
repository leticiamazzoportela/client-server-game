# Cliente
# Autora: Letícia Mazzo
# Data de Criação: 26/11/2018
# Data de Modificação: 04/12/2018

import socket, threading, sys, select
from termcolor import colored

def isnumber(value):
    try:
         int(value)
    except ValueError:
         return False
    return True

def showModos():
    print(colored('{:=^40}'.format('\n>: VAMOS JOGAR PEDRA-PAPEL-TESOURA-LAGARTO-SPOCK!!!'), 'cyan'))
    print(colored('''Modos de Jogo:
    [ A ] Partida Única
    [ B ] Melhor de 3
    [ C ] Melhor de 5\n''', 'cyan'))

def showMsg():
    print(colored('''Sua opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
    [ 3 ] Lagarto
    [ 4 ] Spock\n''', 'cyan'))

with socket.socket() as s:
    s.connect(('', 5000))
    while True:
        io_list = [sys.stdin, s]
        ready_to_read,ready_to_write,in_error = select.select(io_list , [], [])
        for io in ready_to_read:
            if io is s: # se tivermos recebido mensagem
                resp = s.recv(1024)
                if not resp:
                    print(colored('>: Servidor inativo', 'red'))
                    sys.exit()
                print('{}'.format(resp.decode()))
            else:
                msg = sys.stdin.readline() # enviar mensagem
                s.send(msg.encode())

                if msg == 'sair\n':
                    s.close()
                    sys.exit()
                elif msg == 'ajuda\n':
                    with open('ajuda.txt', 'r') as f:
                        for linha in f:
                            print(colored(linha, 'yellow'))
                elif msg == 'jogar\n':
                    # showModos()
                    # msg = sys.stdin.readline() # enviar mensagem
                    
                    # if isnumber(msg):
                        # print(colored('\n>: Opção não reconhecida! Tente novamente.', 'magenta'))
                    # else:
                    showMsg()
                        # s.send(msg.encode())

                else:
                    if not isnumber(msg):
                        print(colored('\n>: Opção não reconhecida! Tente novamente.', 'magenta'))
                
                sys.stdout.flush()
