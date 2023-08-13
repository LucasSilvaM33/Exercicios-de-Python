"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
"""

n1 = float(input('Digite a sua nota da n1: '))
n2 = float(input('Digite a sua nota da n2: '))

media = (n1 + n2) / 2

if media >= 7:
    print('Parabéns!!!! Você passou de ano!!!')
    print(f'Sua média foi de {media:.1f}')
elif 5 <= media <= 6.9:
    print(f'Sua média foi de {media:.1f}, infelismente você está de recuperação. ')
else:
    print(f'sua média foi de {media:.1f} ')
    print(f'Você foi reprovado... Estude mais no próximo ano!')
