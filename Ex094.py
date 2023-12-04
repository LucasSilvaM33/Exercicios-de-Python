

'''Exercício Python 094: Crie um programa que leia nome, sexo  e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quatas pessoas foram cadastradas.
B) A média de idade.
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
mulheres = []
media = []
dados = dict()
tot = soma = 0
while True:
    dados['Nome'] = str(input('Qual o seu nome? '))
    tot += 1
    dados['Sexo'] = str(input('Qual o seu sexo (M/F) ?')).strip().upper()[0]
    if dados["Sexo"] not in 'Mm':
        mulheres.append(dados["Nome"])
    idade = int(input('Qual a sua idade? '))
    soma += idade

    resp = str(input('Você deseja continuar (S/N) ? ')).strip().upper()[0]
    if resp not in 'Ss':
        break
print(f'Foram cadastradas {tot} pessoas')
print(f'A média das idades cadastradas foram de {soma/tot}')
print(f'A lista de mulheres cadastradas: {mulheres}')

