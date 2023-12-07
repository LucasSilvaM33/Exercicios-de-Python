'''Exercício de Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes di aproveitamento de cada jogador. '''


dados = dict()
totgols = list()
tot = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['partidas'] = int(input('Número de partidas: '))
    for c in range(1, dados['partidas'] + 1):
        gol = int(input(f'Número de gols na {c}° partida: '))
        tot += gol
        totgols.append(gol)
    dados['gols por partida'] = totgols
    dados['total de gols'] = tot
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 50)
print(dados)
print('=-' * 50)
for k, v in dados.items():
    print(f'{k} = {v}')
print('=-' * 50)
for l, c in enumerate(totgols):
    print(f'Na {l + 1}° partida, fez {c} gols')
print(f'Fez um total de {dados["total de gols"]} gols')

