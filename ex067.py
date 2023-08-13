'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
cont = 0
while True:
    num = int(input('Digite um número inteiro qualquer para mostrar sua tabuada:  '))
    if num < 0:
        break
    for c in range (1, 11):
        print(f'{num} x {c} = {num * c}')
print('FIM')


