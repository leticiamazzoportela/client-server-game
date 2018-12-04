# Servidor TCP
# Autora: Letícia Mazzo
# Data de Criação: 26/11/2018
# Data de Modificação: 04/12/2018

import socket, threading
from game import game
from termcolor import colored

conns = set() # armazena conexoes
aux = []
msgs = {} #armazena mensagens
host, port = ('', 5000)

def isnumber(value):
    try:
         int(value)
    except ValueError:
         return False
    return True

def showPalpites(id1, palpite1, id2, palpite2):
    itens = ('PEDRA' , 'PAPEL' , 'TESOURA' , 'LAGARTO' , 'SPOCK')
    str1 = '<==>' *10
    str2 = '{} jogou {}!'.format(id1, itens[palpite1])
    str3 = '{} jogou {}!'.format(id2, itens[palpite2])

    return colored(str1+'\n'+str2+'\n'+str3+'\n'+str1+'\n', 'cyan')

def run(conn):
    while True:
        data = conn.recv(1024) # receber informacao
        if not data: # se o cliente tiver desligado
            break
        
        msg = data.decode()
        cliente = format(conn.getpeername())
        id = cliente.split(", ")[1].split(")")[0]
        
        print('palpites: ', msgs)

        desconectado = 'Cliente '+cliente+' desconectado'

        if msg == "sair\n":
            for c in conns:
                if c is not conn:
                    c.send(colored('\n>>: Cliente {} Saiu...\n', 'magenta').format(conn.getpeername()).encode('utf-8'))
            conns.remove(conn)
            print(colored(desconectado, 'magenta'))

        for c in conns: # enviar mensagem para todos os outros clientes
            if len(conns) > 1:
                aux.append(format(c.getpeername()).split(", ")[1].split(")")[0])
                if c is not conn: # exceto para o que a enviou 
                    # c.send('{}: {}'.format(conn.getpeername(), data.decode()).encode('utf-8'))

                    if msg == "sair\n":
                        c.send(colored('>>: Cliente {} Saiu...', 'magenta').format(conn.getpeername()).encode('utf-8'))
                        conns.remove(c)
                        break
            
                    if msg != "sair\n" and msg != "ajuda\n" and msg != "jogar":
                        if isnumber(msg):
                            msgs[id] = msg
                        # else:
                        #     data2 = conn.recv(1024) # receber informacao
                        #     if not data: # se o cliente tiver desligado
                        #         break
                            
                        #     msg2 = data2.decode()
                        #     print(format(msg2).encode())
            else:
                c.send(colored('''>>: Você não pode jogar sozinho! Espere alguém se conectar e informe sua opção de jogo: ''', 'magenta')
                .encode('utf-8')) 
        
        if len(aux) >= 2 and aux[0] in msgs.keys() and aux[1] in msgs.keys():
            retorno, vencedor = game(aux[0], int(msgs[aux[0]]), aux[1], int(msgs[aux[1]]))
            palpites = showPalpites(aux[0], int(msgs[aux[0]]), aux[1], int(msgs[aux[1]]))
            msgs.clear()

            for c in conns:
                c.send('{}'.format(palpites).encode('utf-8'))

                if vencedor == format(c.getpeername()).split(", ")[1].split(")")[0]:
                    c.send('{}'.format('>>: Você venceu!!!').encode('utf-8'))
                else:
                    c.send('{}'.format(retorno+'\nVocê perdeu :(').encode('utf-8'))
                
                c.send(colored('''\n>>: Para jogar novamente, digite 'jogar' ou 'sair' para encerrar:''', 'cyan')
                .encode('utf-8')) 


with socket.socket() as sock: # conexoes TCP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reutilizar endereco logo a seguir a fechar o servidor
    sock.bind((host, port))
    sock.listen(3) # servidor ativo
    print(colored('>>: Servidor rodando na porta {}\n'.format(port), 'green'))
    while True:
        conn, addr = sock.accept() # esperar que alguem se conect
        conectado = '>>: Servidor conectado ao cliente: {}'.format(addr[1])
        print(colored(conectado, 'green'))
        conn.send(colored('>>: Bem-vindo {}!\nEscolha uma opção: \n Jogar\n Ajuda\n Sair\n', 'green')
            .format(addr).encode())

        conns.add(conn) # adicionar conexao ao nosso set de conexoes
        for c in conns:
            if c is not conn:
                c.send(colored('>>: {} conectado...', 'green').format(conn.getpeername()).encode('utf-8'))

        threading.Thread(target=run, args=(conn,)).start() 

# TODO
#1 Mostrar p/ a pessoa que ela quem ganhou -> +/-
#2 tentar fazer o negócio de pontuação (aí tem que colocar nome)
#4 ver se consigo adicionar mais uma pessoa
#5 Se eu inicio um cara primeiro, mas coloco a primeira opcao de jogo no que iniciei por segundo, ele buga