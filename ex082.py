'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
lista_par = []
lista_ímpar = []
while True:
    lista.append(int(input('Digite um número inteiro qualquer: ')))
    escolha = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N': #alternativa: if escolha in 'Nn':
        break
for indicie, valor in enumerate(lista):
    if valor % 2 == 0:
        lista_par.append(valor)
    elif valor % 2 != 0:
        lista_ímpar.append(valor)
print(f'A lista digitada foi {lista}')
print(f'A lista dos números par: {lista_par}')
print(f'A lista dos números ímpares: {lista_ímpar}')