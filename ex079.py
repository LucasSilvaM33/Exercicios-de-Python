"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente."""

valor = []
escolha = ' '
while True:
    num = int(input('Digite um valor inteiro qualquer: '))
    if num not in valor:
        valor.append(num)
    else:
        print('Valor duplicado...')
        print('Excluído.')
    escolha = str(input('Você quer continuar? [S/N]')).strip().upper()
    if escolha == 'N':
        break
valor.sort()
print(f'Os valores digitados foram {valor}')
print('FIM')
