"""Faça um programa que que leia um ano qualquer e mostre se ele é bissexto"""
year = int(input('Digite o ano que você deseja saber se é bissexto. E Coloque 0 para analizar o ano atual. '))

v1 = year % 4 == 0
v3 = year % 400 == 0
v2 = year % 100 != 0

if v1 and v2 or v3:
    print(f'O ano {year} é bissexto.  ')
else:
    print(f'O ano {year} não é bissexto. ')