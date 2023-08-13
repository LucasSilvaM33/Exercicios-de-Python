'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''

from random import choice #no lugar do choice, poderia ser randint
tentativas = 0 #contador de tentativas
print('Vamos brincar de adivinha. ')
print('Eu vou pensar num número entre 0 e 10 e você vai tentar adivinhar. ')
print('No final do jogo eu mostrarei quantas tentativas você fez até adivinhar o número. ')

lista = [0, 1, 2, 3, 4, 5, 6, 7 , 8, 9, 10] #lista que o computador vai sortear
#poderia ser também
#computador = randint(0, 10)

computador = choice(lista)
#print(f'{computador}') #confirmação da escolha do computador
acertou = False
while not acertou: #enquanto a gente não acertar, vamos repetir
    jogador = int(input('Escolha um número: '))
    tentativas = tentativas + 1
    if jogador == computador:
        acertou = True
        print('Você ganhou!!! ')
        print(f'Você escolheu o número {jogador} e o computador {computador}')
        print(f'Você teve um total de {tentativas} tentativas. ')
    else:
        if jogador < computador:
            print('O número é mais alto, tente novamente. ')
        if jogador > computador:
            print('O número é mais baixo, tente novamente. ')
print('Fim do jogo')













