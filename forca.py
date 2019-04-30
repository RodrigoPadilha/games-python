def jogar():

    print('*****************************************')
    print('****** Bem vindo ao jogo da Forca! ******')
    print('*****************************************')

    palavra_secreta = 'mario'
    chances = 5
    qtd_acertos = 0
    encontrou_chute = False
    vencedor = False
    while chances > 0 and not vencedor:
        print('Qual a letra você acha que a palavr possui?')
        chute = input('Insira a letra:').strip()

        for index in range(len(palavra_secreta)):
            if chute.upper() == palavra_secreta[index].upper():
                print('Encontrou a letra {} no index {}'.format(chute, index))
                encontrou_chute = True
                qtd_acertos += 1

        if not encontrou_chute:
            chances -= 1
            print('chances ', chances)

        encontrou_chute = False
        vencedor = qtd_acertos == len(palavra_secreta)

    if vencedor:
        print('Parabéns, vc Ganhou!!!')
        print('¯\_(ツ)_/¯')
    else:
        print('Vc Perdeu!')
        print(':-(')

    print('Fim do Jogo')


if __name__ == '__main__':
    jogar()
