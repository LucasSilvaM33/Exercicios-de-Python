'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela. '''

aluno = dict()

aluno['nome'] = str(input('Qual o seu nome? '))
aluno['media'] = float(input(f'Qual é a média do {aluno["nome"]}? '))
if aluno['media'] >= 7:
    aluno['situação'] = "Aprovado"
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print(f'Aluno: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
print(f'A situação é igual a: {aluno["situação"]}')


