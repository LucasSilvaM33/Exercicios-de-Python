'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = float(input('Escolha um valor. '))
n2 = float(input('Escolha um segundo valor. '))

opition = 0 #opção começa com zero
while opition != 5:
    print('====================MENU====================')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do Programa')
    opition = int(input('Escolha uma das opções a seguir: '))
    if opition == 1:
        print(f'A soma dos número {n1} e {n2} é igual a {n1 + n2}')
    elif opition == 2:
        print(f'A multiplicação dos números {n1} e {n2} é igual a {n1 * n2}')
    elif opition == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        else:
            print(f'O maior número entre {n1} e {n2} é {n2}')
    elif opition == 4:
        print('Quais números você quer escolher agora:')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
    elif opition == 5:
        print('Finalizando o programa. ')
    else:
        print('Opção invalida, tente novamente. ')
    sleep (2)

print('Fim do programa')




