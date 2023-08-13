"""Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever
na tela se o usuário venceu ou perdeu"""

from random import choice

print('Vamos jogar? ')
print('Eu vou pensar em um número de zero a conco e você vai tentar adinvinhar que número eu estou pensando:')
n = int(input('Qual número eu estou pensando? '))
lista = [0,1,2,3,4,5]
numero_sorteado = (choice(lista)) #comando que faz o computador "pensar"
#print(f'Número que eu pensei {numero_sorteado}') #comando usado para verificar o que o computador "pensou"

if n == numero_sorteado:
    print('Você acertou! Pababéns!!!!! ')

else:
    print(f'Ah que pena, você errou, eu pensei no número {numero_sorteado} e você no {n}!')





