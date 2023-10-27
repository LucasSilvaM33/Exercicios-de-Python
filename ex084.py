''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. '''

dados = list()
galera = list()
maior_peso = menor_peso = 0
totP = 1

escolha = ' '
while escolha not in 'N':
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(int(input('Digite o seu peso: ')))
    galera.append(dados[:])
    dados.clear()
    escolha = str(input('Você quer continuar? [S/N]')).upper().strip()[0]

    if escolha == 'S':
        print('Continuando...')
        totP += 1

    else:
        print('Parando...')
        break
for pessoa in galera:
    if
print(galera)
print(f'O total de pessoas cadastradas foi de {totP}')