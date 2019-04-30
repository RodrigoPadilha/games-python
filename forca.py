import random


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_personagem_secreto()
    letras_reveladas = ['_' for letra in palavra_secreta] # letras_reveladas = ['_','_','_','_','_','_']

    tentativas = 7
    qtd_acertos = 0
    encontrou_chute = False
    vencedor = False

    while tentativas > 0 and not vencedor:
        desenha_forca(letras_reveladas, tentativas)
        chute = input('Qual a letra do Personagem? ').strip()

        for index in range(len(palavra_secreta)):
            if chute.upper() == palavra_secreta[index].upper():
                letras_reveladas[index] = palavra_secreta[index]
                encontrou_chute = True
                qtd_acertos += 1

        if not encontrou_chute:
            tentativas -= 1

        encontrou_chute = False
        vencedor = qtd_acertos == len(palavra_secreta)

    if vencedor:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
        desenha_forca(letras_reveladas, tentativas)


def imprime_mensagem_abertura():
    print('*******************************************************')
    print('****** Bem vindo ao jogo da Forca StreetFigther! ******')
    print('*******************************************************')


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou! ¯\_(ツ)_/¯")
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
    print('Vc Perdeu! O personagem era {}'.format(palavra_secreta))
    print(':-(')


def desenha_forca(letras_reveladas, tentativas):
    print(letras_reveladas)

    print("  _______     ")
    print(" |/      |    ")

    if tentativas == 6:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if tentativas == 5:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if tentativas == 4:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if tentativas == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if tentativas == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if tentativas == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if tentativas == 0:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def carrega_personagem_secreto():
    arquivo = open('personagens_street_figther.txt', 'r')
    personagens = []
    for linha in arquivo:
        personagens.append(linha.strip())
    arquivo.close()
    personagem = random.randrange(0, len(personagens))

    return list(personagens[personagem])


if __name__ == '__main__':
    jogar()