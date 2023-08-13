'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
 desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('digite uma frase qualquer para descobrir se ela é um palíndromo: ')).strip().upper() #strip é para desconsiderar os espaços e upper é para colocar ela toda em maiúscula
palavras = frase.split() #usado para dividir as palavras em grupos. ex bom dia = 'bom' 'dia'
junto = ''.join(palavras) #vai juntar todas as palavras sem espaço da lista
inverso = ''
#O primeiro -1 vai pegar o número de letras do junto e vai tirar 1, por que se a palavra tem 20 letras, o python vai do 0 ao 19
#O segundo -1 é a letra antes da primeira
#O terceiro -1 é que ele vai voltando uma letra
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {frase} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')



