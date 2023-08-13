'''Escreva um programa que converta uma temperatura digitada em °C e convertendo em °F'''

temp_c = float(input('Informe a sua temperatura em °C: '))
print(f'Sua temperatura atual é de {temp_c}, convertendo para °F ficaria {(temp_c * (9/5) + 32):.2f}')