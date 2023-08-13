"""Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome deles e escrevendo o nome do escolhido"""

from random import choice

aluno_1 = str(input('Qual o nome do primeiro aluno?  '))
aluno_2 = str(input('Qual o nome do segundo aluno? '))
aluno_3 = str(input('Qual o nome do terceiro aluno? '))
aluno_4 = str(input('Qual o nome do quarto aluno? '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
print(f'O aluno escolhi foi {choice(lista)}')
