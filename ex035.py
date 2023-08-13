"""Desenvolva um programa que leia o comprimento de três retas e diga e diga ao usuário se eles
podem ou não formar um triângulo. """

r1 = float(input('Qual o comprimento da primeira reta? '))
r2 = float(input('Qual o comprimento da segunda reta? '))
r3 = float(input('Qual o comprimento da terceira reta? '))

regra1 = (r2 - r3) < r1 < r2 + r3
regra2 = (r1 - r3) < r2 < r1 + r3
regra3 = (r1 - r2) < r3 < r1 + r2

if regra1 and regra2 and regra3:
    print(f'Os seguimentos de retas {r1}, {r2} e {r3} podem formar um triângulo. ')


else:
    print(f'Não é possível fazer um triângulo com os segmentos de retas {r1}, {r2} e {r3}. ')
