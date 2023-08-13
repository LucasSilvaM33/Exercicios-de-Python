"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- Se ele aida vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

seu programa também deverá mostrar o tenmpo que falta ou que passou do prazo."""
from datetime import date #biblioteca de datas
ano_atual = date.today().year #comando para pegar o atual ano do sistema
ano_nascimento = int(input('Qual o ano do seu nascimento? '))
idade = ano_atual - ano_nascimento

if idade == 18:
    print(f'Você tem {idade} anos e tem que se alistar esse ano! Cuidado para não perder o prazo.')
elif idade > 18:
    saldo = idade - 18 #para saber quantos anos já passou o alismento da pessoa
    print(f'Você tem {idade} anos e seu prazo de alistamento já passou.')
    print(f'Você deveria ter se alistado a {saldo} anos')
    ano = ano_atual - saldo
    print(f'Seu alistamento deveria ter sido realizado no ano de {ano}')
else:
    saldo =18 - idade #para saber quantos anos ainda falta para o alistamento da pessoa
    print(f'Você tem {idade} anos e ainda não está apto a se alistar. ')
    print(f'Seu alistamento vai acontecer daqui a {saldo} anos')
    ano = ano_atual + saldo
    print(f'Seu alistamento será realizado no ano de {ano}')