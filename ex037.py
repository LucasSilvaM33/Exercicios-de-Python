"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
 qual será a base de conversão:
 1 - Para binário
 2- Para octal
 3- Para hexadecimal"""

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções: 
[1] Converter para binário: 
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O número {num} convertido para Binério é {bin(num) [2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para Octal é {oct(num [2:])}')
elif opcao == 3:
    print(f'O número {num} convertido para Hexadecimal é {hex(num [2:])}')
else:
    print('Opção invalida, tente novamente! ')

