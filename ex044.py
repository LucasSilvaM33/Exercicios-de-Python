"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
-À vista dinheiro ou cheque: 10% de desconto
-À vista no cartão: 5% de desconto
-Em até 2 vezes no cartão: Preço  normal
-3 vezes ou mais no cartão: 20% de juros
"""

preco = float(input('Digite o valor do produto que você deseja comprar: '))
print('1 = À Vista dinheiro/cheque: ')
print('2 = À Vista no cartão ')
print('3 = 2x no cartão ')
print('4 = 3x ou mais no cartão ')
pagamento = int(input('qual tipo de pagamento você deseja realizar? '))

if pagamento == 1:
    print(f'Sua compra tem um desconto de 10%, então ela passa de R$ {preco} para R$ {preco * 0.9} ')
elif pagamento == 2:
    print(f'Sua à vista no cartão recebe um desconto de 5%, ficando no valor de  R$ {preco * 0.95}')
elif pagamento == 3:
    print(f'Sua compra de {preco} será parcelada em 2x de R$ {preco / 2} sem juros.')
elif pagamento == 4:
    parcelas = int(input('Em quantas vezes você deseja parcelar a sua compra? '))
    print(f'sua compra de R$ {preco} será parcelada em {parcelas}x de R$ {preco / parcelas:.2f} com juros')
    print(f'Ficando com um total de {preco * 1.2}')
else:
    total = 0
    print('Opção invalida de pagamento. Tente novamente!')









