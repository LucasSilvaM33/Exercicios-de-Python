'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.'''

from random import randint
vit = 0
while True:
    jogador = int(input('Escolha um número: '))
    computador = randint(0, 10)
    resultado = jogador + computador
    tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    while tipo not in 'PI':
        print('Tipo inválido, escolha novamente.  ')
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'O compuador escolheu {computador} e o jogador {jogador}, o resultado foi {resultado}')
    print('deu PAR' if resultado % 2 ==0 else 'Deu Ímpar')
    if tipo == 'P' and resultado % 2 == 0:
        print(f'Você Ganhou! ')
        vit += 1
    elif tipo == 'I' and resultado % 2 != 0:
        print(f'Você Ganhou! ')
        vit += 1
    else:
        print('Você perdeu')
        break
print(f'Você teve {vit} vitórias!')









