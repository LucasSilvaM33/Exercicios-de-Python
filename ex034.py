"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1250,00  calcule o aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Qual é o seu salário? '))
aumento_1 = salario * 1.10
aumento_2 = salario * 1.15
if salario > 1250:
    print(f'Você ganha {salario} reais e vai receber um aumento de 10%, então seu novo salário vai ser de {aumento_1:.2f} reais! ')
else:
    print(f'Você ganha {salario} reais e vai receber um aumento de 15%, entaão seu salário vai ser de {aumento_2:.2f} reais! ')