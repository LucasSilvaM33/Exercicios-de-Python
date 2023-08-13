'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''


saque = int(input('Qual o valor você quer sacar? R$ '))
total = saque
cédula = 50
totcédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totcédula += 1
    else:
        if totcédula > 0:
            print(f'Você vai receber {totcédula} cédulas de R$ {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
            totcédula = 0
        if total == 0:
            break
print('FIM')

