import random
import jogos
import os

def jogar():

    imprime_mensagem_abertura()

    print("\nTem certeza que quer entrar nesse jogo?")
    volta_jogo = int(input("SIM-1 | NAO-2: ").strip())
    if(volta_jogo == 2):
        os.system('cls')
        jogos.escolhe_jogo()

    else:
        palavra_secreta = carrega_palavra_secreta()
        print(palavra_secreta)

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)   # foi criado um laço para cada letra da palavra.
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    pontos = 7

    # enquanto não enforcou E nao acertou
    while (not enforcou and not acertou):
        print("Voce tem {} erros".format(pontos))
        chute = pede_chute()
        if (chute in palavra_secreta):                                       # procurar um posição da letra na palavra_secreta(generalizada)
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            pontos -= 1

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)




def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:  # O for é para organizar as palavras e adicionar elas em list[]
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))  # Sortear uma palavra para o jogo da forca de 0 ao maximo(num.) das palavras
    palavra_secreta = palavras[numero].upper()  # palavra_secreta recebe a palavra sorteada atraves da list[]
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()  # strip tira os espaços da palavra, adcionada letra maiuscula em tudo.
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0  # procurar uma letra na palavra_secreta.
    for letra in palavra_secreta:  # o chute tem que ser igual a letra procurada.
        if (chute == letra):  # letras acertadas vai receber as letras e coloca-las nas posições corretas.
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == "__main__"):
    jogar()