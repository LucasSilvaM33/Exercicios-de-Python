'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. ''''''Seu programa deverá ler um número pelo teclado (entre 0 e 20)
 e mostrá-lo por extenso.'''


usuario = int(input('Digite um número de 0 a 20: '))

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while usuario > 20 or usuario < 0:
    print('Número inválido, tente novamente... ')
    usuario = int(input('Digite um número de 0 a 20:  '))
print(f'Você digitou o número {numeros[usuario]}')





