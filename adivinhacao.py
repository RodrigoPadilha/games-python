import random
print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')


print('Escolha o nível de dificuldade: (1)Noob (2)Junior (3)Veteran')
dificuldade = int(input('Nível: '))
total_de_tentativas = 20
pontos = 1000
numero_secreto = random.randrange(1, 101)

if dificuldade == 2:
    total_de_tentativas = 10
elif dificuldade == 3:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas):
    print('Rodada {} de {}'.format(rodada, total_de_tentativas))
    chute_str = input('Digite um número:')
    print('Você digitou:', chute_str)
    chute_val = int(chute_str)

    acertou = chute_val == numero_secreto
    maior = chute_val > numero_secreto
    menor = chute_val < numero_secreto

    if acertou:
        print('Parabens vc ACERTOU!!!')
        print('Pontuação: {}'.format(pontos))
        break
    elif maior:
        print('Tente um numero menor')
    else:
        print('Tente um numero maior')

    pontos -= abs(numero_secreto - chute_val)


print('O número secreto era {}'.format(numero_secreto))
print('Fim do jogo')

