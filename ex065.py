'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
num = media = soma = cont = menor = maior = 0
escolha = ' '
while escolha not in 'Nn':
    num = int(input('Digite um número inteiro qualquer: '))
    escolha = str(input('Quer continuar? [S/N ]')).upper().strip()[0]
    soma = soma + num
    cont = cont + 1
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'A soma foi {soma}, foram {cont} numeros somados, a média foi de {media:.2f} e menor número foi {menor} e o maior foi {maior}')



