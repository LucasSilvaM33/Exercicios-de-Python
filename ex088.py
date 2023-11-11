'''Exercício de Python 088: Faça um programa que ajude um jogador da mega sena a criar palpites.
O progama vai perguntar quantos jogos serão geradores e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrado
 tudo em uma lista composta'''

from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 50)
print('                    MEGA SENA                   ')
print('-' * 50)
escolha = int(input('Quantos jogos você quer sortear? '))
tot = 1
print('-' * 50)
while escolha >= tot:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    i += 1
    print(f'Jogo {i}º: {l}')
    sleep(1)
print('BOA SORTE')