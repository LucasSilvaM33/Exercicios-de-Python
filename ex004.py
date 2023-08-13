'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele'''

nome = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(nome)}')
print(f'Só tem espaço? {nome.isspace()}')
print(f'É um número? {nome.isnumeric()}')
print(f'É alfabético? {nome.isalpha()}')
print(f'É alfanumérico? {nome.isalnum()}')
print(f'Está em maiúsculo? {nome.isupper()}')
print(f'Está em minúsculas? {nome.islower()}')
print(f'Está capitalizada? {nome.istitle()}')