#outra forma de resver a atividade 53

frase = str(input('digite uma frase qualquer para descobrir se ela é um palíndromo: ')).strip().upper() #strip é para desconsiderar os espaços e upper é para colocar ela toda em maiúscula
palavras = frase.split() #usado para dividir as palavras em grupos. ex bom dia = 'bom' 'dia'
junto = ''.join(palavras) #vai juntar todas as palavras sem espaço da lista

inverso = junto[::-1] #primeiro : = começa do inicio / segundo : = termina no fim / -1 começa de trás para frente

print(f'O inverso de {junto} é {inverso}') #só para ver como as palavras estão iguais
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
