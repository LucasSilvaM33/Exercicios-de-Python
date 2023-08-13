#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('amor', 'cristal', 'lupi', 'pretinha', 'samir', 'lucas', 'hildo', 'zuleide')
for p in palavras:
    print(f'\nNa palavras {p} temos as vogais ', end=' ')
    for letras in p: #para cada letra em p
        if letras.lower() in 'aeiou': #para cada letra.lowe() em p
            print(letras, end=' ')

