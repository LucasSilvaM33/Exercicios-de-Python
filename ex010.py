'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos Dólares ela pode comprar
Considerando U$1,00 = R$3,27'''

money = float(input('Quantos reais você tem na sua carteira? '))
print(f'Você tem R${money} e convertendo para dolar ficaria U${(money / 3.27):.2f} ')