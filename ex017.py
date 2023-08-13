'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa.'''

oposto = float(input('Qual o comprimentro do cateto oposto em metros? '))
adjacente = float(input('Qual o comprimentro do cateto adjacente em metros? '))
print(f'O comprimento do cateto oposto é de {oposto}m e do adjacente é de {adjacente}m, então o valor da hiponetusa é de {(oposto ** 2 + adjacente ** 2) ** (1/2):.2f}m')