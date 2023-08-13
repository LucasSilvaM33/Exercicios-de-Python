"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo' """

name = str(input('Digite o nome de uma cidade: ')).strip()
var = name.upper()
print(f'A cidade escolhida foi {name}')
print(f'Agora vamos verificar se ela possui Santos em seu nome: {"SANTO" in var} ')