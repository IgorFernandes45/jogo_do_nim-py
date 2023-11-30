def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    elif n % (m + 1) == 0:
        return m
    else:
        return n % (m + 1)


def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada > m or jogada < 1 or jogada > n:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_usuario = True
    else:
        print("Computador começa!")
        vez_do_usuario = False

    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            vez_do_usuario = False
            print("Você tirou", jogada, "peça(s).")
        else:
            jogada = computador_escolhe_jogada(n, m)
            vez_do_usuario = True
            print("O computador tirou", jogada, "peça(s).")
        n -= jogada
        print("Restam", n, "peças no tabuleiro.")

    if vez_do_usuario:
        print("O computador ganhou!")
        return 0
    else:
        print("Você ganhou!")
        return 1


def campeonato():
    placar_usuario = 0
    placar_computador = 0
    for i in range(3):
        print("**** Rodada", i + 1, "****")
        vencedor = partida()
        if vencedor == 0:
            placar_computador += 1
        else:
            placar_usuario += 1
    print("**** Final do campeonato! ****")
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
opcao = int(input())

if opcao == 1:
    print("Você escolheu uma partida isolada!")
    partida()
else:
    print("Você escolheu um campeonato!")
    campeonato()



























