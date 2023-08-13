"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite um segundo número: '))
n3 = float(input('Digite um terceiro número: '))

if n1 > n2 > n3:
    print(f'O maior número é {n1} e o menor é {n3}')
    if n1 > n3 > n2:
        print(f'O maior número é {n1} e o menor é {n2}')
        if n2 > n1 > n3:
            print(f'O maior número é {n2} e o menor é {n3}')
            if n2 > n3 > n1:
                print(f'O maior número é {n2} e o menor é {n1}')
                if n3 > n1 > n2:
                    print(f'O maior número é {n3} e o menor é {n2}')
                    if n3 > n2 > n1:
                        print(f'O maior número é {n3} e o menor é {n1}')

