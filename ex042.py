"""Refaça o desafio 035 dos triângulos, acresentando o recurso de mostrar que tipo de triângulo
será formado:
-Equilátero: Todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: Todos os lados diferentes"""

r1 = float(input('Qual o comprimento da primeira reta: '))
r2 = float(input('Qual o comprimento da segunda reta: '))
r3 = float(input('Qual o comprimento da terceira reta: '))

regra1 = (r2 - r3) < r1 < r2 + r3
regra2 = (r1 - r3) < r2 < r1 + r3
regra3 = (r1 - r2) < r3 < r1 + r2

if regra1 and regra2 and regra3:
    print(f'Os seguimentos de retas {r1}, {r2} e {r3} podem formar um triângulo!')

    if r1 == r2 == r3:
        print('É um triângulo Equilátero, pois todos os lados são iguais. ')

    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triângulo Isósceles, pois tem dois lados iguais. ')

    else: #caso usasse o elif aqui. r1 != r2 != r3 =! r1
        print('É um triângulo Escaleno, pois todos os seus lados são diferentes')









else:
    print(f'Os segmentos de retas {r1}, {r2} e {r3} não podem formar um triângulo! ')


