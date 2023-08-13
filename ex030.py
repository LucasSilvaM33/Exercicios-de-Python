"""Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar"""

num = int(input('Pense em um número inteiro qualquer e eu mostrarei se ele é par ou ímpar: '))
par = num % 2 == 0

if par:
    print(f'O número {num} é par! ')
else:
    print(f'O número {num} é ímpar! ')


