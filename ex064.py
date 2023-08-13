'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''


contador = num = soma = 0
num = int(input('Digite um número inteiro qualquer: '))
while num != 999:
    contador += 1
    soma += num
    num = int(input('Digite um número inteiro qualquer: '))
print('Fim do programa. ')
print(f'Você Digitou {contador} números e a soma entre eles é de {soma}. ')

