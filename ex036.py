"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, o salário do
comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ele não pode exceder 30% do salário ou então o
empréstimo será negado."""

imovel = float(input('Qual o valor da residência que você deseja adquirir? '))
salario = float(input('Quanto você ganha por mês? '))
tempo = int(input('Quantos anos você pretende financiar o imóvel? '))

financiamento = imovel / (tempo * 12) #valor de anos convertido em meses.


if  financiamento <= (0.3 * salario):
    print('Seu emprestimo foi aprovado!!')
    print(f'Você vai pagar R$ {financiamento:.2f} por mês. ')

else:
    print(f'Sinto muito, mas o seu empréstimo foi negado, pois ele excedeu 30% do seu sálario. '
          f'A prestação seria de R$ {financiamento:.2f} ')