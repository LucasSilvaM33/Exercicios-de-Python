'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
ano_atual = date.today().year
totalmaior = 0 #necessário para contar o número de pessoas maior de idade
totalmenor = 0 #nnecessário para contar o número de pessoas menor de idade
for pess in range(1,8):
    nasc = int(input(f'Qual o ano de nascimento da {pess}º pessoa? '))
    idade = ano_atual - nasc
    if idade >= 21:
       totalmaior += 1
    else:
        totalmenor += 1
print(f'{totalmaior} São maiores de idade')
print(f'{totalmenor} São menores de idade')