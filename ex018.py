#Faca um programa que leia um ãngulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ãngulo

import math

n = float(input('Informe o ãngulo que você deseja: '))
seno = math.sin(math.radians(n))
cosseno = math.cos(math.radians(n))
tangente = math.tan(math.radians(n))
print(f'O valor do seno é de: {seno:.2f}')
print(f'O valor do cosseno é de: {cosseno:.2f}')
print(f'O valor da tangente é de: {tangente:.2f}')