"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex: Digite um número: 1834
unidade: 4, dezena: 3, centena: 8, milhar: 1"""

num = int(input('Digite um número de 0 a 9999: '))

print(f'O número  que você escolheu foi {num}')
print(f'Ele tem {num // 1 %10 } unidades, {num // 10 % 10} dezenas, {num // 100 % 10} centenas e {num // 1000 % 10} milhar')
