'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento'''

salario = float(input('Informe o seu salário: '))
print(f'O seu salário é de R$ {salario} e com um aumento de 15%, você passara a receber {(salario * 1.15):.2f}')