'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

print('Progressão Aritmetica')
print('='*100)

a1 = int(input('Qual o primeiro termo: '))
r = int(input('Qual a razão: '))
for c in range(1, 11):
    n = c #termo da PA. Coloco c para variar de acordo com o contador da repetição
    calculo = a1 + (n - 1) * r #formula da PA
    print(f'{calculo}', end= '-> ')
print('-> Acabou')


