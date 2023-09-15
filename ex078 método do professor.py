'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um número inteiro para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]

    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('=-' * 30)
print(f'Você escolheu os números {lista}')
print(f'O maior valor da lista é {maior} e está na posição ', end=' ')
for pos, val in enumerate(lista):
    if val == maior:
        print(f'{pos}... ', end=' ')
        print()
print(f'O menor valor da lista é {menor} e está na posição ', end=' ')
for pos, val in enumerate(lista):
    if val == menor:
        print(f'{pos}...', end='')
