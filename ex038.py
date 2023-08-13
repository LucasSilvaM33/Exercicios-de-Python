"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite um segundo número inteiro qualquer: '))
if n1 > n2:
    print(f'O número {n1} é maior que o número {n2} ')
elif n2 > n1:
    print(f'O número {n2} é maior que o {n1} ')
else:
    print(f'Não existe valor maior, pois os números {n1} e {n2} são iguais! ')