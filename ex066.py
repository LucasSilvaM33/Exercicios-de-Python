'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

soma = cont = 0
while True: #TRansformei num loop infinito e não precisei usar o flag while num != 999:
    num = int(input('Digite um número inteiro qualquer (999 para parar): '))
    if num == 999:
        break
    soma = soma + num
    cont += 1
print(f'Foram usados {cont} números e a soma deles foram de {soma}\nFim do Programa')
