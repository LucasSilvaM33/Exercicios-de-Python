"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro"""

nome = str(input('Qual o seu completo? ')).strip()
print(f'O seu nome todo em maiúsculas fica: {nome.upper()}')
print(f'O seu nome todo em minúscula fica: {nome.lower()}')
print(f'Seu nome tem ao todo  {len(nome) - nome.count(" ")} letras ')
print(f'O seu primeiro nome tem {nome.find(" ")} letras')
#outra maneira
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras') #separa[0] está selecionando o primeiro agrupamento do nome, ex: 'Lucas' = 0 'Martins' = 1