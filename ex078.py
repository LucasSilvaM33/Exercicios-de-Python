'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

lista = list()
pos_maior =  []
pos_menor = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {cont}º: ')))
print(f'Os valores digitados foram {lista}')
for pos, num in enumerate(lista):
    if num == max(lista):
        print(f'O maior valor foi {max(lista)} e ele está na posição {pos}')
    if num == min(lista):
        print(f'O menor valor da lista foi {min(lista)} e ele está na posição {pos}')
print('FIM')



