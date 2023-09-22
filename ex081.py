'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
escolha = ' '
while True:
    lista.append(int(input('Digite um número qualquer: ')))
    escolha = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break
if 5 not in lista: #poderia ser if 5 in lista:
    print('O valor 5 não foi encontrado na lista')
else:
    print('O valor 5 foi encontrado na lista')
n = len(lista)
lista.sort(reverse=True)
print(f'foram digitados {n} números')
print(f'A lista em ordem decrescente: {lista}')