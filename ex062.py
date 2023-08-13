'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

numero = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
#Agora vamos ter duas variáveis
termo = numero
contador = 1
total = 0
escolha = 10
while escolha != 0:
    total = total + escolha#Como o total é 0 no começo, aqui vai dar 10 termos, no decorrer do programa a escolha vai aumentando
    while contador <= total:
        print(f'{termo} -> ', end=' ')
        contador = contador + 1
        termo = termo + razao
    escolha = int(input('\nQuantos termos você quer mostrar a mais? '))

print('FIM')
print(f'Tivemos um total de {total} termos')


