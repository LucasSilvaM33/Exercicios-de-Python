'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
tot = produto1000 = cont = menor = barato = 0
while True:
    produto = str(input('Qual o nome do produto selecionado? '))
    preço = int(input('Qual o valor do produto selecionado? R$ '))
    cont += 1
    tot = tot + preço
    if preço > 1000:
        produto1000 += 1
    if cont == 1:
       barato = produto
       menor = preço
    else:
        if preço < menor:
           barato = produto
           menor = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total gasto foi de R$ {tot}')
print(f'O número de produtos acima de R$ 1000,00 é de {produto1000}')
print(f'O produto mais barato foi {barato} e o seu custa foi de R$ {menor}')

print('FIM')