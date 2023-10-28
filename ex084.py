''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. '''

dados = list()
galera = list()
maior_peso = menor_peso = 0
# totP = 1   #usando como contador
escolha = ' '
while escolha not in 'N':
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(float(input('Digite o seu peso: ')))
    if len(galera) == 0:
        maior_peso = dados[1]
        menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    galera.append(dados[:])
    dados.clear()
    escolha = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if escolha == 'S':
        print('Continuando...')
        # totP += 1 Contador
    else:
        print('Parando...')
        break
print(galera)
print(f'O total de pessoas cadastradas foi de {len(galera)}.')  #No lugar do contador, estou mostrando o tamanho da lista da galera
print(f'O maior peso foi de {maior_peso} kg. Peso de ', end=' ')
for pessoa in galera:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}]', end=' ')
        print()
print(f'O menor peso foi de {menor_peso}. Peso de ', end=' ')
for pessoa in galera:
    if pessoa [1] == menor_peso:
        print(f'[{pessoa[0]}]', end=' ')
        print()