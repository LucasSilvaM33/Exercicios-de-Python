'''Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros'''

#quilômetro(km), hectômetro(hm), decâmetro (dam), metro (m), decímetros (dm), centímetros (cm), milímetros (mm)

num = float(input('Informe um valor em metros: '))
print(f'Em quilometros é {num * 1000} km')
print(f'Em hectômetros é {num * 100} hm')
print(f'Em decâmetros é {num * 10} dam')
print(f'Em decímetros é {num / 10} dm')
print(f'Em centímetros é {num / 100} cm')
print(f'Em milímetros é {num / 1000} mm')