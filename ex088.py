'''Exercício de Python 088: Faça um programa que ajude um jogador da mega sena a criar palpites.
O progama vai perguntar quantos jogos serão geradores e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrado
 tudo em uma lista composta'''
'''from random import randint
dados = []
jogo = []

num = int(input('quantos jogos você quer que eu sorteie? '))
for c in range(0, num):
    dados.append(randint(0,60))
    jogo.append(dados[:])
    dados.clear()
print(jogo, end=' ')'''

'''from random import randint
dados = []
jogo = []
num_jogo = int(input('Quantos jogos você quer fazer? '))
for c in range(0, num_jogo):
    for num_jogo in range(0,6):
        dados.append(randint(0,60))
        jogo.append(dados[:])
        dados.clear()
'''


