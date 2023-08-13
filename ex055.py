'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
foi o maior e o menor peso lidos.'''

maiorpeso = 0
menorpeso = 0
for pess in range(1, 6):
    peso = float(input(f'Qual o peso da {pess}º pessoa: '))
    if pess == 1: #lendo o peso da primeira pessoa, isso vai acontecer se for o primeiro laço.
        maiorpeso = peso #como eu só li o peso da primeira pessoa, ela vai ter o maior e o menor peso.
        menorpeso = peso
    else:#se não for o primeiro laço, vamos verificar os próximos.
        if peso > maiorpeso: #Se o peso que eu li da primeira pessoa que até o momento é o maior peso, for menor que o da segunda pessoa...
            maiorpeso = peso #...então o maior peso passa a ser o da segunda pessoa e não mais o da primeira, essa verificação vai se repetir até a ultima pessoa
        if peso < menorpeso:# O mesmo raciocinio vale para o menor peso
            menorpeso = peso
print(f'A pessoa com o maior peso tem {maiorpeso} Kg')
print(f'A pessoa com o menor peso tem {menorpeso} Kg')
