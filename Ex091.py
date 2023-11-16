'''Exercício de Python 091: Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado.'''

# Meu metodo mas não deu certo

from random import randint
from time import sleep
from operator import itemgetter

'''dados = {}
ranking = dict()
for c in range(1, 5):
    dados[f'jogador'] = randint(1,6)
    for k, v in dados.items():
        print(f'O {k}{c} tirou {v} no dado')
        sleep(1)
ranking = sorted(dados.items(), key=itemgetter(0))
print(ranking)'''

dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)
         }
ranking = list()
for keys, valves in dados.items():
    print(f'O {keys} tirou {valves} no dado')
    sleep(1)
print('=-'*50)
print()
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True) # Comando que coloca em ordem decrescente
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}. ')
    sleep(1)
