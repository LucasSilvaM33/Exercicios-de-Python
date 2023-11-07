'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo
teclado. No final, mostre a matriz na tela, com a formação correta.'''


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}][{coluna}]: '))
print('-'*50)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^4}]', end=' ')
    print()





