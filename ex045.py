"""Crie um programa que faça o computador jogar Pedra, Papel e Tesoura com você."""

from random import randint
from time import sleep
print('Vamos jogar pedra, papel, tesoura! ')
lista = ('pedra', 'papel', 'tesoura') #pedra = 0, tesoura = 1, papel = 2
computador = randint(0, 2) #Vai randomizar de 0 a 2
print('Faça a sua escolha e teste a sua sorte!')
print('[ 0 ] = PEDRA\n[ 1 ] = PAPEL\n[ 2 ] = TESOURA')
jogador = int(input('qual das opcções você vai escolher? '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)
print('-='*40)
print(f'Computador jogou {lista[computador]} ')
print(f'Jogador jogou {lista[jogador]} ')
print('-='*40)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('JOGADOR VENCEU!')

    elif jogador == 2:
        print('COMPUTADOR VENCEU!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!')

    elif jogador == 1:
        print('EMPATE!')

    elif jogador == 2:
        print('JOGADORDOR VENCEU!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!')

    elif jogador == 1:
        print('COMPUTADOR VENCEU!')


    elif jogador == 2:
        print('EMPATE!')

    else:
        print('JOGADA INVÁLIDA!')
else:
    print('JOGADA INVÁLIDA!')









