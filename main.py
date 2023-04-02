import random
import os
from palavras import Palavras


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

vida = 5
erro = 0
erros_letra = ""
jogo = True
acertos = 0
game = True
letra = "0"


def ChamarPalavra():
    global D, P, espaco, vazio, P_O
    p = Palavras()
    P_O = p.palavra_original
    P = p.palavra
    D = p.dica
    espaco = len(P)
    vazio = espaco * "_"

ChamarPalavra()

while game == True:
    os.system('cls')
    print(10 * "=-=")
    print("Vida: ", vida)
    print("Erros: ", erro)

    print("Palavra: ", vazio, "(", espaco, ")")
    print("\nDica: ", D)
    print(10 * "=-=")
    print("\nLetras erradas: ", erros_letra, )
    while True:
        letra = str(input("\nEscolha uma letra: ").lower())
        if letra == "":
            print("Voce deve escolher uma letra")
            True
        elif len(letra) == 1:
            break
        else:
            print("Previsa ser só uma letra")
            True
    vezes_letra = P.count(letra)
    print(vezes_letra)
    if (letra in P) == True:
        for n in range(0, vezes_letra):
            index = P.find(letra)
            vazio = vazio[:index] + letra + vazio[index + 1:]
            P = P[:index] + "_" + P[index + 1:]
            acertos += 1
            if acertos == espaco:
                clear()
                print("Você conseguiu!")
                print("A palavra era: ", vazio)
                game = False
    else:
        erros_letra = erros_letra + letra + " / "
        erro = erro + 1
        vida = vida - 1
        if vida == 0:
            clear()
            print("Você perdeu, a palavra era: ", P_O)
            break