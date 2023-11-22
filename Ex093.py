'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante
o campeonato.'''

dados = {}
lista = []
tot = 0
dados['Nome'] = str(input('Nome do jogador: '))
dados['Partidas'] = int(input('Número de partidas jogadas: '))
for c in range(1, dados['Partidas'] + 1):
    gols = int(input(f'Numero de gols na {c}° partida: '))
    tot += gols
    lista.append(gols)
dados['Gols'] = lista
dados['Total'] = tot
print('-=' * 50)
print(dados)
print('-=' * 50)
for k, v in dados.items():
    print(f'- {k}:  {v}')
print('-=' * 50)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partidas')
for l, c in enumerate(lista):
    print(f'Na {l + 1}° partida, fez {c} gols')
print(f'Fez um total de {dados["Total"]} gols')