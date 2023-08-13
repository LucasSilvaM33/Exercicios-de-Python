"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
# Resolução do professor

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

#Quem é o menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Quem é o maior:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor número é o {menor}')
print(f'O maior número é o {maior}')