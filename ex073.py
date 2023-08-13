'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.''' #Fortaleza

times = ('Botafogo', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminese', 'Bragantino', 'Atletico-PR', 'São Paulo', 'Cuiabá',
         'Cruzeiro', 'Fortaleza', 'Internacional', 'Atlético-MG', 'Corinthians', 'Santos', 'Goiás', 'Bahia', 'Coritiba',
          'América-MG', 'Vasco da Gama')
print(f'Os cincos primeiros times são: {times[0:5]}')
print(f'Os 4 últimos times são: {times[16:20]}') #poderia ser -4:
print(f'Os times em ordem alfabetica: {sorted(times)}') #sorted coloca os valores da tupla em ordem
print(f'O fortaleza está na posição {times.index("Fortaleza") + 1}')