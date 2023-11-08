'''Exercício Python 87: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha'''
spar = scol = mai = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um valor para a posição {l}x{c} da matriz: '))
print('-'*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            spar = spar + matriz[l][c]
    print()
print('-'*50)
print(f'A soma dos números pares é igual a: {spar}')
#print(f'{matriz[0][2] + matriz[1][2] + matriz[2][2]}') #Soma da coluna primeira maneira
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma da coluna três é igual a: {scol}')
for c in range(0,3):
    if matriz[1][c] > mai:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior número da segunda linha é {mai}')

