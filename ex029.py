"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma menssagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite."""

vel = float(input('Com qual velocidade você passou pela avenida? '))
multa = vel > 80
valor_da_multa = float((vel - 80) * 7)

if multa:
    print(f'Você andou acima da velocidade estabelecida de 80 km/h, então você foi multado em {valor_da_multa:.2f} Reais!')
else:
    print('Você andou dentro do limite de velocidade! Obrigado por respeitar as leis de trânsito. ')
