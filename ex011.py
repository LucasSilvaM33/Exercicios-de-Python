'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a
sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de
tinta, pinta uma área de 2m²'''

alt = float(input('Qual a altura da sua parede em metros? '))
lag = float(input('Qual a largura dasua parede em metros?'))
area = alt * lag
print(f'A área da parede é de {area:.2f}m²')
print(f'vocẽ vai precisar de {(area / 2):.2f} litros de tinta')
