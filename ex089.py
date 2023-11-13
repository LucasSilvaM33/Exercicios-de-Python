'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
 mostrar as notas de cada aluno individualmnte'''
from time import sleep
dados = []
while True:
    nome = str(input('Nome do aluno: ')).strip().upper()
    n1 = float(input('Nota 01: '))
    n2 = float(input('Nota 02: '))
    media = (n1 + n2)/2
    dados.append([nome, [n1, n2], media])
    resp = str(input('Você quer continuar? [S/N]'))
    if resp not in 'Ss':
        break
#boletim.append(dados[:])
#dados.clear()
print('=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')

while True:
    ind = int(input('Mostrar a nota de qual aluno? (interromper 999): '))
    if ind == 999:
        print(f'FINALIZANDO...')
        sleep(1)
        break
    if ind <= len(dados) - 1:
        print(f'O aluno {dados[ind][0]} tirou as notas {dados[ind][1]}')


