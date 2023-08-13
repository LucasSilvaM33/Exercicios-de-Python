'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
id18 = 0
men = 0
women = 0
idwomen = 0
while True:
    idade = int(input('Qual a sua idade? '))
    if idade >= 18:
        id18 += 1
    sexo = str(input('Qual o seu sexo? [F/M]')).strip().upper()[0]
    if sexo == 'M':
        men += 1
    elif sexo == 'F' and idade < 20:
        idwomen += 1
    while sexo not in 'FM':
        print('Sexo inválido. ')
        sexo = str(input('Qual o seu sexo? [F/M]')).strip().upper()[0]
    escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if escolha == 'S':
        print('Ok')
    elif escolha == 'N':
        break
    else:
        print('Opção inválida, tente novamente.')
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if escolha == 'S':
            print('Ok')
        else:
            break
print(f'O número de pessoas que tem mais de 18 anos é de {id18}')
print(f'O número de homens cadastrado foi de {men}')
print(f'O número de mulheres que tem menos de 20 anos é de {idwomen}')


