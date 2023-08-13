''' Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

a1 = int(input('Digite um número inteiro qualquer:'))
r = int(input('Qual a razão da PA: '))
termo = a1
contador = 1
while contador <= 10:

    print(f'{termo} -> ', end=' ')
    contador = contador + 1
    termo = termo + r
print('FIM')
