'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0 #acumulador
cont = 0 #contador
for c in range(1, 7):
    num = int(input(f'Escolha o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if num % 2 == 1:
        print('Todos os números escolhidos foram ímpares, então não haverá soma. ')

print(f'Foram escolhidos {cont} números pares ')
print(f'O resultado da soma de todos os número pares foram {soma} ')




