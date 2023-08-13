'''Exercício Python 52: Faça um programa que leia um número
inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite um número: '))
tot = 0 #contador de quantas vezes o número é divisível
for c in range(1, num +1): #for sempre conta 1 a menos, então por isso o +1
    if num % c == 0:
        print('\033[33m', end=' ') #amarelo se for divisível
        tot += 1
    else:
        print('\033[31m', end=' ') #vermelho se não for divisível
    print(f'{c} ', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('É por isso que ele é PRIMO!')

else:
    print('É por isso que ele NÃO É PRIMO!')


