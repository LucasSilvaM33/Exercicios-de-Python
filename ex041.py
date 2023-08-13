"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
-Até 9 anos: Mirim
-Até 14 anos: Infantil
-Até 19 anos: Junior
-Até 25 anos: Senior
-Acima: Master
-"""

from datetime import date

atual = date.today().year
nascimento = int(input('Qual ano você nasceu? '))
idade = atual - nascimento

if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é Mirim. ')
elif idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é Infantil. ')
elif idade <= 19:
    print(f'Você tem {idade} anos e sua categoria é Junior. ')
elif idade <= 25:
    print(f'Você tem {idade} anos e sua categoria é Sênior. ')
else:
    print(f'Você tem {idade} anos e sua categoria é Master. ')
