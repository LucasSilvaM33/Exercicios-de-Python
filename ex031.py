"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
 por Km para viagens de até 200Km a R$0,45 para viagens mais longas"""

dist = float(input('Qual a distãncia da sua viagem em km?'))
viagem_curta = dist * 0.50 #até 200km
viagem_longa = dist * 0.45 #acima de 200km
if dist <= 200:
    print(f'O valor da sua viagem é de {viagem_curta:.2f} Reais')
else:
    print(f'O valor da sua viagem é de {viagem_longa:.2f} Reais')
