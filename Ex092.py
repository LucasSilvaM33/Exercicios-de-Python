''' Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. '''

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira'] = int(input('Carteira de trabalho (digite 0 se você não tiver): '))
if dados['carteira'] != 0:
    dados['contrato'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    # Tempo de contribuição / trabalho
    contrib = datetime.now().year - dados['contrato']
    # Leitura do tempo de aposentadoria
    dados['aposentadoria'] = (35 - contrib) + dados['idade']
    # Mostrando resultados
print('-=' * 50)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
