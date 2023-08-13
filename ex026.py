"""Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'A'
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez"""

frase = str(input('Digite uma frase qualquer:')).upper().strip()

print(f'Quantas vezes aparece a letra "A"? {frase.count("A")}')
print(f'Em que posição ela aparece a primeira vez? {frase.find("A") + 1}')
print(f'Em que posição ela aparece a ultima vez? {frase.rfind("A") + 1}')
