"""Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome"""

name = str(input('Digite o seu nome completo: ')).strip()
print('Verificando se seu nome tem "Silva": ')
var = name.upper()
print(f'A resposta é: {"SILVA" in var} ')