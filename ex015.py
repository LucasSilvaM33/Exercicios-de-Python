'''Escreva um programa que prgunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

caminho = float(input('Quantos Km você percorreu? '))
aluguel = int(input('Quantos dias você passou com o carro? '))
print(f'Você passou {aluguel} dias com o carro e percorreu {caminho} Km, logo você deverar pagar R${((aluguel * 60) + (caminho * 0.15)):.2f}')