'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas
mulheres têm menos de 20 anos.
'''
media_idade = 0
soma_idade =0
homemmaisvelho = 0
nomevelho = ' '
numeromulheres = 0
for pessoa in range(1,5):
    print(f'{pessoa}° Pessoa: ')
    nome = str(input('Qual o nome: ')).strip()
    idade = int(input('Qual a idade: '))
    sexo = str(input('Sexo [M/F]')).strip().upper()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        homemmaisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        numeromulheres += 1




media_idade = soma_idade / 4
print(f'Média da idade: {media_idade:.2f} anos')
print(f'O homem mais velho é {nomevelho} e ele tem {homemmaisvelho} anos')
print(f'Número de mulheres que tem menos de 20 anos, é de: {numeromulheres} mulheres')


