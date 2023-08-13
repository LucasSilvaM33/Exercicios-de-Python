'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. ''''''Seu programa deverá ler um número pelo teclado (entre 0 e 20)
 e mostrá-lo por extenso.'''
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
escolha = ' '
while escolha not in 'N':
    usuario = int(input('Escolha um número de 0 a 20: '))
    if 0 <= usuario <= 20:
        print(f'A forma extensa do número {usuario} é {numeros[usuario]}')
    else:
        print('Opção invalida.', end=' ')
    escolha = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
print('Fim do Programa... ')

