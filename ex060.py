'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

'''from math import factorial
n1 = int(input('Digite o número para achar o seu fatorial '))
fatorial =factorial(n1)
print(f'{fatorial}')''' #uma das formas de se resolver


#modo tradicional

n = int(input('Digite um número qualquer: '))
contador = n
fatorial = 1 #Na multiplicação o fatorial nulo é o 1, então vamos começar a nossa multiplicação com 1
print(f'O fatorial de {n}!')
while contador > 0:
    print(f'{contador}', end=' ')
    print(' x ' if contador > 1 else ' = ', end=' ' ) #para fazer o sinal de x e = no print acima
    fatorial = fatorial * contador
    contador = contador - 1
print(f'O fatorial de {n} é {fatorial}')





