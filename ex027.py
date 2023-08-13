"""Faça um programa que leia o ome completo de uma pessoa, mostrando em seguinda o primeiro e o último nome
separadamente.
Ex: Ana Maria Souza
Primeiro: Ana
Último: Souza"""

n = str(input('digite o seu nome completo: ')).strip()
name = n.split()
print(f'Seu preimeiro nome é {name[0]}')
print(f'Seu último nome é {name[len(name)]-1}')
